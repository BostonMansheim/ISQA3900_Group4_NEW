from django.contrib import admin
from .models import Customer, Address, Payment, Topping, Product, Cart, Item

"""
# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class AddressList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class PaymentList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class ToppingList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class ProductList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class CartList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


class ItemList(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    ordering = []


admin.site.register(Customer, CustomerList)
admin.site.register(Address, AddressList)
admin.site.register(Payment, PaymentList)
admin.site.register(Topping, ToppingList)
admin.site.register(Product, ProductList)
admin.site.register(Cart, CartList)
admin.site.register(Item, ItemList)
"""

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Item)
