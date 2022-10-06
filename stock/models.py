from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Category(models.Model):
    name = models.CharField(max_length=25)


class Brand(models.Model):
    name = models.CharField(max_length=50)

class Product(UpdateCreate):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)