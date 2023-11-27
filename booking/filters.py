import django_filters 
from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingFilter(django_filters.FilterSet):
    class Meta: 
        model = Booking
        widgets = {'check_in_date': DateInput()}
        fields = [
            'check_in_date', 
            'pitch_ID',
        ]