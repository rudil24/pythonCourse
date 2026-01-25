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
        # Base URL for the directory
        self.base_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTWNjuOrkBTQWWevMolvRrBt0IKk_TPXAA-YX8S_6PKjrPAkgS69XoEnfzGysJ-Vbrw_0g9GUiZnc3U/pubhtml"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.gid_map = {}

    def _fetch_gid_map(self):
        print("Fetching sheet directory (Version: CSV Strategy)...")
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching base URL: {e}")
            return

        # Regex to find Year and GID
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

        # --- THE CSV URL STRATEGY ---
        # We replace '/pubhtml' with '/pub' and add output=csv
        # This is the standard "Download" link for published sheets
        root_url = self.base_url.replace("/pubhtml", "/pub")
        csv_url = f"{root_url}?gid={gid}&single=true&output=csv"

        print(f"Downloading CSV for {year_str} (GID: {gid})...")
        response = requests.get(csv_url, headers=self.headers)

        # If Google returns HTML (login page/loading screen) instead of text, we know it failed
        if "html" in response.headers.get("Content-Type", "").lower():
            print(
                "DEBUG: Google returned HTML instead of CSV. This sheet might block raw downloads."
            )
            # We return an error so we don't crash
            return {"error": "Google blocked the CSV download (received HTML)."}

        if response.status_code != 200:
            return {"error": f"Download Failed (Status {response.status_code})"}

        # Parse CSV
        try:
            f = StringIO(response.text)
            reader = csv.reader(f)
            rows = list(reader)
        except Exception as e:
            return {"error": f"Failed to parse CSV: {e}"}

        if not rows:
            return {"error": "CSV data was empty."}

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
            return {
                "error": f"Could not find headers (Song Title) in the first 10 rows."
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
