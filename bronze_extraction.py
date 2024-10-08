import os
from bs4 import BeautifulSoup
from csv_loader import load_to_csv

def scrapper():
    """
    Extracts product details from html files stored in the 'data' folder and
    writes them to a csv file. The details extracted are product name, ratings,
    sale price and actual price.

    Args:
        None

    Returns:
        A string indicating the status of csv creation.
    """
    pd_data={'product_name':[],'ratings':[],'sale_price':[],'actual_price':[]}
    for files in os.listdir("data"):
        
        with open(f"data/{files}",encoding='utf-8') as f:
            html_doc=f.read()
        soup=BeautifulSoup(html_doc,'html.parser')
        product_name=soup.find('h2')
        ratings=soup.find('span',class_="a-icon-alt")
        sale_price=soup.find('span',class_="a-price-whole")
        actual_price=soup.find('span',class_="a-price a-text-price")

        name = product_name.text.split(',')[0] if product_name else None
        ratings = ratings.text.split(" ")[0] if ratings else None
        sale_price = sale_price.text.strip() if sale_price else None
        actual_price = actual_price.text.split('₹')[1].strip().split('₹')[0].strip() if actual_price and '₹' in actual_price.text else None
        pd_data['product_name'].append(name)
        pd_data['ratings'].append(ratings)
        pd_data['sale_price'].append(sale_price)
        pd_data['actual_price'].append(actual_price)

    load_data=load_to_csv(pd_data)
    print(load_data)