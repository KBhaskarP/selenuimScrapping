from selenium import webdriver
from selenium.webdriver.common.by import By
from bronze_extraction import scrapper

driver = webdriver.Chrome()
file_number=0
query="laptop"
for pages in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={pages}&crid=2TB9FB3OM4XK1&qid=1728295989&sprefix=laptop%2Caps%2C197&ref=sr_pg_3")
    elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"Crawler found {len(elem)} items" )
    for elems in elem:
        outer_html=elems.get_attribute("outerHTML")
        with open(f"data\{query}_{file_number}.html",'w',encoding="utf-8") as f:
            f.write(outer_html)
            file_number+=1
    pages+=1
driver.close()
scrapper()
