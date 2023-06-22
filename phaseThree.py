import requests
from bs4 import BeautifulSoup
from phaseTwo import process_pages

homeURL = "http://books.toscrape.com/catalogue/category/books_1/index.html"


# scans current page and returns it
def scan_page(url):
    raw_page = requests.get(url)
    page = BeautifulSoup(raw_page.content, "html.parser")
    return page


home_page = scan_page(homeURL)
# scans all the source page for categories and returns the div with certain class
url_list = home_page.find("div", class_="side_categories").find_all("a")


# loop to run through all categories <a> tags and returns them as url
for category in range(1, len(url_list)):
    category_address = url_list[category]["href"]
    category_url = category_address.replace("../", "http://books.toscrape.com/catalogue/category/")
    process_pages(category_url)

