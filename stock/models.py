
from random import choices
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(UpdateCreate):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='b_products' )
    stock = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Firm(UpdateCreate):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Transaction(UpdateCreate):
    TRANSACTION = (
        ('I','IN'),
        ('O', 'OUT')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name='transactions')
    transaction = models.SmallIntegerField(choices=TRANSACTION)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='transactions' )
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digit=6, decimal_places=2)
    price_total = models.DecimalField(max_digit=9, decimal_places=2)

    def __str__(self):
        return f'{self.transaction} - {self.product} - {self.quantity}'