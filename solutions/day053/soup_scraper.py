import requests
from bs4 import BeautifulSoup


class SoupScraper:
    """
    Scrapes listing data from the Zillow Clone site.
    """

    def __init__(self):
        self.url = "https://appbrewery.github.io/Zillow-Clone/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }
        # Headers above required to mimic a real browser request

    def get_listings(self):
        """
        Fetches the webpage and extracts listing addresses, prices, and links.
        Returns:
            tuple: (addresses, prices, links) where each is a list of strings.
        """
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return [], [], []

        soup = BeautifulSoup(response.text, "html.parser")

        # 1. Create a list of links
        link_elements = soup.select(".StyledPropertyCardDataArea-anchor")
        links = [link.get("href") for link in link_elements]

        # 2. Create a list of prices
        price_elements = soup.select(".PropertyCardWrapper__StyledPriceLine")
        prices = []
        for price in price_elements:
            # Clean up: "$1,234+ /mo" -> "$1,234"
            text = price.get_text()
            clean_price = text.split("/")[0].split("+")[0].strip()
            prices.append(clean_price)

        # 3. Create a list of addresses
        address_elements = soup.select("address")
        addresses = []
        for address in address_elements:
            # Clean up: Remove newlines, pipes, extra whitespace
            text = address.get_text()
            clean_address = text.replace("\n", " ").replace("|", " ").strip()
            # Collapse multiple spaces
            clean_address = " ".join(clean_address.split())
            addresses.append(clean_address)

        return addresses, prices, links
