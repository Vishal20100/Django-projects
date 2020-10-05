from django.contrib import admin
from . models import Customer,Product,Order,OrderItem,ShippingAddress

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','name','email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','digital']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','date_ordered','complete','transcation_id']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['product','order','quantity','date_added']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=['customer','order','address','city','state','zipcode','date_added']
