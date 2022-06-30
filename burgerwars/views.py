from django.http import HttpResponse
from django.shortcuts import render  # , get_object_or_404
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views import generic
from django.core.mail import EmailMessage

from django.db.models.query import *


# Create your views here.


def home(request):
    return render(request, 'burgerwars/home.html',
                  {'burgerwars': home})


def about(request):
    return render(request, 'burgerwars/about.html', {'burgerwars': about})


def bwmenucat(request):
    return render(request, 'burgerwars/bwmenucat.html', {'burgerwars': bwmenucat})


def drinkitems(request):
    product = Product.objects.filter()
    return render(request, 'burgerwars/drinkitems.html', {'products': product})


def burgeritems(request):
    product = Product.objects.filter()
    return render(request, 'burgerwars/burgeritems.html', {'products': product})


def appetitems(request):
    product = Product.objects.filter()
    return render(request, 'burgerwars/appetitems.html', {'products': product})


@login_required
def checkout(request, product_key):
    if request.method == "POST":
        product = product_key
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.save()
            return render(request, '#')
    else:
        form = CheckoutForm()
    for i in Product.objects.all().filter(id=product_key):
        productName = i.product_name
        productPrice = i.product_price
        productImage = i.product_image
    return render(request, 'burgerwars/checkout.html',
                  {'form': form, 'productName': productName, 'productPrice': productPrice, 'productImage': productImage,
                   'productID': product_key})


class itemdetails(generic.DetailView):
    model = Product


def send_email_view(request):
    if request.method == 'POST':
        to = request.POST['recipient_email_address']
        send_email('subject of the message', 'email body', '<p>email body</p>', [to, ])
    return render(request, 'index.html')


email = EmailMessage(
    'Hello',
    'Body goes here',
    'test@example.com',
    ['jacobfrisbie@outlook.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)
