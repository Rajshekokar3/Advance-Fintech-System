import os
import time
from matplotlib import ticker
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup


class DataScraper:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.news_url = "https://gnews.io/api/v4/search"
        self.api_key = "ea54132ae726450e8b7810641a5ac4e5"  # set this once

    def price_scraper(self, ticker: str) -> float:
        if ticker.upper() == "BTC":
            url = "https://www.google.com/finance/quote/BTC-USD"
        else:
            url = f"https://www.google.com/finance/quote/{ticker}:NSE"

        response = requests.get(url, headers=self.headers, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        price_text = soup.find(class_="YMlKec fxKbKc").text

        return float(price_text[1:].replace(",", ""))

    def news_collection(self, ticker: str) -> pd.DataFrame:
        params = {
            "q": f"{ticker} latest news",
            "lang": "en",
            "max": 10,   # FREE PLAN LIMIT
            "apikey": self.api_key
        }

        response = requests.get(self.news_url, params=params, timeout=5)
        response.raise_for_status()

        articles = response.json().get("articles", [])

        return pd.DataFrame(articles)

    def collect_price_and_news(self, ticker: str) -> pd.DataFrame:
        price = self.price_scraper(ticker)
        news_df = self.news_collection(ticker)

        if news_df.empty:
            return pd.DataFrame()

        final_df = pd.DataFrame({
            "ticker": ticker,
            "price": price,
            "title": news_df["title"],
            "content": news_df["content"],
            "source_url": news_df["url"],
            "fetched_at": datetime.utcnow()
        })

        return final_df


# ---------------- RUN PIPELINE ---------------- #

scraper = DataScraper()

df = scraper.collect_price_and_news("BTC")

os.makedirs("data/news", exist_ok=True)
df.to_parquet(f"data/news/{ticker}.parquet", index=False)

print(df.head())
