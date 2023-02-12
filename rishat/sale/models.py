from django.db import models


class Item(models.Model):
    name = models.TextField(null=False, unique=True)
    description = models.TextField(null=False)
    price = models.IntegerField()
    api_price_id = models.TextField(default=None,blank=True, null=True, unique=True)


class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
