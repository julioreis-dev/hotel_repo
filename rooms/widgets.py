from django import forms


class DatePickerInput(forms.DateTimeInput):
    """
    Class to create a object type date
    """
    input_type = 'date'
