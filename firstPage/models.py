from django.db import models as m
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Categories(m.Model):
    id=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)
    category=m.CharField(max_length=40)

class Product(m.Model):
    uuid=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True)
    name=m.CharField(max_length=100)
    desc=m.TextField()
    pic=m.ImageField(upload_to="pictures")
    approved_at=m.DateTimeField(auto_now_add=False,null=True,blank=True)
    category=m.ForeignKey(Categories,on_delete=m.CASCADE,null=True,blank=True,related_name="prd_category")

class Requested_Product(m.Model):
    uuid=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True)
    name=m.CharField(max_length=100)
    desc=m.TextField()
    pic=m.ImageField(upload_to="requsted_pictures")
    requested_at=m.DateTimeField(auto_now_add=False,null=True,blank=True)
    category=m.ForeignKey(Categories,on_delete=m.CASCADE,null=True,blank=True,related_name="req_prd_category")
    #email=User.EMAIL_FIELD()

class Cart(m.Model):
    user=m.ForeignKey(User,on_delete=m.CASCADE,related_name="cart")

class CartItems(m.Model):
    cart=m.ForeignKey(Cart,on_delete=m.CASCADE,related_name='items')
    product=m.ForeignKey(Product,on_delete=m.SET_NULL,blank=True,null=True)

    #def __str__(self) -> str:
      #  return self.product.name
    
class ContactSeller(m.Model):
    desc=m.TextField()
    product=m.ForeignKey(Product,on_delete=m.SET_NULL,blank=True,null=True)
    seller=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="seller")
    buyer=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="buyer")
    sent_at = m.DateTimeField(auto_now_add=True,null=True,blank=True)

class ContactBuyer(m.Model):
    desc=m.TextField()
    product=m.ForeignKey(Product,on_delete=m.SET_NULL,blank=True,null=True)
    seller=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="seller_reply")
    buyer=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="buyer_reply")
    sent_at = m.DateTimeField(auto_now_add=True,null=True,blank=True)
    #updated_at = m.DateTimeField(auto_now=True)

class buyers(m.Model):
    id=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)
    product=m.ForeignKey(Product,on_delete=m.CASCADE,blank=True,null=True)
    seller=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="seller_info")
    buyer=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True,related_name="buyer_info")

