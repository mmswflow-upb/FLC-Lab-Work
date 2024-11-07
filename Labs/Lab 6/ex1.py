import requests
from bs4 import BeautifulSoup
import re

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

main_title_row= soup.find("div", class_="col-sm-8 h1")
main_title = main_title_row.a.text.strip() + " " + main_title_row.small.text.strip()

print("Page Title:", main_title)

page_info = soup.select_one("li.current").text.strip()
print("Pagination Info:", page_info)

button_content = soup.find("button")
if button_content:
    print("Button Content:", button_content.text.strip())

products = soup.find_all("article", class_="product_pod")
for product in products:
    title = product.h3.a["title"]
    print("Title:", title)

    price = product.find("p", class_="price_color").text
    print("Price:", price)

categories = soup.find("ul", class_="nav nav-list").find("ul").find_all("li")
for category in categories:
    category_name = category.text.strip()
    category_name = re.sub(r'\s+', ' ', category_name)
    if category_name:
        print("Category:", category_name)

images = soup.find_all("img")
for img in images:
    alt_text = img.get("alt", "")
    if alt_text:
        print("Image Alt Text:", alt_text)
