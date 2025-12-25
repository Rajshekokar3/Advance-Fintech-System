import nselib
from nselib import capital_market
import requests
from bs4 import BeautifulSoup
import time


class data_scaper:
    def price_scrape(self,ticker):
        while True:
        #for i in range(3)
            nse_url=f'https://www.google.com/finance/quote/{ticker}:NSE'
            response=requests.get(nse_url)

            soup=BeautifulSoup(response.text,'html.parser')
            # Price real time 
            class1='YMlKec fxKbKc'
            price=float(soup.find(class_=class1).text.strip()[1:].replace(",",''))
            time.sleep(1)
            return price

    def new_collection(self,ticker):
        url = "https://gnews.io/api/v4/search"
        params = {
            "q": f"{ticker} latest news",
            "lang": "en",
            "country": "in",
            "max": 50,
            "apikey": "ea54132ae726450e8b7810641a5ac4e5"
        }
        res = requests.get(url, params=params)
        articles = res.json()["articles"]


#object creation 
ds=data_scaper()
ds.price_scrape('Reliance')
