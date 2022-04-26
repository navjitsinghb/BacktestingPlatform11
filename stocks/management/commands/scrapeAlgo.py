from django.core.management.base import BaseCommand, CommandError
import requests
import pandas as pd  
import numpy as np  
import yfinance as yf  
import datetime as dt 
from pandas_datareader import data as pdr 
from stocks.models import Stock, StockPrice

stockList = [
{
    "companyName": "Tesla",
    "ticker": "TSLA"
},
{
    "companyName": "Microsoft",
    "ticker": "MSFT"
}
]

class Command(BaseCommand):
    def handle(self,*args,**options):
        Stock.objects.all().delete()
        print("scrape stocks ")
        for stock in stockList:
            startyear = 2019
            startmonth = 1
            startday = 1
            start = dt.datetime(startyear, startmonth, startday)
            now = dt.datetime.now()
            df = pdr.get_data_yahoo(stock['ticker'], start, now)
            stockInstance = Stock.objects.create(
                companyName=stock['companyName'],
                ticker=stock['ticker']
            )
            stockInstance.save()
            for row in df.index:
                high = df["High"][row]
                low = df["Low"][row]
                open = df["Open"][row]
                close = df["Close"][row]
                volume = df["Volume"][row]
                adjclose = df["Adj Close"][row]
                date = str(row)
                year = date[0:4]
                month = date[5:7]
                day = date[8:10]
                print("high: ",high," low: ",low," open: ",open," close: ",close," volume: ",volume
                ," adjClose: ",adjclose, " year: ",year," month: ",month," day: ",day)
                StockPrice.objects.create(
                    stock=stockInstance,
                    open=open,
                    high=high,
                    low=low,
                    close=close,
                    adjclose=adjclose,
                    day=day,
                    month=month,
                    year=year
                )
            
