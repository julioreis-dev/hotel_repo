from django import forms
from .widgets import DatePickerInput
from .models import Reservation



class ReservationForm(forms.ModelForm):
    """
    Class that lets to create a Form class from a Django model
    """
    class Meta:
        model = Reservation
        fields = ['checkin', 'number_host']
        widgets = {
            'checkin': DatePickerInput(),
        }
