from selenium import webdriver

# keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# then my code to access that chrome tab that driver.get opened goes below
# ...
# ...

# # cleanup - close browsers
# # to close a single selenium-driven browser tab (the active tab)
# driver.close()

# # to close ALL OPEN selenium-driven tabs and windows
# driver.quit()
