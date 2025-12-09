import requests
from bs4 import BeautifulSoup
from loguru import logger

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# quotes = soup.find_all("span", class_="text")

# for q in quotes:
#     logger.info(f"{q.get_text()}")

# authors = soup.find_all("small", class_="author")
# for a in authors:
#     logger.info(f"{a.get_text()}")

# quotes = soup.find_all("div", class_="quote")
# for q in quotes:
#     text = q.find("span", class_="text").get_text()

#     tag_elements = q.find("div", class_="tags").find_all("a", class_="tag")
# tags = [t.get_text() for t in tag_elements]
# tags = []
# for t in tag_elements:
#     tags_content = t.get_text()
#     tags.append(tags_content)
# tags = [t.get_text() for t in tag_elements]
# logger.info(f"{text}")
# logger.info(f"Tags:{tags}")

# 2: count total number of quotes:
# quotes = soup.find_all("div", class_="quote")
# logger.info(f"Total quoted on the page: {len(quotes)}")

# 3: Extract all unique authors
authors = soup.find_all("small", class_="author")
unique_authors = []
for a in authors:
    name = a.get_text()
    if name not in unique_authors:
        unique_authors.append(name)
logger.info(f"{unique_authors}")
