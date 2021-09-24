from django import conf
from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    product=Product.objects.all()
    con={
        'p':product
    }
    return render(request,'shop.html',con)
def category(request):
    return render(request,'category.html')    