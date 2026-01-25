import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
data = response.text

soup = BeautifulSoup(data, "html.parser")

# All articles titles and links
articles = soup.select(".titleline")

# All points
points = soup.select(".score")

# Convert points [str] to [int] in a new list
int_points = [int(item.text.split()[0]) for item in points]

# Index of highest point
highest_point = int_points.index(max(int_points))

# Article|Upvote|Link
print(
    f"Article : ({highest_point}){articles[highest_point].text}\n"  # Article : (article number)Article text
    f"Upvotes: {int_points[highest_point]}\n"
    f"Link :{articles[highest_point].find('a')['href']}"
)
