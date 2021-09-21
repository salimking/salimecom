
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class MainUser(AbstractUser):
    alluser=((1,'customer'),(2,'seller'))
    u_t=models.CharField(max_length=50,choices=alluser,default=2)
   


class Customer(models.Model):
    user=models.OneToOneField(MainUser,on_delete=models.CASCADE,primary_key=True)  
    password=models.CharField(max_length=50)
    USERNAME_FIELD='username'
    def __str__(self) :
        return self.user.username

class Seller(models.Model):
    user=models.OneToOneField(MainUser,on_delete=models.CASCADE,primary_key=True)
    password=models.CharField(max_length=50)

    USERNAME_FIELD='username'
    def __str__(self) :
        return self.user.username

@receiver(post_save,sender=MainUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.u_t==1:
            Customer.objects.create(user=instance)
        if instance.u_t==2:
            Seller.objects.create(user=instance)


@receiver(post_save,sender=MainUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.u_t==1:
        instance.customer.save()
    if instance.u_t==2:
        instance.seller.save()

