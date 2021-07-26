from buyer.models import ClearedReserveUp
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name='bhome'),
    path('update/', update, name='update'),
    path('reserve/', reserve, name='reserves'),
    path('refresh', refresh, name='refresh'),
    path('declaration/', declaration, name='declaration'),
    path('schedule/', schedule, name='schedule'),
    path('upreserve/dat', upreserve, name='upreserve'),
    path('downreserve/dat', downreserve, name='downreserve'),
    path('clearedreserveup/<str:type>/', dispclearup, name='clearedreserveup'),
    path('clearedreservedown/<str:type>/',
         dispcleardown, name='clearedreservedown'),
    path('upreservertm', upreservertm, name='upreservertm'),
    path('downreservertm/', downreservertm, name='downreservertm'),
    path('downreservedat/', downreservedat, name='downreservertm'),
    path('upreservedat', upreservedat, name='upreservedat'),
    path('runcodedatup/', runcodedatup, name='runcodedatup'),
    path('runcodedatdown/', runcodedatdown, name='runcodedatdown')
]
