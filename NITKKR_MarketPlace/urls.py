"""
URL configuration for NITKKR_MarketPlace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from firstPage.views import *


urlpatterns = [
    path("main/", admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',user_views.logout_view,name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('admin/',admin_page),
    path('admin/add_product/<uuid>',add_product),
    path("",firstpage,name='home-page'),
    path("firstpage/<uuid>",prod_page),
    path("sell/",req_product),
    path("add_to_cart/<uuid>",add_to_cart,name='add_to_cart'),
    path("cart",cart,name='cart'),
    path("cart/Delete/<uuid>",delete_cartitem,name="del-cartitem"),
    path('myproducts/delete/<uuid>',del_prod),
    path('myproducts/',myproducts,name='myproducts'),
    path('contactseller/<uuid>',contact_seller),
    path('myproducts/mail/<uuid>',showmail),
    path('seller_response/<uuid>',seller_response),
    path('myproducts/mail/readmessage/contactbuyer/<id>',contact_buyer),
    path('seller_response/contactseller/<uuid>',contact_seller),
    path('myproducts/mail/readmessage/<id>',readmessage),
    path('category_products/<id>',category_products),
    path('category_products/add_to_cart/<uuid>',add_to_cart),
    path("category_products/firstpage/<uuid>",prod_page),
    path("myproducts/firstpage/<uuid>",prod_page),
    path("cart/firstpage/<uuid>",prod_page),
    path("", include('users.urls')),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)