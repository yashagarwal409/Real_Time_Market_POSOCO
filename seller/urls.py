from django.urls import path
from .views import datbid, datbidlist, home, placebid, rtmbid
urlpatterns = [
    path('home/', home, name="shome"),
    path('placebid/<str:rtmordat>/<str:upordown>/', placebid, name="placebid"),
    path('rtmbid/<str:upordown>/', rtmbid, name='rtmbid'),
    path('datbid/<str:upordown>/', datbid, name='datbid'),
    path('datbidlist/<str:upordown>/', datbidlist, name='datbidlist'),
]
