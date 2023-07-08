# Project2-BookLibraryScraper

This is a learning project to scrape a book library (books.toscrape.com) through a Python script. The application is intended to collect and store the data and images of each book as ‘csv’ and ‘jpg’ files in a directory created for this purpose.

The project is divided into three files:

1 - main_scraper.py - Scrapes all categories found in the library from the homepage and returns them as URLs. 
2 - category_scraper.py - Goes one step down and scrapes the collection of books inside a specific category, considering pagination (when books are displayed on multiple pages). 
3 - book_scraper.py - At this final stage, it scrapes the book specifications (like title, description, rating, price, …) of each copy available in the library.

The Python version used to write this script is Python 3.11.3

# Installation

1. Clone the repository:

To test this application, execute the following command on your local machine:

```shell
git clone https://github.com/GraziMarinoni/P2-BookLibraryScraper.git


2. Create and activate a virtual environment:

cd Project2-BookLibraryScraper
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate.bat     # For Windows


3. Install the dependencies: (libraries are included in the requirements.txt file)
pip install -r requirements.txt

Open the ‘main_scraper.py’ file and run the code from there. All the following phases
will be run automatically.

