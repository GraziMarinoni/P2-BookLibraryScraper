import requests
import csv
import pathlib
from phaseThree import scan_page

# folder path where the data and images will be stored
images_path = pathlib.Path('/Users/grazimarinoni/Desktop/OpenClassroom/Projects/Project-2/images')
data_path = pathlib.Path('/Users/grazimarinoni/Desktop/OpenClassroom/Projects/Project-2/data')


# pulls book details
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

    # stores the values in the csvfile created on phaseTwo
    csv_path = (data_path/f"{category_name}").with_suffix('.csv')
    with csv_path.open(mode='a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header_values)

    # stores the books images as jpg
    image_name = str(book_title).replace("/"," ")
    img_data = requests.get(image_url).content
    img_path = (images_path/f"{image_name}").with_suffix('.jpg')
    with img_path.open(mode='wb') as image:
        image.write(img_data)
    return

