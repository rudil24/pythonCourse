# rudil24
# billboard_history_scraper.py
# A web scraper for the Google Sheet (and its tabs for each year) that contain the Billboard Hot 100 weekly charts on mindformusic.com/billboard-history
import requests
import csv
import re
from datetime import datetime, timedelta
from io import StringIO


class BillboardHistoryScraper:
    def __init__(self):
        # The public HTML URL (used for finding the list of years)
        self.base_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTWNjuOrkBTQWWevMolvRrBt0IKk_TPXAA-YX8S_6PKjrPAkgS69XoEnfzGysJ-Vbrw_0g9GUiZnc3U/pubhtml"

        # The "Secret" API Endpoint
        # We replace '/pubhtml' with '/tq' (Table Query)
        self.api_url = self.base_url.replace("/pubhtml", "/tq")

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.gid_map = {}

    def _fetch_gid_map(self):
        """
        Fetches the master page just to find the map of 'Year' -> 'gid'.
        """
        print("Fetching sheet directory...")
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching base URL: {e}")
            return

        # Regex to find Year and GID
        # Pattern: name: "1977" ... gid: "1401499388"
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

        # --- THE FIX ---
        # We use the /tq endpoint with 'tqx=out:csv'
        # This forces the Google Visualization API to return raw CSV data.
        # It is strictly for data transfer, so it never sends HTML loading screens.
        query_url = f"{self.api_url}?tqx=out:csv&gid={gid}"

        print(f"Fetching clean data for {year_str} (GID: {gid})...")
        response = requests.get(query_url, headers=self.headers)

        if response.status_code != 200:
            return {"error": f"API Failed (Status {response.status_code})"}

        # Parse CSV content
        f = StringIO(response.text)
        reader = csv.reader(f)
        rows = list(reader)

        if not rows:
            return {"error": "API returned empty data."}

        # --- Header Detection ---
        header_map = {}
        start_row = 0

        # Scan first 10 rows for "Song Title"
        for i, row in enumerate(rows[:10]):
            row_lower = [str(c).lower().strip() for c in row]
            if "song title" in row_lower:
                for idx, col_name in enumerate(row):
                    if col_name.strip():
                        header_map[idx] = col_name.strip()
                start_row = i + 1
                break

        if not header_map:
            # Fallback: Sometimes the API returns headers in row 0 perfectly
            # Let's assume row 0 is header if we failed to find "Song Title" explicitly
            # but usually, this means something is wrong. Let's return error to be safe.
            return {
                "error": f"Could not find headers. First row data: {rows[0] if rows else 'Empty'}"
            }

        # Find Date Column
        date_col_idx = -1
        for idx, name in header_map.items():
            if "Date" in name:
                date_col_idx = idx
                break

        if date_col_idx == -1:
            return {"error": "Could not find 'Date' column."}

        # --- Date Filtering ---
        closest_date = None
        closest_diff = timedelta(days=365)
        valid_rows = []

        for row in rows[start_row:]:
            if len(row) <= date_col_idx:
                continue

            date_text = row[date_col_idx]
            if not date_text:
                continue

            try:
                row_date = None
                # Billboard data usually uses Month/Day/Year
                for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%Y/%m/%d"):
                    try:
                        row_date = datetime.strptime(date_text, fmt)
                        break
                    except ValueError:
                        continue

                if row_date:
                    valid_rows.append((row_date, row))
                    # We look for dates BEFORE or ON the target
                    if row_date <= target_date:
                        diff = target_date - row_date
                        if diff < closest_diff:
                            closest_diff = diff
                            closest_date = row_date
            except:
                continue

        if closest_date is None:
            return {"error": f"No chart found on or before {target_date_str}."}

        # --- Build Final List ---
        final_chart = []
        for r_date, row in valid_rows:
            if r_date == closest_date:
                entry = {}
                for idx, col_name in header_map.items():
                    if idx < len(row):
                        entry[col_name] = row[idx]
                final_chart.append(entry)

        return {"week_of": closest_date.strftime("%Y-%m-%d"), "data": final_chart}
