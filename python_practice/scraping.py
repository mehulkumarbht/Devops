import requests
from bs4 import BeautifulSoup
from loguru import logger

# url = "https://quotes.toscrape.com"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

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
# authors = soup.find_all("small", class_="author")
# unique_authors = []
# for a in authors:
#     name = a.get_text()
#     if name not in unique_authors:
#         unique_authors.append(name)
# logger.info(f"{unique_authors}")

# scrape quotes from all the pages:

# base_url = "https://quotes.toscrape.com"

# url = base_url
# all_quotes = []

# while True:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # get quotes from this page
#     quotes = soup.find_all("div", class_="quote")
#     for q in quotes:
#         text = q.find("span", class_="text").get_text()
#         author = q.find("small", class_="author").get_text()
#         tags = [t.get_text() for t in q.find_all("a", class_="tag")]
#         all_quotes.append({"text": text, "author": author, "tags": tags})

#     # fina next page
#     next_btn = soup.find("li", class_="next")
#     if next_btn is None:
#         break

#     next_url = next_btn.find("a")["href"]
#     url = base_url + next_url

# logger.info(f"Total quotes scraped: {len(all_quotes)}")
