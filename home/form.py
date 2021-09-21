from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Seller




class Customerform(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),label='username')
    
    class Meta(UserCreationForm):
        model=Customer
        fields=["username"]





class Sellerform(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),label='username')
    

    class Meta(UserCreationForm):
        model=Seller
        fields=["username"]

     
