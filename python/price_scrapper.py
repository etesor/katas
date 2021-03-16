# Go to your amazon product page, find it's price and notify if has dropped below certain threshold.

import requests
from bs4 import BeautifulSoup


def price_scrapper(URL, targetPrice):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Accept-Language': 'en-US'
        }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().replace(',','')
    converted_price = float(price.replace('$', ''))

    if converted_price < targetPrice:
        print(f"Price for {title} is at ${str(converted_price)}, go get it!")
        # TODO: As a user I want to get notified when mi product price drops below my target price
    else:
        print(f"Price for {title} is too high :(")

