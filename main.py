import requests
from bs4 import BeautifulSoup
import csv

# relevant data to be scraped
headings = ["product_page_url", "universal_product_code (upc)", "book_title", "price_incl_tax", "price_excl_tax", "qnt_available", "product_description", "category", "review_rating", "image_url"]
bookURL = "http://books.toscrape.com/catalogue/under-the-tuscan-sun_504"

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headings)

def details(url):
    # webpage to be scraped
    page = requests.get(url)
    # pulling the HTML content of the current page
    soup = BeautifulSoup(page.content, "html.parser")

    # print(soup.prettify())  >>>> This is a command

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
    product_page_url = page.url

    header_values = [product_page_url, UPC, book_title, price_incl_tax, price_excl_tax, qnt_available, product_description, category, review_rating, image_url]
    # print(header_values)   >>>> This is a command

    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header_values)
    return

# calling the function for the first book URL
details(bookURL)
# end of phase one

# start of phase two
# scrapes the chosen category page
page_category = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
soup = BeautifulSoup(page_category.content, "html.parser")
# print(soup.prettify())

# To collect a list of the div tags that have the books URLs
url_list = soup.find_all("div", class_="image_container")


# To collect a list of the div tags that have the books URLs
for i in range(len(url_list)):
    url = url_list[i].find("a")["href"].replace("../../../","http://books.toscrape.com/catalogue/")
    details(url)
