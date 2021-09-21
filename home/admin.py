from django.contrib import admin
from .models import Customer,MainUser,Seller
# Register your models here.
admin.site.register(MainUser)
admin.site.register(Customer)
