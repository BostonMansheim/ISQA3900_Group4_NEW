from django.http import HttpResponse
from django.shortcuts import render#, get_object_or_404
from django.shortcuts import redirect
# Create your views here.


def home(request):
    return render(request, 'burgerwars/home.html',
                  {'burgerwars': home})


def about(request):
    return render(request, 'burgerwars/about.html', {'burgerwars': about})


def bwmenucat(request):
    return render(request, 'burgerwars/bwmenucat.html', {'burgerwars': bwmenucat})


def drinkitems(request):
    return render(request, 'burgerwars/drinkitems.html', {'burgerwars': drinkitems})


def burgeritems(request):
    return render(request, 'burgerwars/burgeritems.html', {'burgerwars': burgeritems})


def appetitems(request):
    return render(request, 'burgerwars/appetitems.html', {'burgerwars': appetitems})