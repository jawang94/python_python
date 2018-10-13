from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    order_total = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_total', 'description']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_price']



