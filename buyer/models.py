import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db.models.fields import CharField
from django.utils import timezone
User = settings.AUTH_USER_MODEL
# Create your models here.


class TimeBlock(models.Model):
    time = models.CharField(max_length=20)


class Reserve(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class Declaration(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class Schedule(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class UpReserve(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    time = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class ClearedReserveUp(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    mcp = models.DecimalField(max_digits=5, decimal_places=2)
    time_block = models.CharField(max_length=20, default="NoTime")
    date = models.DateField(default=timezone.now)
    is_rtm = models.BooleanField(default=False)
    is_dat = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now)


class ClearEntityUp(models.Model):
    clearedreserve = models.ForeignKey(ClearedReserveUp, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)


class ClearedReserveDown(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    time_block = models.CharField(max_length=20, default="NoTime")
    date = models.DateField(default=timezone.now)
    is_rtm = models.BooleanField(default=False)
    is_dat = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now)


class ClearEntityDown(models.Model):
    clearedreserve = models.ForeignKey(ClearedReserveDown, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
