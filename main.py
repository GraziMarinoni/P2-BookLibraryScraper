import requests
from bs4 import BeautifulSoup
page = requests.get("http://books.toscrape.com/catalogue/under-the-tuscan-sun_504")

headings = ["product_page_url", "universal_product_code (upc)", "book_title", "price_incl_tax", "price_excl_tax", "qnt_available", "product_description", "category", "review_rating", "image_url"]
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

book_title = soup.find("li", class_="active").get_text()
UPC = soup.find("th", string="UPC").next_sibling.get_text()
price_excl = soup.find("th", string="Price (excl. tax)").next_sibling.get_text()
price_incl = soup.find("th", string="Price (incl. tax)").next_sibling.get_text()
qnt_available = soup.find("p", class_="instock availability").get_text().replace("In stock (", "").replace("available)", "")
img_url = soup.find("img", attrs={"alt": book_title})["src"].replace("../../media", "http://books.toscrape.com/media")
product_description = soup.find("div", attrs={"id": "product_description", "class": "sub-header"}).find_next_sibling("p").get_text()
category = soup.find("ul", class_="breadcrumb").find_all("a", limit=3)[-1].get_text()
review_rating = soup.find("p", class_="instock availability").find_next_sibling("p")["class"][-1]

product_page_url = page.url
print(product_page_url)


# soup.find("div", class_="col-sm-6 product_main")
