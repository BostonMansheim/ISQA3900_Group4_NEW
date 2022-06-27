from django import forms
from .models import *


class CheckoutForm(forms.ModelForm):
   class Meta:
       model = Checkout
       fields = ('checkout_customer', 'checkout_payment', 'checkout_product', 'checkout_address')