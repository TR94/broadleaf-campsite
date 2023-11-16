from datetime import date
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
# date input widget from: https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/
    class Meta:
        model = Booking
        fields = ['f_name', 'l_name', 'pitch_ID', 'check_in_date', 'check_out_date', 'num_guests']
        widgets = {
            'check_in_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'check_out_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in_date'].widget.attrs.update({
            'min': date.today()
        })