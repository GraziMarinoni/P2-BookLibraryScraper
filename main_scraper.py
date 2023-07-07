from category_scraper import process_pages
from book_scraper import scan_page

homeURL = "http://books.toscrape.com/catalogue/category/books_1/index.html"

home_page = scan_page(homeURL)
# scans all the source page for categories and returns the div with certain class
url_list = home_page.find("div", class_="side_categories").find_all("a")


# loop to run through all categories <a> tags and returns them as url
for category in range(1, len(url_list)):
    category_address = url_list[category]["href"]
    category_url = category_address.replace("../", "http://books.toscrape.com/catalogue/category/")
    process_pages(category_url)
