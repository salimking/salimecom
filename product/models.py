from django.db import models
from django.db.models.fields import DateTimeField

from home.models import MainUser

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)
    time=DateTimeField(auto_now_add=True)


    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='product_creator')
    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product/', default='images/default.png')
   
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.name
    class Meta:
        ordering=['-created']