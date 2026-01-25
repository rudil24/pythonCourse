# Day 48: Cookie Clicker Bot - Chat Transcript

## 1. Initial Setup
**User:**
Rudi Lewis: follow the comment thread in this main.py to create all necessary code. don't delete any comments already in main.py. separate classes you make into other .py files in same directory: day048

**Gemini:**
To implement the automated Cookie Clicker bot as requested, I will create a new file `cookie_bot.py` to encapsulate the game interaction logic and modify `main.py` to run the bot.

The bot will target the official Cookie Clicker version (v2) which includes the language selection screen mentioned in the instructions.

### `cookie_bot.py`
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class CookieClickerBot:
    def __init__(self, driver):
        self.driver = driver
        self.url = "[https://orteil.dashnet.org/cookieclicker/](https://orteil.dashnet.org/cookieclicker/)"

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
        # Get current cookie count
        try:
            cookies_text = self.driver.find_element(By.ID, "cookies").text
            # Format is usually "100 cookies\nper second: 10"
            if not cookies_text:
                return
            # Split to get the number and remove commas
            current_cookies = int(cookies_text.split("\n")[0].split(" ")[0].replace(",", ""))
        except (ValueError, IndexError, NoSuchElementException, StaleElementReferenceException):
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
                product_to_buy.click()
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
```

### `main.py`
```python
# 5. Once you've managed to get the bot to work, feel free to tweak the algorithm if you think there is a better way to play the game. e.g. Change the time, instead of every 5 seconds to check the upgrades, what if you did every second or every 10 seconds? Or maybe the bot should buy all the affordable upgrades. Post your algorithm in the Q&A and impress us all if you manage to get a higher cookies/second with your algo.
# 6. Use good coding style. Break your code into functions where possible, use meaningful variable names, and add comments where necessary to explain your logic.

import time
from selenium import webdriver
from cookie_bot import CookieClickerBot

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
bot = CookieClickerBot(driver)
bot.start_game()

# Timers
timeout = time.time() + 5
five_min = time.time() + 60 * 5 # 5 minutes

while True:
    bot.click_cookie()

    # Every 5 seconds check for upgrades
    if time.time() > timeout:
        bot.check_and_buy_upgrades()
        timeout = time.time() + 5

    # After 5 minutes stop and print result
    if time.time() > five_min:
        cps = bot.get_cookies_per_second()
        print(f"cookies/second: {cps}")
        break
```

---

## 2. URL Change
**User:**
run the game from https://ozh.github.io/cookieclicker/ instead (the self.url you are going to currently on orteil has "are you human" checks, we don't want to mess with that.)

**Gemini:**
Here is the updated code for `cookie_bot.py` with the URL changed to the version without the "are you human" checks.

### `cookie_bot.py` (Update)
```python
class CookieClickerBot:
    def __init__(self, driver):
        self.driver = driver
        # self.url = "[https://orteil.dashnet.org/cookieclicker/](https://orteil.dashnet.org/cookieclicker/)"
        self.url = "[https://ozh.github.io/cookieclicker/](https://ozh.github.io/cookieclicker/)"
    
    # ... rest of class
```

---

## 3. Terminal Feedback
**User:**
need a little more feedback at the terminal while the program is running. can you add a print statement for every minute elapsed from 1-4 "x minutes elapsed", and a print statement for every upgrade bought "bought y upgrade for z cookies"

**Gemini:**
I've added a `start_time` variable and a check inside the loop to print the elapsed time every minute. In `cookie_bot.py`, I've updated `check_and_buy_upgrades` to fetch the upgrade name and print the purchase details.

### `main.py` (Update)
```python
bot.start_game()

# Timers
start_time = time.time()
timeout = time.time() + 5
five_min = time.time() + 60 * 5 # 5 minutes
next_minute = start_time + 60

while True:
    bot.click_cookie()

    if time.time() > timeout:
        bot.check_and_buy_upgrades()
        timeout = time.time() + 5

    if time.time() > next_minute:
        print(f"{int((time.time() - start_time) / 60)} minutes elapsed")
        next_minute += 60

    # After 5 minutes stop and print result
    if time.time() > five_min:
        # ...
