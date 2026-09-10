import requests
from bs4 import BeautifulSoup
import csv
import time

all_books = []

for page in range(1, 51):  # страницы с 1 по 50
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").get_text()
        availability = book.find("p", class_="instock").get_text(strip=True)
        all_books.append({"title": title, "price": price, "availability": availability})

    print(f"Страница {page}: собрано {len(books)} книг (всего: {len(all_books)})")
    time.sleep(0.3)  # маленькая пауза, чтобы не заваливать сайт запросами

# Сохраняем всё в CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"\nГотово! Сохранено {len(all_books)} книг в books.csv")