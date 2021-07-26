from django.urls import path
from .views import datbid, datbidlist, placebid, rtmbid
urlpatterns = [
    path('placebid/<str:rtmordat>/<str:upordown>/', placebid, name="placebid"),
    path('rtmbid/<str:upordown>/', rtmbid, name='rtmbid'),
    path('datbid/<str:upordown>/', datbid, name='datbid'),
    path('datbidlist/<str:upordown>/', datbidlist, name='datbidlist'),
]
