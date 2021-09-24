
from django.urls import path
from . import views
app_name='product'
urlpatterns = [
   
    path('product',views.product,name='product'),
    path('category',views.category,name='category'),


]
