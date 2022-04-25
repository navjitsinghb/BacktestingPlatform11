from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=True)
    rank = models.IntegerField(default=0, blank=True)
    image = models.URLField(blank=True,null=True) 

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['rank']

class CoinPrice(models.Model):
    name = models.ForeignKey(Coin, related_name='coin_name',on_delete=models.CASCADE)
    price = models.FloatField(default=0, blank=True)
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)