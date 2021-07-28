from django.urls import path
from .views import cleardatadown, cleardataup, dat, datbid, datbidlist, displaydata, home, placebid, rtm, rtmbid
urlpatterns = [
    path('home/', home, name="shome"),
    path('rtm/', rtm, name="sellerrtm"),
    path('dat/', dat, name="sellerdat"),
    path('displaydata/', displaydata, name="sellerdisplay"),
    path('placebid/<str:rtmordat>/<str:upordown>/', placebid, name="placebid"),
    path('rtmbid/<str:upordown>/', rtmbid, name='rtmbid'),
    path('datbid/<str:upordown>/', datbid, name='datbid'),
    path('datbidlist/<str:upordown>/', datbidlist, name='datbidlist'),
    path('cleardataup/<str:rtmordat>/', cleardataup, name='cleardataup'),
    path('cleardatadown/<str:rtmordat>/', cleardatadown, name='cleardatadown')
]
