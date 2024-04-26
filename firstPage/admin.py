from django.contrib import admin
from .models import Product,Requested_Product
# Register your models here.
admin.site.register(Product)
admin.site.register(Requested_Product)