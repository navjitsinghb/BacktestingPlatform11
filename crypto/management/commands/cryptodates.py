from django.core.management.base import BaseCommand, CommandError
import requests
from crypto.models import Coin, CoinPrice
class Command(BaseCommand):
    dateDict = {



    }
    def handle(self,*args,**options):
        coins = Coin.objects.all()
        # print(coins)
        # for coin in coins:
        # print(coin.name)
        c = Coin.objects.filter(id=1)
        for x in c:
            name = x
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-12-2017'
        data = requests.get(url).json()
        print(data['market_data']['current_price']['usd'])
        pricedata = data['market_data']['current_price']['usd']
        CoinPrice.objects.create(
           name = name,
    price = pricedata,
    day = 30,
    month = 12,
    year = 2017 )

        