# Language Flash Cards - Rudi Lewis
Day 31 Project in the 100 days of Python! 
## Project Description
Build a deck of flash cards that helps the English speaker learn the top ~~100~~ 1000 words in ~~French~~ Brazilian Portuguese.

## Deliverables
### MVP: 
- [x] build a working flash card UI in TKinter that:
  - [x] uses TKInter and the assets in ./assets to build the overall UI (card_front.png, card_back.png, right.png, wrong.png)
  - [x] uses Pandas to read a two-column csv (default bra_pt_words.csv) to create front and back of cards
  - [x] lets the user see the front of a random card, then after a (default 3 second) delay, the back of the card
  - [x] lets the user self-check whether they got it "right" or "wrong" with a red x (./assets/wrong.png) or green checkmark (./assets/right.png)
  - [x] keeps a list of "known" words (or actually the inverse, unknown words) so that the user is shown only unknown and never tried words each time they run the program.
- [x] utilize object oriented programming wherever possible (classes and methods in separate external files, use class inheritance, keep main.py very tight and readable for flow.)
- [x] employ great documentation in any and all *.py files, written so other developers and casuals can easily understand your code blocks and flow

### stretch goals: 
- [x] switch the input file from French to Brazilian Portuguese and upping the word count to 1000
  - [ ] let the user choose between available language files at startup
- [ ] also keep a list of "known words" and instead of totally hiding them, just decrease their frequency over time by diluting their randomness every time they are shown and guessed correctly

### super stretch goals:
- [ ] stats on percentage correct: overall, by language (if language selector implemented), and for each word

## Mockup

<img src="docs/flash_card_layout.webp" width="700">

## To Run
  1. For now, clone to local deployment only. 
     - Requires:
       - TKinter GUI package (usually included in your standard Python install).
       - Pandas data analysis toolkit available on pypi.org
  2. I built it in Python 3.14.2, but I think it should work in any 3.x based on the standard libraries and code used.

## Development Workflow
- [x] 1. Create the UI with TKinter based on the mockup in ./docs/flash_card_layout.webp
- [x] 2. Create new flash cards from reading the csv data in ./data/bra_pt_words.csv with Pandas
- [x] 3. Create the "Flip the card" sequence
- [x] 4. Create a words_to_learn.csv that stays updated with all words EXCEPT those that have been "green checked" when they were shown to the user
- [x] 5. Create a check (preferrably using a try/except/else/finally block) for words_to_learn.csv on startup. if it exists, use it to make the cards. If not, use the original csv.
- [x] 6. Create an elegant way for user to exit the program at any time.
- [x] 7. DEPLOY and TEST (locally) 

## Reflection
| DATE        | NOTES                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 18-jan-2026 | tested and working as specified, will leave the stretch goals as possibilities for improvement for possible portfolio project                                   |
| 17-jan-2026 | looking to make this README robust enough so that I simply orchestrate and review code, (that's the skill i'm trying to become first class at, not programming) |

## References
  * [Wiktionary: Language Frequency Lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)
  * [hermitdave's github repo of Frequency words](https://github.com/hermitdave/FrequencyWords)
  * [GOOGLETRANSLATE function in Google Sheets](https://support.google.com/docs/answer/3093331?hl=en-GB)