# rudil24
# Day 48:# 100 Days of Code™: The Complete Python Pro Bootcamp
# Challenge: Create an Automated Game Playing Bot
# 1. Go to the game on github pages and familiarise yourself with how it works:
# https://github.com/ozh/cookieclicker (new version)
# 2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
# Note that you will need to find a way to automatically dismiss the language selection before you can get started.
# 3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. You'll need to check how much money (cookies) you have against the price of each upgrade.
# e.g. both Grandma and Cursor are affordable as we have 105 cookies, but Grandma is the more expensive one, so we'll purchase that instead of the cursor.
# I reckon the most challenging part will be figuring out how to select the most expensive item every 5 seconds, since the upgrades become available only gradually over time.
# HINT 1: https://www.w3schools.com/python/ref_string_split.asp
# HINT 2: https://www.w3schools.com/python/ref_string_strip.asp
# HINT 3: https://www.w3schools.com/python/ref_string_replace.asp
# HINT 4: https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
# 4. After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is mine:
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
start_time = time.time()
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes
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