```

### `cookie_bot.py` (Update)
```python
    # ... inside check_and_buy_upgrades ...
    # Buy the most expensive affordable upgrade
    if affordable_upgrades:
        # Sort by price descending
        affordable_upgrades.sort(key=lambda x: x[0], reverse=True)
        highest_price, product_to_buy = affordable_upgrades[0]
        
        try:
            upgrade_name = product_to_buy.find_element(By.CSS_SELECTOR, ".title").text
        except NoSuchElementException:
            upgrade_name = "Unknown"

        try:
            product_to_buy.click()
            print(f"bought {upgrade_name} upgrade for {highest_price} cookies")
        except StaleElementReferenceException:
            pass
```

---

## 4. Cookies/Second Feedback
**User:**
also add a line to print the current cookies/second when you print each minute "1 minute elapsed" "cookies/second: xx"

**Gemini:**
I've updated `main.py` to fetch and print the cookies per second rate every minute.

### `main.py` (Update)
```python
    if time.time() > next_minute:
        print(f"{int((time.time() - start_time) / 60)} minutes elapsed")
        cps = bot.get_cookies_per_second()
        print(f"cookies/second: {cps}")
        next_minute += 60
```

---

## 5. Logic Updates & Backup
**User:**
two problems i see. 
1. we're missing quite a few upgrades (buttons) located in the divs within this xpath: `//*[@id="upgrades"]`. you'll see divs in there with data-id: [0-10] that connect to tooltips Game.crateTooltip(Game.UpgradesById[0-10]. Can you investigate those and see if they will add more bang for the buck to buy those? playing it manually it seems like they are doing much more impact than Cursors and Grandmas. 
2. We're also "never getting to" the big upgrades like Mine because we buy things every 5 seconds. let's only buy every 5 seconds for the first 30 seconds, then add 5 seconds to that wait every 30 seconds, (from secs 30-60 we buy every 10 seconds, from secs 60-90 we buy every 15 seconds, etc. so we can accrue enough cookies to buy better stuff. 
3. also, save a copy of current files with the append of `_v1` before you make changes in the `main.py` and `cookie_bot.py`.

**Gemini:**
Here are the changes. First, I will create the backup files `cookie_bot_v1.py` and `main_v1.py` with the current code. Then, I will modify `cookie_bot.py` to include the logic for buying tech upgrades and `main.py` to implement the dynamic wait time strategy.

### 5.1 Backups
(Content of `cookie_bot_v1.py` and `main_v1.py` would match the code from step 4).

### 5.2 `cookie_bot.py` (Final)
```python
    def check_and_buy_upgrades(self):
        """Checks affordable upgrades and buys the most expensive one."""
        
        # Check for special tech upgrades (in the store top section)
        try:
            # Find enabled upgrades (affordable and unlocked)
            upgrades = self.driver.find_elements(By.CSS_SELECTOR, "#upgrades .crate.upgrade.enabled")
            
            for upgrade in upgrades:
                try:
                    upgrade.click()
                    print("Bought a tech upgrade")
                except Exception:
                    pass
        except Exception:
            pass

        # ... (Rest of original building purchase logic follows) ...
```

### 5.3 `main.py` (Final)
```python
# ... imports ...

bot.start_game()

# Timers
start_time = time.time()
timeout = time.time() + 5
five_min = time.time() + 60 * 5 # 5 minutes
next_minute = start_time + 60

while True:
    bot.click_cookie()

    # Check for upgrades with dynamic timeout
    if time.time() > timeout:
        bot.check_and_buy_upgrades()
        
        # Dynamic wait calculation: 5s initially, add 5s for every 30s elapsed
        elapsed = time.time() - start_time
        interval = 5 + (int(elapsed / 30) * 5)
        timeout = time.time() + interval

    # Every minute print elapsed time and cookies/second
    if time.time() > next_minute:
        print(f"{int((time.time() - start_time) / 60)} minutes elapsed")
        cps = bot.get_cookies_per_second()
        print(f"cookies/second: {cps}")
        next_minute += 60

    # After 5 minutes stop and print result
    if time.time() > five_min:
        cps = bot.get_cookies_per_second()
        print(f"cookies/second: {cps}")
        break
```