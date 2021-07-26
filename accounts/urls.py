from django.urls import path
from .views import *
urlpatterns = [
    path('signup/buyer/', buyersignup, name="bsignup"),
    path('signup/seller/', sellersignup, name="ssignup")
]
