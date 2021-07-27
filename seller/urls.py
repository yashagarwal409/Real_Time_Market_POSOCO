from django.urls import path
from .views import cleardatadown, cleardataup, datbid, datbidlist, home, placebid, rtmbid
urlpatterns = [
    path('home/', home, name="shome"),
    path('placebid/<str:rtmordat>/<str:upordown>/', placebid, name="placebid"),
    path('rtmbid/<str:upordown>/', rtmbid, name='rtmbid'),
    path('datbid/<str:upordown>/', datbid, name='datbid'),
    path('datbidlist/<str:upordown>/', datbidlist, name='datbidlist'),
    path('cleardataup/<str:rtmordat>/', cleardataup, name='cleardataup'),
    path('cleardatadown/<str:rtmordat>/', cleardatadown, name='cleardatadown')
]
