from django.http import HttpResponse
from django.shortcuts import render#, get_object_or_404
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import *
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
def checkout(request):
   if request.method == "POST":
       form = CheckoutForm(request.POST)
       if form.is_valid():
           checkout = form.save(commit=False)
           checkout.save()
           return render(request, '#')
   else:
       form = CheckoutForm()

   return render(request, 'burgerwars/checkout.html', {'form': form})


from django.views import generic

class itemdetails(generic.DetailView):
    model = Product


