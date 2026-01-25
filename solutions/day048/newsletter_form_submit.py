# rudil24
# Day 48 exercise: newsletter_form_submit.py FEATURING selenium web automation
# use selenium package methods to "sign up" for Angela's newsletter on her "example" site: https://secure-retreat-92358.herokuapp.com/
# fill in the first name, last name, email fields from the constants below, and click the submit button
FIRST_NAME = "Rudi"
LAST_NAME = "Lewis"
EMAIL = "rudil24@gmail.com"
# CREATE CODE BELOW THIS LINE
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# very cool way to combine the "find_element" with the "send keys" action
driver.find_element(By.NAME, value="fName").send_keys(FIRST_NAME)
driver.find_element(By.NAME, value="lName").send_keys(LAST_NAME)
driver.find_element(By.NAME, value="email").send_keys(EMAIL)

driver.find_element(By.CSS_SELECTOR, value="form button").click()
