# rudil24
# Music Time Machine Project
# Day 46 of the 100 Days of Code: Python Pro Bootcamp
from billboard_history_scraper import BillboardHistoryScraper

if __name__ == "__main__":
    scraper = BillboardHistoryScraper()

    # user input
    user_date = input("Enter a date (YYYY-MM-DD): ")  # e.g., 1977-08-16

    # method to get chart data for the specified date
    data = scraper.get_chart(user_date)

    if "error" in data:
        print(f"Error: {data['error']}")
    else:
        # get data for week of
        print(f"Top 100 songs for the week of {data['week_of']}:")
        print("-" * 50)

        # We assume the list is named 'data' in the return object
        for i, song in enumerate(data["data"][:100], 1):
            # We use .get() to avoid crashes if a column name varies slightly
            title = song.get("Song Title", "Unknown Title")
            artist = song.get("Artist", "Unknown Artist")
            print(f"{i}. {title} by {artist}")
