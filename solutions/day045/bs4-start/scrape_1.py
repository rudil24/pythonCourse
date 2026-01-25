from bs4 import BeautifulSoup
import requests

# The code below will not work for the live website because the HTML has changed.
# For scraping the live site see: https://gist.github.com/TheMuellenator/941a8d6bfc555dbc7c939d2c3720a87d
# response = requests.get("https://news.ycombinator.com/")

# This code will fetch data from the static practice website that I've created for you:
# response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")

# # Find all articles, identified by <a> tags with the class "storylink"
# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []

# # Iterate over each article tag found
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)

# # Find all <span> tags with the class "score" and extract the upvote count
# article_upvotes = [
#     int(score.getText().split()[0])
#     for score in soup.find_all(name="span", class_="score")
# ]

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# print(article_texts[largest_index])
# print(article_links[largest_index])

# This above code no longer works as ycombinator has restructured its homepage somewhat. For one, the a tags with the link/name of the articles no longer contain a class attribute, but they can be identified by the fact that they are contained within a tr tag with a class of "athing". More problematic is the fact that not every article will have a score associated with it. Therefore, it is no longer viable to have separate lists for the names, links and scores and associate the values by their index position in each of the lists. The below code instead creates one list, with a dict for each article inside it, and assigns a score of None to articles that do not have one.

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
articles = []

# Select all tr tags with class = athing (there should always be 30 of those, containing the name and link of the articles)
rows = soup.find_all("tr", class_="athing")

for row in rows:
    # Find the article title and link
    article_link_tag = row.select_one("span.titleline > a")
    article_name = article_link_tag.text
    article_link = article_link_tag["href"]

    # If a score exists, it will be inside a span with a class of score, which itself is contained in the next tr tag
    next_row = row.find_next_sibling("tr")
    score_tag = next_row.select_one("span.score")

    # If the score exists, extract it, otherwise set score to None
    score = score_tag.text.split()[0] if score_tag else None

    # Append the article information
    articles.append({"name": article_name, "link": article_link, "score": score})

# Sort the articles by their score, treating articles without a score as though their score was 0
sorted_articles = sorted(
    articles,
    key=lambda x: int(x["score"]) if x["score"] is not None else 0,
    reverse=True,
)

# Article with highest score will be at position 0 in the list
print(sorted_articles[0])
