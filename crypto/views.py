from django.shortcuts import render
from .models import Coin

# Create your views here.
def crypto(request):
    coins = Coin.objects.all()
    context = {"coins":coins}
    return render(request,'crypto.html',context)

def cryptodetail(request, id):
    coin = Coin.objects.filter(id=id)
    print(coin)
    context = {'coin': coin}
    return render(request, 'cryptodetail.html', context)