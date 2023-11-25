import django_filters
from .models import Booking

class BookingFilter(django_filters.FilterSet):
    class Meta: 
        model = Booking
        fields = [
            'check_in_date', 
            'pitch_ID'
        ]