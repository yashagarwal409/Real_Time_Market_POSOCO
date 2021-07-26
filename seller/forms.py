from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


class bidform(forms.Form):
    date = forms.DateField(widget=DateInput, validators=[
                           present_or_future_date])
    time = forms.CharField()
    volume = forms.FloatField()
    price = forms.FloatField()


class rtmform(forms.Form):
    date = forms.DateField(widget=DateInput, validators=[
                           present_or_future_date])
    volume = forms.FloatField()
    price = forms.FloatField()
    time = forms.ChoiceField(label='Time', choices=[])

    def __init__(self, timeoptions=None, *args, **kwargs):
        super(rtmform, self).__init__(*args, **kwargs)
        if timeoptions:
            choicelist = []
            for option in timeoptions:
                choicelist.append((str(option), str(option)))
            self.fields['time'].choices = choicelist
