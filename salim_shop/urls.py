
from django.contrib import admin
from django.urls import path,include
# from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('cart/',include('carts.urls')),
    path('product/',include('product.urls')),


    

]
