from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_csv("amazon_products.csv")

driver = webdriver.Chrome()
data = []


def fetch_product_detail(url):
    driver.get(url)
    description = driver.find_element(
        By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]').text
    asin = driver.find_element(
        By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[6]/span/span[2]').text
    product_description = driver.find_element(
        By.XPATH, '//*[@id="productDescription"]').text
    manufacturer = driver.find_element(
        By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[10]/span/span[2]').text

    for descr, asin_number, pr_descr, manufc in zip(description, asin, product_description, manufacturer):
        data.append({descr, asin_number, pr_descr, manufc})

    return data


csv_file = "product_details.csv"

product_urls = df["Product URL"]
result_df = pd.DataFrame(columns=['Description', 'ASIN Number', 'Product Description', 'Manufacturer'])

for product_url in product_urls:
    data = fetch_product_detail(product_url)
    result_df = result_df._append(data, ignore_index=True)

result_df.to_csv(csv_file, index=False)