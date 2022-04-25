from django.contrib import admin
from .models import Coin, CoinPrice

admin.site.register(Coin)
admin.site.register(CoinPrice)