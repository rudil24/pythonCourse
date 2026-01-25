# rudil24
# use selenium package to interact with Wikipedia page https://en.wikipedia.org/wiki/Main_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import (
    Keys,
)  # for sending keyboard keys. ⌘🖱(Cmd+Click) on Keys above to see all available keys

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# locate the element containing the number of articles in English
# num_articles = driver.find_element(
#     By.XPATH,
#     value='//*[@id="articlecount"]/ul/li[2]/a[1]',  # had to do it by xpath since wikipedia has changed their structure, and Angela's method in her solution takes the first element (active editors)
# )
# print(num_articles.text)
# # click on the link to go to the page with more details about the number of articles
# num_articles.click() # careful with clicks, anything below this will be regarding where we clicked to if we don't comment it out.

# # find element by link text
# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# find the search <input> by name
search_box = driver.find_element(By.NAME, value="search")
# type a search term in the box
search_box.send_keys("Python programming language")
# submit the search form
search_box.submit()
# close the browser
# driver.quit()
