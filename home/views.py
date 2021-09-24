from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .form import Customerform,Sellerform
from django.contrib import messages
from .models import Customer,MainUser 
from django.contrib.auth import authenticate,login,logout



def  home(request):
    return render(request,'index.html')


    
def  logins(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            if user.u_t==1:
                return HttpResponseRedirect('/')
            if user.u_t==2:
                return HttpResponse('Hello')    
        else:
            return HttpResponseRedirect("home:login")
    return render(request,'login.html')   

def profile(request):
    return render(request,'profile.html')

def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')    



def  customer(request):
    form=Customerform()

    if request.method=='POST':
        form=Customerform(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            
            user=MainUser.objects.create_user(username=username,password=password,u_t=1)
            user.save()
        
            messages.success(request,"Thank ur 4 registration")
    con = {'form':form
    }    
    return render(request,'customer.html',con)   


def search(request):
    if request.method=="POST":
        s=request.POST['s']
        n=request.POST['n']
        v=s.split(',')
        for i in v:
            if i==n:
                return HttpResponse("True")
            else:
                return HttpResponse("You r gay")


    return render(request,'s.html')    