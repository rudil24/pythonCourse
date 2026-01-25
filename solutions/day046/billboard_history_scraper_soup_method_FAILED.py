# rudil24
# billboard_history_scraper.py
# A web scraper for the Google Sheet (and its tabs for each year) that contain the Billboard Hot 100 weekly charts on mindformusic.com/billboard-history
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta


class BillboardHistoryScraper:
    def __init__(self):
        # The Master URL (Published to Web root)
        self.base_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTWNjuOrkBTQWWevMolvRrBt0IKk_TPXAA-YX8S_6PKjrPAkgS69XoEnfzGysJ-Vbrw_0g9GUiZnc3U/pubhtml"
        self.headers = {
            # Using a standard browser string to avoid being served a mobile/limited version
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.gid_map = {}

    def _fetch_gid_map(self):
        """
        Fetches the master page to map 'Year' -> 'gid'.
        """
        print("Fetching sheet directory...")
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching base URL: {e}")
            return

        # Regex to find the Year and GID in the page's JavaScript
        # Matches pattern: {name: "1977", ... gid: "1401499388"}
        matches = re.findall(r'name:\s*"(\d{4})"[^}]*?gid:\s*"(\d+)"', response.text)

        for year, gid in matches:
            self.gid_map[year] = gid

        print(f"Found {len(self.gid_map)} years (Tabs).")

    def get_chart(self, target_date_str):
        if not self.gid_map:
            self._fetch_gid_map()

        try:
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        except ValueError:
            return {"error": "Invalid date format. Use YYYY-MM-DD"}

        year_str = str(target_date.year)

        if year_str not in self.gid_map:
            return {"error": f"No tab found for the year {year_str}."}

        gid = self.gid_map[year_str]

        # --- KEY FIX ---
        # We use 'single=true' to get just the sheet.
        # We REMOVED 'widget=true' which was causing the 'No Table' error.
        # We add &output=html to force the static HTML render
        sheet_url = f"{self.base_url}?gid={gid}&single=true&output=html"

        print(f"Fetching data for {year_str} (GID: {gid})...")
        response = requests.get(sheet_url, headers=self.headers)

        # Parse the Table
        soup = BeautifulSoup(response.text, "html.parser")

        # Google Sheets published tables usually have the class 'waffle'
        table = soup.find("table")

        if not table:
            # Debugging block: If this hits, we see what Google actually sent
            print("DEBUG: Table not found. Response start:", response.text[:200])
            return {"error": "Could not find data table in the sheet response."}

        # Parse Headers (Song Title, Artist, Date)
        rows = table.find_all("tr")
        header_map = {}
        start_row = 0

        # Scan first 10 rows for headers
        for r_idx, row in enumerate(rows[:10]):
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            # We look for "Song Title" specifically
            if "Song Title" in cells:
                for c_idx, cell_text in enumerate(cells):
                    if cell_text:
                        header_map[c_idx] = cell_text
                start_row = r_idx + 1
                break

        if not header_map:
            return {"error": "Could not detect table headers (Song Title/Artist)."}

        # Find 'Date' column index
        date_col_idx = -1
        for idx, name in header_map.items():
            if "Date" in name:
                date_col_idx = idx
                break

        if date_col_idx == -1:
            return {"error": "Could not find 'Date' column."}

        # Scan for closest date
        closest_date = None
        closest_diff = timedelta(days=365)
        valid_rows = []

        for row in rows[start_row:]:
            cells = row.find_all("td")
            # Skip rows that are too short
            if len(cells) <= date_col_idx:
                continue

            date_text = cells[date_col_idx].get_text(strip=True)
            if not date_text:
                continue

            try:
                # Handle formats like 8/16/1977 or 1977-08-16
                row_date = None
                for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%Y/%m/%d"):
                    try:
                        row_date = datetime.strptime(date_text, fmt)
                        break
                    except ValueError:
                        continue

                if row_date:
                    valid_rows.append((row_date, row))
                    if row_date <= target_date:
                        diff = target_date - row_date
                        if diff < closest_diff:
                            closest_diff = diff
                            closest_date = row_date
            except Exception:
                continue

        if closest_date is None:
            return {
                "error": f"No charts found on or before {target_date_str} in {year_str}."
            }

        # Extract songs for the closest date
        final_chart = []
        for r_date, row in valid_rows:
            if r_date == closest_date:
                entry = {}
                cells = row.find_all("td")
                for col_idx, col_name in header_map.items():
                    if col_idx < len(cells):
                        entry[col_name] = cells[col_idx].get_text(strip=True)
                final_chart.append(entry)

        return {"week_of": closest_date.strftime("%Y-%m-%d"), "data": final_chart}
