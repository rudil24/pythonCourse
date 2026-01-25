import os
import time
import requests
from billboard_history_scraper import BillboardHistoryScraper


def backup_entire_history():
    # Initialize the scraper just to get the list of years/GIDs
    scraper = BillboardHistoryScraper()

    # Create a folder for the backup so we don't clutter your project
    folder_name = "billboard_raw_backup"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    print(f"--- Starting Full Backup into '{folder_name}/' ---")

    # 1. Fetch the directory of tabs
    scraper._fetch_gid_map()

    # Sort years so we download in order (1958 -> 2024)
    # We filter to ensure we only get valid 4-digit years
    years = sorted([y for y in scraper.gid_map.keys() if y.isdigit()])

    print(f"Found {len(years)} years of data to save.")
    print("-" * 40)

    # 2. Loop through every year and download the raw CSV
    for year in years:
        gid = scraper.gid_map[year]
        filename = os.path.join(folder_name, f"billboard_{year}.csv")

        # We use the CSV Export URL strategy directly
        root_url = scraper.base_url.replace("/pubhtml", "/pub")
        csv_url = f"{root_url}?gid={gid}&single=true&output=csv"

        print(f"Saving {year}...", end=" ", flush=True)

        try:
            response = requests.get(csv_url, headers=scraper.headers)

            if response.status_code == 200:
                # write the content to a file
                with open(filename, "wb") as f:
                    f.write(response.content)
                print("✅ Done")
            else:
                print(f"❌ Failed (Status {response.status_code})")

        except Exception as e:
            print(f"❌ Error: {e}")

        # Sleep briefly to be polite to Google's servers
        time.sleep(1.5)

    print("-" * 40)
    print("Backup Complete! You now own the data.")


if __name__ == "__main__":
    backup_entire_history()
