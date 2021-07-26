from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.utils import timezone
User = settings.AUTH_USER_MODEL
# Create your models here.


class Bid(models.Model):
    seller = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=20)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_up = models.BooleanField(default=False)
    is_down = models.BooleanField(default=False)
    is_rtm = models.BooleanField(default=False)
    is_dat = models.BooleanField(default=False)
