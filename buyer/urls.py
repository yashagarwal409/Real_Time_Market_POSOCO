from buyer.models import ClearedReserveUp
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name='bhome'),
    path('update/', update, name='update'),
    path('displaydata/', display, name='display'),
    path('rtm/', rtm, name='rtm'),
    path('dat/', dat, name='dat'),
    path('update/rtm', updatertm, name='updatertm'),
    path('update/dat', updatedat, name='updatedat'),
    path('refresh/dat', refreshdat, name='refreshdat'),
    path('reserve/<str:datorrtm>', reserve, name='reserves'),
    path('refresh/rtm', refreshrtm, name='refreshrtm'),
    path('declaration/<str:datorrtm>', declaration, name='declaration'),
    path('schedule/<str:datorrtm>', schedule, name='schedule'),
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
