import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


all_books = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException:
            print(f"attempt {attempt + 1} failed, try again after 3 sec")
            time.sleep(3)

    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("article", class_="product_pod")
    for res in result:
        title = res.find("h3").find("a")["title"]
        price = res.find("p", class_="price_color").get_text()
        availability = res.find("p", class_="instock").get_text(strip=True)
        all_books.append({"title": title, "price": price, "availability": availability})

with open("books_v2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
    writer.writeheader()
    writer.writerows(all_books)

