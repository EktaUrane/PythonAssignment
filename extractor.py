from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()
pge_num = 1

data = []
while pge_num <= 20:
    url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{pge_num}"
    driver.get(url)
    product_url = driver.find_elements(
        by=By.CSS_SELECTOR,  value='a.a-link-normal.a-text-normal')
    product_name = driver.find_elements(
        by=By.CSS_SELECTOR,  value='span.a-size-medium')
    product_price = driver.find_elements(
        by=By.CSS_SELECTOR,  value='span.a-price')
    product_ratings = driver.find_elements(
        by=By.XPATH,  value='.//div[@class="a-row a-size-small"]/span')

    product_rating = []
    product_reviews = []
    ratings = []
    for rating in product_ratings:
        product_rating.append(rating.get_attribute("aria-label"))

    for index in range(0, len(product_rating), 2):
        rating = product_rating[index]
        reviews = product_rating[index + 1]
        ratings.append(rating)
        product_reviews.append(reviews)

    for title, url, price, pr_rating, review in zip(product_name, product_url, product_price, ratings, product_reviews):
        data.append({"Product URL": url.get_attribute("href"), "Product Name": title.text,
                    "Product Price": price.text, "Product Rating": pr_rating, "Product Reviews": review})

    pge_num += 1

csv_file = "amazon_products.csv"

driver.quit()

# Saving the CSV File
df = pd.DataFrame(data=data)
df.to_csv(csv_file, index=False)
print("[INFO] CSV File created successfully.")