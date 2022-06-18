from django.http import HttpResponse
from django.shortcuts import render#, get_object_or_404
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'burgerwars/home.html',
                  {'burgerwars': home})