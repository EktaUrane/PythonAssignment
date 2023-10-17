from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome()
pge_num = 1
url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{pge_num}"

driver.get(url)

product_url = driver.find_elements(by=By.CSS_SELECTOR,  value='a.a-link-normal.a-text-normal')
product_name = driver.find_elements(by=By.CSS_SELECTOR,  value='span.a-size-medium')
product_price = driver.find_elements(by=By.CSS_SELECTOR,  value='span.a-price')

data = []

# for price in product_price:
#     print(price.text)


for title, url, price in zip(product_name, product_url, product_price):
    data.append({"Product URL": url.get_attribute("href"), "Product Name": title.text, "Product Price": price.text })

csv_file = "amazon_products.csv"

with open(csv_file, "w", newline="", encoding='utf-8') as file:
    field_names = ["Product URL", "Product Name", "Product Price"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

driver.quit()   