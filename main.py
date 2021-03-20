import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

URL = "https://www.amazon.de/-/en/Lamicall-Adjustable-Stand-Tablet-iPad/dp/B06XCD4PDF/ref=sr_1_3?crid=281ELNZCEGD30&dchild=1&keywords=ipad+halter+st%C3%A4nder&qid=1616236607&sprefix=ipad+holder%2Claunchpad%2C176&sr=8-3"

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
website_data = response.text

soup = BeautifulSoup(response.content, "lxml")

price_text = soup.find(name='span', class_='a-size-medium a-color-price priceBlockBuyingPriceString')
price = price_text.getText()
price_split = float(price.split("€")[1])

product_name = soup.find(name='span', id='productTitle', class_='a-size-large product-title-word-break').getText().strip()

best_price = 15

if price_split < best_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Time to Buy {product_name}\n\n This price low or equal to {price_split}")
else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Not Time to Buy {product_name}\n\n This price is {price_split}")




