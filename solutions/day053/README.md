# Zillow Rental Alerts using Data Entry Job Automation - Rudi Lewis
Day 53 Project in the 100 days of Python!
## Project Description
Apply everything we've learned about website and web scraping with Beautiful Soup and Selenium to create a program
that researches Zillow listings based on rental objectives of the Customer, and "scrapes" those listings into an offline Google Sheet to share with the Customer.
(We'll be using an App Brewery cloned version of Zillow for the project.)

## Deliverables
### MVP: 
- [x] Understand Customer Needs
  - [x] **Inputs: Zillow search: San Francisco, For Rent, 1 bedroom apt, <= $3000 / month** *(searched via BeautifulSoup scraping the Zillow clone website)*
  - [x] **Outputs: Price, address, URL for the zillow listing** *(via Selenium typing to a Google Form front-end that produces a Google Sheet)*
- [x] build the program that satisfies customer needs 
  - [x] [FINAL OUTPUT](https://docs.google.com/spreadsheets/d/1_9Omb50fIaFTUEfs8ukAXJO6gQMMu8DwAw5g8RznSKw/edit?usp=sharing)
- [x] utilize object oriented programming wherever possible (classes and methods in separate external files, use class inheritance, keep main.py very tight and readable for flow.)
- [x] employ great documentation in any and all *.py files, written so other developers and casuals can easily understand your code blocks and flow
<!-- 
### Stretch Goals:
- [ ] 
### Super Stretch Goals:
- [ ] 
-->

## To Run
  1. For now, clone to local deployment only. 
     - Requires:
       - **Requests** http package available on pypi.org
       - **BeautifulSoup** bs4 package available on pypi.org
       - **Selenium** package available on pypi.org
  2. I built it in Python 3.14.2, but I think it should work in any 3.x based on the standard libraries and code used.

## Development Workflow
- [x] 1. Create the [Google Form](https://docs.google.com/forms/d/e/1FAIpQLScqa1QPYcn1F-iU5rsIBFNDL8rZses1bsNCXTtlIKCA-7Dc3A/viewform?usp=publish-editor)
- [x] 2. Write the soup_scraper.py to use BeautifulSoup/Requests to scrape all the listings from the [Zillow-Clone web address](https://appbrewery.github.io/Zillow-Clone/)
  - [x] 1. Create a list of links for all the listings you scraped
  - [x] 2. Create a list of prices for all the listings you scraped
    - [x] 1. Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. The price should look like "$1,234" instead of "$1,234+ /mo"
  - [x] 3. Create a list of addresses for all the listings you scraped
    - [x] 1. Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.
- [x] 3. Write the selenium_form_writer.py to fill in the [Google Form](https://docs.google.com/forms/d/e/1FAIpQLScqa1QPYcn1F-iU5rsIBFNDL8rZses1bsNCXTtlIKCA-7Dc3A/viewform?usp=publish-editor) with the lists of data from the soup_scraper.py
- [x] 4. Write main.py to call the soup_scraper.py and selenium_form_writer.py
- [x] 5. Implement and Test


## Reflection
| DATE | NOTES |
| --- | --- |
| 27-jan-2026 | The gymnastics we've been doing to make these sites "scrape-able" (Gym assignment, Tinder assignment, this assignment) leads me to believe Selenium and BeautifulSoup are very brittle with modern websites. [Gemini agrees](https://gemini.google.com/share/6f9ca098f7d1).
| 27-jan-2026 | One thing i'm trying in this project is to see how nested dev workflow helps/hurts Gemini's ability to understand and work through the problem. seemed to work well! |


## References
  * [Zillow pre-loaded Customer_A search parameters](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D)
  * [Zillow "clone site" on app brewery (pre-loaded with Customer_A search parameters)](https://appbrewery.github.io/Zillow-Clone/)
  * [Selenium Read The Docs User Documentation](https://selenium-python.readthedocs.io/)
 