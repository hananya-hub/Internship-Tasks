import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        rating = book.select_one(".star-rating")["class"][1]

        writer.writerow([title, price, rating])

print("Data saved to data.csv")
