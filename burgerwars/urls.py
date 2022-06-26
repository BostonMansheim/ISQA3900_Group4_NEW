
from . import views
from django.urls import path, re_path
from django.urls import path
from . import views

app_name = 'burgerwars'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('about', views.about, name='about'),
    path('bwmenucat', views.bwmenucat, name='bwmenucat'),
    path('drinkitems', views.drinkitems, name='drinkitems'),
    path('burgeritems', views.burgeritems, name='burgeritems'),
    path('appetitems', views.appetitems, name='appetitems'),
    path('itemdetails/<int:pk>', views.itemdetails.as_view(), name='itemdetails'),
]