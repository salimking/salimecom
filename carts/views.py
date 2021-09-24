from django.http.response import HttpResponse
from product.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from carts.models import Cart,Order
from product.models import  Product
from django.contrib import messages

# Create your views here.
def  cart(request):
    carts=Cart.objects.filter(user=request.user,parchased=False)
    orders=Order.objects.filter(user=request.user,ordered=False)
    total_oroder=orders.count()
    if carts.exists() and orders.exists():
        order=orders[0]
        con={
                'cart':carts,
                'order':total_oroder
            }
        return render(request,'cart.html',con)

    # return render(request,'cart.html')

def  add_cart(request,id):
    if request.user.is_authenticated:
        item=get_object_or_404(Product,id=id)
        order_item=Cart.objects.get_or_create(item=item,user=request.user,parchased=False)
        order_qs=Order.objects.filter(user=request.user,ordered=False)
        if order_qs.exists():
            order=order_qs[0]
            

            if order.orderitems.filter(item=item).exists():
                order_item[0].quantity +=1
                order_item[0].save()
                messages.info(request,"Add the  product")
                return redirect('cart:cart')
                

            else:
                order.orderitems.add(order_item[0])
                return redirect('cart:cart')    

              
        else:
            order=Order(user=request.user)
            order.save()
            order.orderitems.add(order_item[0])
            return redirect('/')

def  remove_cart(request,id):
    if request.user.is_authenticated:
        item=get_object_or_404(Product,id=id)
        order_qs=Order.objects.filter(user=request.user,ordered=False)
        if order_qs.exists():
            order=order_qs[0] 
            if order.orderitems.filter(item=item).exists():
                order_item=Cart.objects.filter(item=item,user=request.user,parchased=False)[0]
                order.orderitems.remove(order_item)
                order_item.delete()
                # return redirect('cart:')    
                return redirect("cart:cart")
            else:
                  
                messages.info(request,"there is not product")
                return redirect("cart:cart")

        else:
            
            return HttpResponse('You have none')

                
           


        
