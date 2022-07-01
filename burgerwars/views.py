from django.http import HttpResponse
from django.shortcuts import render  # , get_object_or_404
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models.query import *
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


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


from django.views import generic


class itemdetails(generic.DetailView):
    model = Product


def confirmation(request):
    return render(request, 'burgerwars/confirmation.html')


# def contact(request):
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = form.cleaned_data['sender']
#         cc = form.cleaned_data['cc']
#         recipients = ['sender@example.com']
#         recipients.append(sender)
#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect('/thanks/')
#     else:
#         form = ContactForm()
#         return render(request,'/templates/checkout.html',{'form':form})


def send_email(request):
    subject = '{}, Burger Wars Order Confirmation'
    message = 'Your Burger Wars order has been confirmed.'
    user = request.user
    user_email = user.email
    try:
        send_mail(subject, message, 'yourEmailAddress@gmail.com', [user_email])
        sent = True
    except:
        print("Error sending e-mail")
