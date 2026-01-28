from soup_scraper import SoupScraper
from selenium_form_writer import SeleniumFormWriter


def main():
    print("Starting Zillow Rental Alerts Automation...")

    # 1. Scrape Data
    scraper = SoupScraper()
    print("Scraping data from Zillow Clone...")
    addresses, prices, links = scraper.get_listings()

    if not addresses:
        print("No data found. Exiting.")
        return

    print(f"Successfully scraped {len(addresses)} listings.")
    print("Sample Data:")
    print(f"Address: {addresses[0]}")
    print(f"Price: {prices[0]}")
    print(f"Link: {links[0]}")

    # 2. Fill Form
    print("Initializing Selenium to fill Google Form...")
    form_writer = SeleniumFormWriter()
    form_writer.fill_form(addresses, prices, links)


if __name__ == "__main__":
    main()
