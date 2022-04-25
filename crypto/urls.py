from django.urls import path

from . import views
urlpatterns = [
    path('', views.crypto, name='cryptos'),
    path('<int:id>',views.cryptodetail,name='cryptodetail')
]