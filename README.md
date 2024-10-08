# Amazon Product Scraper
This repository contains a simple web scraping project that extracts product details from Amazon using Selenium for crawling and BeautifulSoup for data extraction. The project allows scraping product information such as product name, ratings, sale price, and actual price, and stores the data in a CSV file.

# Project Structure

├── data/                     # Folder where scraped HTML files are stored
├── bronze_extraction.py      # Script to scrape product details from HTML files
├── bronze_loader.py          # Script to load scraped product details into a CSV
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies for the project


Here’s a sample README.md file you can add to your GitHub repository. It explains the purpose of your project, the functionality of each script, and instructions on how to set it up.

Amazon Product Scraper
This repository contains a simple web scraping project that extracts product details from Amazon using Selenium for crawling and BeautifulSoup for data extraction. The project allows scraping product information such as product name, ratings, sale price, and actual price, and stores the data in a CSV file.

Project Structure
plaintext
Copy code
├── data/                    # Folder where scraped HTML files are stored
├── bronze_extraction.py      # Script to scrape product details from HTML files
├── bronze_loader.py          # Script to load scraped product details into a CSV
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies for the project

# How it Works

The project is divided into three main parts:

1. Bronze Loading Script (bronze_loader.py):

This script uses Selenium to crawl Amazon product pages and save the HTML content of each product to the data folder. It creates multiple HTML files, each containing information about a product.

Key Functions:

-> Uses the Selenium web driver to browse Amazon product listings.
-> Fetches product details based on a search query and stores the HTML data in the data folder.
-> Crawler runs for a specified number of pages (in this case, 20).

2. Scraping & Extraction Script (bronze_extraction.py):

This script parses the HTML files stored in the data folder using BeautifulSoup and extracts product details such as the product name, rating, sale price, and actual price. These details are then stored in a structured dictionary.

Key Functions:

-> Reads HTML files from the data folder.
-> Extracts product details using BeautifulSoup.
-> Cleans and structures the data for easy loading.

3. Loader Function (csv_loader.py):

Once the product details are extracted, this script loads the data into a CSV file for further analysis.

Key Functions:

-> Receives structured product data from the scraping script.
-> Writes the data to a CSV file for further analysis or usage.

# Installation and Setup

1. Create and activate a virtual environment:
python -m venv myvenv

On windows
.\myvenv\Scripts\Activate

2. Install the required dependencies:
pip install -r requirements.txt

3.  Run the crawler:
You can modify the query in the bronze_loader.py script to search for any product (e.g., "laptop", "smartphone"). After that, run the crawler to start scraping Amazon.

This will save the HTML files for the specified products into the data folder.

4. Run the extraction:
After scraping, you can run the scrapper function from the bronze_extraction.py file to extract data and store it in a CSV.

his will generate a CSV file with product details.

# Dependencies

Selenium (for web scraping)
BeautifulSoup (for HTML parsing)
pandas (for data manipulation)

# Usage and Customization

1. Search Query:
You can change the search query (query="laptop") in the bronze_loader.py file to scrape details for different products.

2. Number of Pages:
You can adjust the number of pages to scrape by modifying the range(1, 20) loop in the crawler script.


# Quick tip
The code will start scrapping the URL as soon as you start (bronze_loading.py) file other functions will be dynamically called.