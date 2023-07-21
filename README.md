# Project2-BookLibraryScraper

This is a learning project to scrape a book library (books.toscrape.com) through a Python script. The application is intended to collect and store the data and images of each book as ‘csv’ and ‘jpg’ files in a directory created for this purpose.

The project is divided into three files:

1 - main_scraper.py - Scrapes all categories found in the library from the homepage and returns them as URLs. 
2 - category_scraper.py - Goes one step down and scrapes the collection of books inside a specific category, considering pagination (when books are displayed on multiple pages). 
3 - book_scraper.py - At this final stage, it scrapes the book specifications (like title, description, rating, price, …) of each copy available in the library.

The Python version used to write this script is Python 3.11.3

# Installation

Step 1: Ensure you have Python installed on your computer. 
Step 2: Ensure you have Git installed on your computer. 
Step 3: Clone the repository:
To test this application, execute the following command on your local machine:

git clone https://github.com/GraziMarinoni/P2-BookLibraryScraper.git

Step 4: Create a virtual environment. Open the Terminal or Command Prompt and navigate to the directory where you want to create the new environment. 
Then run the following command:

cd P2-BookLibraryScraper
python3 -m venv venv

Step 5: Activate the virtual environment. Run the command according to your operational system:

source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate.bat     # For Windows

Step 6: Install the dependencies: (libraries are included in the requirements.txt file)

pip install -r requirements.txt

# Running the app

Navigate to the application's directory from the Terminal.  
To open the file and run the code, type the command:

python main_scraper.py

All the following stages of the script will be run automatically.


