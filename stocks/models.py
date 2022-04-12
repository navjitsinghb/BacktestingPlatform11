from django.db import models

# Create your models here.
class Stock(models.Model):
    companyName = models.CharField(max_length=100, null=True, blank=True)
    ticker = models.CharField(max_length=10, null=True, blank=True)
    open = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.companyName
