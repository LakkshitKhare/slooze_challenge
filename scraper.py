from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def init_driver():
    driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
    service = Service(driver_path)

    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Edge(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def scrape_amazon(query, max_pages=10):
    driver = init_driver()
    results = []
    page = 1

    while page <= max_pages:
        url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}&page={page}"
        print(f"🔍 Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        product_blocks = soup.select('div.s-main-slot div[data-component-type="s-search-result"]')

        if not product_blocks:
            print("⚠️ No products found. Stopping.")
            break

        print(f"✅ Found {len(product_blocks)} products")

        for block in product_blocks:
            title_tag = block.select_one('h2 span')
            price_tag = block.select_one('.a-price-whole')
            seller_tag = block.select_one('.a-row.a-size-base.a-color-secondary')

            name = title_tag.get_text(strip=True) if title_tag else "N/A"
            price = price_tag.get_text(strip=True) if price_tag else "N/A"
            seller = seller_tag.get_text(strip=True) if seller_tag else "N/A"

            results.append({
                'product_name': name,
                'price': price,
                'seller_info': seller,
                'category': query,
                'page': page
            })

        page += 1

    driver.quit()
    return results

def save_to_csv(data, filename='amazon_data.csv'):
    if not data:
        print("⚠️ No data scraped.")
        return
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"📁 Saved {len(data)} records to {filename}")

if __name__ == "__main__":
    category = "industrial machinery"
    scraped_data = scrape_amazon(category, max_pages=10)  # You can increase this limit
    save_to_csv(scraped_data)
