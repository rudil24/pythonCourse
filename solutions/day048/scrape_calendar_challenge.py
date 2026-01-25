# rudil24
# use selenium package to scrape the elements of the "Upcoming Events" calendar on https://www.python.org/ homepage
# into a dictionary within a dictionary as follows (first two example elements are accurate to existing page on 2026-01-23):
# {0: {'time': '2026-01-27', 'name': 'PyLadies Amsterdam: Robotics beginner class with MicroPython'}, 1: {'time': '2026-01-31', 'name': 'Python Devroom @ FOSDEM 2026'}, ... }
# and print that dictionary
# CREATE CODE BELOW THIS LINE
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
driver.quit()
# it works!
