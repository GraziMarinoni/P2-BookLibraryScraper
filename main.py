import requests
from bs4 import BeautifulSoup, Comment

# webpage to be scraped
page = requests.get("http://books.toscrape.com/catalogue/under-the-tuscan-sun_504")

# relevant data to be scraped
headings = ["product_page_url", "universal_product_code (upc)", "book_title", "price_incl_tax", "price_excl_tax", "qnt_available", "product_description", "category", "review_rating", "image_url"]
# pulling the HTML content of the current page
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())


book_title = soup.find("li", class_="active").get_text()
UPC = soup.find("th", string="UPC").next_sibling.get_text()
# UPC = short for * universal product code *
price_excl_tax = soup.find("th", string="Price (excl. tax)").next_sibling.get_text()
# price excluding taxes
price_incl_tax = soup.find("th", string="Price (incl. tax)").next_sibling.get_text()
# price including taxes
qnt_available = soup.find("p", class_="instock availability").get_text().replace("In stock (", "").replace("available)", "")
# quantity available
image_url = soup.find("img", attrs={"alt": book_title})["src"].replace("../../media", "http://books.toscrape.com/media")
product_description = soup.find("div", attrs={"id": "product_description", "class": "sub-header"}).find_next_sibling("p").get_text()
category = soup.find("ul", class_="breadcrumb").find_all("a", limit=3)[-1].get_text()
review_rating = soup.find("p", class_="instock availability").find_next_sibling("p")["class"][-1]
# star rating review method
product_page_url = soup.findAll(string=lambda string: isinstance(string, Comment))[9].replace('\n', '').replace(" ", "").replace('<aid="write_review"href="/', '').replace('/reviews/add/#addreview"class="btnbtn-successbtn-sm">Writeareview</a>', '').replace('catalogue/', 'https://books.toscrape.com/catalogue/')

header_values = [product_page_url, UPC, book_title, price_incl_tax, price_excl_tax, qnt_available, product_description, category, review_rating, image_url]

print(header_values)
