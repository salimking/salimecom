
from django.urls import path
from . import views
app_name='home'

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.logins,name='login'),
    path('profile',views.profile,name='profile'),

    path('logout',views.logouts,name='logout'),

    path('customer',views.customer,name='customer'),


]
