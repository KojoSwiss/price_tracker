import requests
from bs4 import BeautifulSoup
import lxml

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
print(price_split)

