# Cookie Clicker - Rudi Lewis
Day 48 Project in the 100 days of Python!
## Project Description
Use the Selenium package to scrape the Cookie Clicker game with these goals:
  * enable (fastest rate) automated clicks on the cookie itself
  * recognize (scrape) upgrade buttons, text, and tooltips, and click ability, on all the different upgrades that cookies can buy
  * buy the "most expensive" available upgrade every 5 seconds.
  * continue clicking and buying for a total of 5 minutes.
  * print out the cookies/second rate at the end of 5 minutes, and exit the program.

## Deliverables
### MVP: 
- [x] Successfully implement a python program to: 
  - [x] opens the site (game) in Selenium webdriver (aka "Test Software") mode
  - [x] completes the description above using Selenium methods for scrapes and clicks, and Python (and time package) for the timers & logic. 
- [x] Resulting in: **28 clicks/second top rate.**
### Stretch Goals:
- [x] Add improvements to upgrade recognition (v1 was not recognizing tech upgrades palette)
- [x] Add timing enhancements (we're buying too many "little" upgrades that have diminishing returns, need to save up cookies for "bigger" purchases.)
  - [x] devised a method to delay purchase interval by another 5 seconds every 30 seconds of game clock. So we buy something every 5 seconds from 0:00 to 0:30, every 10 seconds from 0:30 to 1:00, etc.
- [x] Resulting in: **86 clicks/second top rate, a 307% improvement.**
### Super Stretch Goals:
- [ ] Learn more about statistical analysis in Python, then come back and build an optimized brain for knowing what to buy when to maximize click rate over a 5 minute period.


## To Run
  1. For now, clone to local deployment only. 
     - Requires:
       - Selenium api package available on pypi.org
  2. I built it in Python 3.14.2, but I think it should work in any 3.x based on the standard libraries and code used.

## Development Workflow
- [x] 1. Cut & paste project requirements into top of main.py
- [x] 2. Tell Gemini 3.0 to get after it
- [x] 3. Work with Gemini to [manage bug fixes and improvements](./gemini_cookie_bot_convo.md)
- [x] 4. Implement and Test


## Reflection
| DATE | NOTES |
| --- | --- |
| 24-jan-2026 | this is WAAAY cooler problem than I thought, b/c MVP is just the start of "clicks/second optimization". i thought of some and made a v2.
| 24-jan-2026 | Very good implementation by Gemini Code Assist, worked through all the timers and Selenium commands with me.

## References
  * [Cookie Clicker Game (new version)](https://ozh.github.io/cookieclicker/)
  * [Selenium Documentation](https://www.selenium.dev/documentation/)
