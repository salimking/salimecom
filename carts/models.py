from django.db import models
from home.models import MainUser
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(MainUser,on_delete=models.CASCADE)
    item = models.ManyToManyField(Product, blank=True)

    quantity = models.PositiveIntegerField(default=1)
    parchased=models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.item}x{self.quantity}'
    def get_total(self):
        total=self.item.price *self.quantity  
        f_total=format(total,'0.2f')
        return f_total

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart, null=True)
    user=models.ForeignKey(MainUser,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=300,blank=True,null=True)
    orderid=models.CharField(max_length=300,blank=True,null=True)
    def get_total(self):
        total=0
        for order in self.orderitems.all():
            total=float(self.order.get_total())
        return total    