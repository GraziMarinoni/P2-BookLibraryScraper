import requests
from bs4 import BeautifulSoup
import csv
import pathlib
images_path = pathlib.Path('/Users/grazimarinoni/Desktop/OpenClassroom/Projects/Project-2/images')
data_path = pathlib.Path('/Users/grazimarinoni/Desktop/OpenClassroom/Projects/Project-2/data')
def scan_page(url):
    raw_page = requests.get(url)
    page = BeautifulSoup(raw_page.content, "html.parser")
    return page
# print(page.prettify()) >>>> This is a command


def details(url):
    page = scan_page(url)

    category_name = page.find("ul", class_="breadcrumb").find_all("a", limit=3)[2].get_text()
    book_title = page.find("li", class_="active").get_text()
    product_page_url = url
    upc = page.find("th", string="UPC").next_sibling.get_text()
    price_incl_tax = page.find("th", string="Price (incl. tax)").next_sibling.get_text()
    price_excl_tax = page.find("th", string="Price (excl. tax)").next_sibling.get_text()
    qnt_available = page.find("p", class_="instock availability").get_text().replace("In stock (", "").replace("available)","")
    if page.find("h2", string="Product Description"):
        product_description = page.find("h2", string="Product Description").find_next().get_text()
    else:
        product_description = "No Product Description"
    review_rating = page.find("p", class_="instock availability").find_next_sibling("p")["class"][1]
    image_url = page.find("div", class_="item active").find("img")["src"].replace("../../","http://books.toscrape.com/")

    header_values = [category_name, book_title, product_page_url, upc, price_incl_tax, price_excl_tax, qnt_available,
                     product_description, review_rating, image_url]
    # print(header_values)   >>>> This is a command


    csv_path = (data_path/ f"{category_name}").with_suffix('.csv')
    with csv_path.open(mode='a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header_values)

    img_data = requests.get(image_url).content
    print(img_data)
    img_path = (images_path/f"{book_title}").with_suffix('.jpg')
    with img_path.open(mode='wb') as image:
        image.write(img_data)
    return

