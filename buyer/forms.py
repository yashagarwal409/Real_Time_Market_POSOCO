from django import forms
from django.db import models
from django.forms import widgets
from .models import UpReserve
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


class UpReserveForm(forms.Form):
    date = forms.DateField(widget=DateInput, validators=[
                           present_or_future_date])
    time = forms.CharField(max_length=20)
    quantity = forms.DecimalField(max_digits=5, decimal_places=2)


class rtmform(forms.Form):
    date = forms.DateField(widget=DateInput, validators=[
                           present_or_future_date])
    time = forms.ChoiceField(label='Time', choices=[])
    quantity = forms.FloatField()

    def __init__(self, timeoptions=None, *args, **kwargs):
        super(rtmform, self).__init__(*args, **kwargs)
        if timeoptions:
            choicelist = []
            for option in timeoptions:
                choicelist.append((str(option), str(option)))
            self.fields['time'].choices = choicelist
