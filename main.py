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

# Calling the function for the first book URL
details(bookURL)
# End of phase 1

# Start of phase 2
# Scrapes the chosen category page
page_category = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
soup = BeautifulSoup(page_category.content, "html.parser")
# print(soup.prettify())

# To collect a list of the div tags that have the books URLs
url_list = soup.find_all("div", class_="image_container")


# To collect a list of the div tags that have the books URLs
for i in range(len(url_list)):
    url = url_list[i].find("a")["href"].replace("../../../","http://books.toscrape.com/catalogue/")
    details(url)

# End of phase 2 (PAGINATION still to be done)

# Start of phase 3
def scan_page():
    books_page = requests.get("http://books.toscrape.com/catalogue/category/books_1/index.html")
    formatted_html = BeautifulSoup(books_page.content, "html.parser")
    return formatted_html


def find_all_categories_links(html):
    categories = html.find("div", class_="side_categories")
    links = categories.find_all("a")
    del links[0]
    return links


def find_all_category_books(category):
    for book in category:
        print(book)

def phase_three():
    html = scan_page()
    categories = find_all_categories_links(html)
    for category in categories:
        find_all_category_books(category)


categories = find_all_categories_links()
for category in categories:
    book_address = category["href"]
    book_url = book_address.replace("../","http://books.toscrape.com/catalogue/category/")
    print(book_address)

# for i in range(len(meta_list)):
#     meta_url = meta_list[i].find("li").find("a")["href"].replace("../../../","http://books.toscrape.com/catalogue/")
#     details(meta_url)
