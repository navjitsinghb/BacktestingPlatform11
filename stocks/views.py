from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Stock
import requests
# Create your views here.
def home(request):
    # r = requests.get('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=hbJiRLJtmp4m3obtdFF_gtWOY08wxhPx')
    # print('greger',r.content)
    stocks = Stock.objects.all()
    amount = stocks.count()
    context = {
        "stocks": stocks,
        "amount": amount
    }
    return render(request, 'index.html', context) 

def detail(request, id):
    detailStock = Stock.objects.filter(id=id)
    print(detailStock)
    context = {
    "stock" : detailStock,
    "amount": 1
     }
    return render(request, 'detailview.html',context) 