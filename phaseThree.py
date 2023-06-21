from phaseOne import scan_page
from phaseTwo import process_pages



homeURL = "http://books.toscrape.com/catalogue/category/books_1/index.html"

home_page = scan_page(homeURL)
URL_list = home_page.find("div", class_="side_categories").find_all("a")


for category in range(1, len(URL_list)):
    category_address = URL_list[category]["href"]
    category_url = category_address.replace("../", "http://books.toscrape.com/catalogue/category/")
    process_pages(category_url)


