from selenium import webdriver
from selenium.webdriver.common.by import By

# nice 5070ti laptop (Thunderobot Radiant 16 i9 5070Ti 2.5K 300Hz Gaming Laptop, NVIDIA GeForce RTX 5070 Ti, Core i9-13900HX, 16" QHD+ 300Hz Display, 32GB DDR5, 1TB SSD, RGB Backlit KB, Wi-Fi 6, Win 11 Home, Black)
ITEM1 = "https://www.amazon.com/Thunderobot-Radiant-16-GeForce-i9-13900HX/dp/B0FZLBKYC4/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.35c3a4b6-c692-4e40-a10a-4f3d93be8195%3Aamzn1.sym.35c3a4b6-c692-4e40-a10a-4f3d93be8195&crid=3RXM096SAUY8C&th=1"
SITE2 = "https://www.python.org/"

# keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(ITEM1)  # get the Amazon item page
driver2 = webdriver.Chrome(options=chrome_options)
driver2.get(SITE2)  # get the python.org page


# then my code to access that chrome tab that driver.get opened goes below
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver2.find_element(
    By.NAME, value="q"
)  # when you find a web form entry it is a ripe area for NAME locators, since they often hold the form field names
print(search_bar.get_attribute("placeholder"))
# the placeholder at the q element is "Search"

button = driver2.find_element(By.ID, value="submit")
print(button.get_attribute("value"))
print(button.size)

documentation_link = driver2.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a"
)  # great way to find "the first anchor tag within this CSS_SELECTOR"
print(documentation_link.text)

# use xpath to drill right to a specific element.  you can right click on the element in developer tools window, "copy xpath"
community_link = driver2.find_element(
    By.XPATH, value='//*[@id="container"]/li[4]/a'
)  # use single quotes to surround this one, since it has double quotes already in the content
print(community_link.text)

# # cleanup - close browsers
# # to close a single selenium-driven browser tab (the active tab)
# driver.close()

# to close ALL OPEN selenium-driven tabs and windows use "quit" instead of "close"
driver.quit()
driver2.quit()
