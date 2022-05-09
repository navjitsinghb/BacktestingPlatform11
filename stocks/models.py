from django.db import models

# Create your models here.
class Stock(models.Model):
    companyName = models.CharField(max_length=100, null=True, blank=True)
    ticker = models.CharField(max_length=10, null=True, blank=True)
    lastScrape = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    logo = models.TextField(max_length=200, null=True, blank=True)
    mostRecentPrice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.companyName
class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, null=True, blank=True, on_delete=models.CASCADE)
    open = models.FloatField(null=True, blank=True)
    high = models.FloatField(null=True, blank=True)
    low = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)
    adjclose = models.FloatField(null=True, blank=True)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)


