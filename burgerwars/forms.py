from django import forms
from .models import *


class CheckoutForm(forms.Form):
    pass
    #name = forms.CharField(Label='name', max_length=200)
    #email = forms.EmailInput(Label='email')
    #address = forms.CharField(Label='address', max_length=200)
    #card = forms.IntegerField(Label='card')
    #exp = forms.CharField(Label='exp')
    #cvv = forms.IntegerField(Label='CVV')
