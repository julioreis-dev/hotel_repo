from django import forms
from .widgets import DatePickerInput
from .models import Reservation



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['checkin', 'number_host']
        widgets = {
            'checkin': DatePickerInput(),
        }
