from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumFormWriter:
    """
    Automates filling out a Google Form using Selenium.
    """

    def __init__(self):
        self.form_url = "https://docs.google.com/forms/d/e/1FAIpQLScqa1QPYcn1F-iU5rsIBFNDL8rZses1bsNCXTtlIKCA-7Dc3A/viewform"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def fill_form(self, addresses, prices, links):
        """
        Iterates through the provided lists and fills the form for each entry.
        """
        for i in range(len(addresses)):
            self.driver.get(self.form_url)
            time.sleep(2)  # Wait for page load

            # Find all text inputs (Address, Price, Link)
            # Google Forms typically uses input[type='text'] for short answers
            text_inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")

            if len(text_inputs) >= 3:
                # Price
                text_inputs[0].send_keys(prices[i])
                # Address
                text_inputs[1].send_keys(addresses[i])
                # Link
                text_inputs[2].send_keys(links[i])

                # Submit Button
                submit_button = self.driver.find_element(
                    By.XPATH, "//span[text()='Submit']"
                )
                submit_button.click()
            else:
                print("Error: Could not find input fields.")
                break

            time.sleep(1)

        print(f"Finished filling {len(addresses)} forms.")
