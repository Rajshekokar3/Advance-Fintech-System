import nselib
from nselib import capital_market
import requests
from bs4 import BeautifulSoup
import time


class data_scaper:
    def price_scrape(self):
        for i in range(3):
            ticker='RELIANCE'
            nse_url=f'https://www.google.com/finance/quote/{ticker}:NSE'
            response=requests.get(nse_url)

            soup=BeautifulSoup(response.text,'html.parser')
            # Price real time 
            class1='YMlKec fxKbKc'
            price=float(soup.find(class_=class1).text.strip()[1:].replace(",",''))
            time.sleep(1)
            print(price)

    def new_collection(self):
        pass


#object creation 
ds=data_scaper()
ds.price_scrape()