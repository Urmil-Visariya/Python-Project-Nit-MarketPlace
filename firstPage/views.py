from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
from .mail import*
import datetime
import pytz
#nit_market_admin priyam@123
# Create your views here.
@login_required(login_url='login/')
def admin_page(request):
     if request.user.is_superuser:
          data=Requested_Product.objects.all()
          #user= User.objects.all().get(email=email)
          context={
               'Data':data,
          }
          if request.method=='POST':
               name=request.POST.get('name')
               c=Categories.objects.create(category=name)
               print(c.category)
          return render(request,"firstPage/admin.html",context)
     return redirect('/')

@login_required(login_url='login/')
def firstpage(request):
    if request.user.is_superuser:
          data=Requested_Product.objects.all()
          context={
               'Data':data,
          }
          if request.method=='POST':
               name=request.POST.get('name')
               c=Categories.objects.create(category=name)
               print(c.category)
          return render(request,"firstPage/admin.html",context)
    
    data=Product.objects.all()
    if request.GET.get('search'):
        data=data.filter(name__icontains = request.GET.get('search'))
    else:
        data=Product.objects.all()
    user=request.user
    categories=Categories.objects.all()
    print(categories)
    context={
        'Data':data,
        'user':user,
        'Categories':categories
    }
    return render(request,"firstPage/firstpage.html",context)


@login_required(login_url='login/')
def add_product(request,uuid):
        prod=Requested_Product.objects.all().get(uuid=uuid)
        Product.objects.create(
            name=prod.name,
            desc=prod.desc,
            pic=prod.pic,
            user=prod.user,
            category=prod.category
        )
        prod.delete()
        
        return redirect('/admin/')


@login_required(login_url='login/')
def prod_page(request,uuid):
        value=Product.objects.all().get(uuid=uuid)
        context={
             "info":value
        }
        return render(request,"firstPage/product.html",context)

@login_required(login_url='login/')
def req_product(request):
    if request.method=='POST':
        data=request.POST
        img=request.FILES.get('pic')
        name=data.get('name')
        desc=data.get('desc')
        category=data.get('Category')
        req_category=Categories.objects.get(category=category)
        value=Requested_Product.objects.create(
        name=name,
        desc=desc,
        pic=img,
        user=request.user,
        category=req_category
        )
    categories=Categories.objects.all()
    return render(request,"firstPage/addproduct.html",{'Categories':categories})


@login_required(login_url='login/')
def add_to_cart(request,uuid):
     user=request.user
     product=Product.objects.get(uuid=uuid)
     cart,_=Cart.objects.get_or_create(user=user)
     if CartItems.objects.all().filter(cart=cart,product_id=uuid):
        print("bhak bsdk")
        return redirect('/')
     else :
        cartitems=CartItems.objects.create(cart=cart,product=product)

     print(cartitems.product.desc)
     return redirect('/cart')


@login_required(login_url='login/')
def cart(request):
    user=request.user
    cart=Cart.objects.get(user=user)
    cartitems=CartItems.objects.filter(cart=cart) 
    context={
        'cartitems':cartitems
    }
    return render(request,'firstPage/cart.html',context)


@login_required(login_url='login/')
def delete_cartitem(request,uuid):
    user=request.user
    cart=Cart.objects.all().get(user=user)
    cartitems=CartItems.objects.filter(cart=cart,product_id=uuid)
    cartitems.delete()
    return redirect('/cart')


@login_required(login_url='login/')
def del_prod(request,uuid):
     prod=Product.objects.all().get(uuid=uuid)
     prod.delete()
     return redirect('/')


@login_required(login_url='login/')
def myproducts(request):
     product=Product.objects.filter(user=request.user)
     context={
          'product':product
     }
     return render(request,'firstpage/myproducts.html',context)


@login_required(login_url='login/')
def contact_seller(request,uuid):
     product=Product.objects.all().get(uuid=uuid)
     if request.method=='POST':
          data=request.POST
          buyermail=data.get('desc')
          #print(datetime.datetime.now())
          date = datetime.datetime.now()
          tz = pytz.timezone('Asia/Kolkata')
          date = tz.localize(date)
          print(date)
          mail=ContactSeller.objects.create(desc=buyermail,product=product,seller=product.user,buyer=request.user,sent_at=date)
          if buyers.objects.filter(product=product,seller=product.user,buyer=request.user).exists():
               pass
          else:
               buyers.objects.create(product=product,seller=product.user,buyer=request.user)
          print(mail)
     context={
          'product':product
     }
     return render(request,'firstpage/contactseller.html',context)


@login_required(login_url='login/')
def showmail(request,uuid):
     product=Product.objects.get(uuid=uuid)
     req_buyers=buyers.objects.filter(product=product,seller=product.user)
     context={
          'buyers':req_buyers
     }
     return render(request,'firstpage/showmail.html',context)


@login_required(login_url='login/')
def readmessage(request,id):
     contact=buyers.objects.get(id=id)
     buyer_mail=ContactSeller.objects.filter(product=contact.product,buyer=contact.buyer)
     mymessages=ContactBuyer.objects.filter(product=contact.product,buyer=contact.buyer)
     email=buyer_mail[0]
     context={
          'buyer_mail':buyer_mail,
          "email":email,
          'mymessages':mymessages
     }
     return render(request,'firstpage/buyermessage.html',context)

@login_required(login_url='login/')
def contact_buyer(request,id):
      info=ContactSeller.objects.get(id=id)
      product=Product.objects.get(uuid=info.product_id)
      context={
     'product':product
     }
      if request.method=='POST':
          data=request.POST
          buyermail=data.get('desc')
          print(datetime.datetime.now())
          date = datetime.datetime.now()
          tz = pytz.timezone('Asia/Kolkata')
          date = tz.localize(date)
          print(date)
          mail=ContactBuyer.objects.create(desc=buyermail,product=product,seller=request.user,buyer=info.buyer,sent_at=date)
      return render(request,'firstpage/contactbuyer.html',context)

@login_required(login_url='login/')
def seller_response(request,uuid):
     sellermail=ContactBuyer.objects.filter(product_id=uuid,buyer=request.user)
     mymessage=ContactSeller.objects.filter(product_id=uuid,buyer=request.user)
     if sellermail:
        seller_info=sellermail[0]
        context={
            'sellermail':sellermail,
            'mymessage':mymessage,
            'seller_info':seller_info
        }
        return render(request,'firstpage/sellerresponse.html',context)
     return render(request,'firstpage/sellerresponse.html')
     

@login_required(login_url='login/')
def category_products(request,id):
     category_products=Product.objects.filter(category_id=id)
     return render(request,'firstpage/category_products.html',{'category_products':category_products})

    
