# Generated by Django 4.0.3 on 2022-05-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_stock_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='mostRecentPrice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
