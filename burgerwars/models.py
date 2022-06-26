from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    username = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.username)


class Address(models.Model):
    address_address = models.CharField(max_length=100)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)

    def __str__(self):
        return str(self.address_address)


class Payment(models.Model):
    payment_nameCard = models.CharField(max_length=100)
    payment_cardNum = models.DecimalField(max_digits=16, decimal_places=0)
    payment_ccv = models.DecimalField(max_digits=3, decimal_places=0)
    payment_expMonth = models.CharField(max_length=20)
    payment_expDay = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return str(self.payment_nameCard)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(max_length=200)
    product_type = models.CharField(max_length=6)

    def __str__(self):
        return str(self.product_name)


class Cart(models.Model):
    cart_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    cart_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cart_customer)


class Item(models.Model):
    item_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_product)

