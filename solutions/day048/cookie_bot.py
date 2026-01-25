from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)


class CookieClickerBot:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://ozh.github.io/cookieclicker/"

    def start_game(self):
        """Navigates to the game and handles the language selection prompt."""
        self.driver.get(self.url)

        # Wait for and click the language selection (English)
        try:
            lang_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "langSelect-EN"))
            )
            lang_select.click()
        except:
            print("Language selection not found or timed out.")

        # Wait for the main game to load (Big Cookie visible)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "bigCookie"))
        )

    def click_cookie(self):
        """Clicks the big cookie once."""
        try:
            self.driver.find_element(By.ID, "bigCookie").click()
        except Exception:
            pass

    def check_and_buy_upgrades(self):
        """Checks affordable upgrades and buys the most expensive one."""
        # Check for special tech upgrades (in the store top section)
        try:
            # Find enabled upgrades (affordable and unlocked)
            upgrades = self.driver.find_elements(
                By.CSS_SELECTOR, "#upgrades .crate.upgrade.enabled"
            )
            for upgrade in upgrades:
                try:
                    upgrade.click()
                    print("Bought a tech upgrade")
                except Exception:
                    pass
        except Exception:
            pass

        # Get current cookie count
        try:
            cookies_text = self.driver.find_element(By.ID, "cookies").text
            # Format is usually "100 cookies\nper second: 10"
            if not cookies_text:
                return
            # Split to get the number and remove commas
            current_cookies = int(
                cookies_text.split("\n")[0].split(" ")[0].replace(",", "")
            )
        except (
            ValueError,
            IndexError,
            NoSuchElementException,
            StaleElementReferenceException,
        ):
            return

        # Find all unlocked products (buildings)
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product.unlocked")

        affordable_upgrades = []

        for product in products:
            try:
                # Get the price of the product
                price_text = product.find_element(By.CSS_SELECTOR, ".price").text
                if not price_text:
                    continue

                # Parse price (remove commas)
                price = int(price_text.replace(",", ""))

                if current_cookies >= price:
                    affordable_upgrades.append((price, product))
            except (ValueError, StaleElementReferenceException, NoSuchElementException):
                continue

        # Buy the most expensive affordable upgrade
        if affordable_upgrades:
            # Sort by price descending
            affordable_upgrades.sort(key=lambda x: x[0], reverse=True)
            highest_price, product_to_buy = affordable_upgrades[0]

            try:
                upgrade_name = product_to_buy.find_element(
                    By.CSS_SELECTOR, ".title"
                ).text
            except NoSuchElementException:
                upgrade_name = "Unknown"

            try:
                product_to_buy.click()
                print(f"bought {upgrade_name} upgrade for {highest_price} cookies")
            except StaleElementReferenceException:
                pass

    def get_cookies_per_second(self):
        """Returns the cookies per second rate as a string."""
        try:
            cookies_text = self.driver.find_element(By.ID, "cookies").text
            parts = cookies_text.split("\n")
            if len(parts) > 1:
                return parts[1].replace("per second: ", "")
        except NoSuchElementException:
            pass
        return "0"
