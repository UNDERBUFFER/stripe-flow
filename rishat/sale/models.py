from django.db import models

class Item(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.IntegerField()
    api_price_id = models.TextField(null=True)