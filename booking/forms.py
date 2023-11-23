from datetime import date
from django import forms
from .models import Booking, Product
from django.core.validators import MaxValueValidator, MinValueValidator 

class DateInput(forms.DateInput):
    # date input widget
    input_type = 'date'

class BookingForm(forms.ModelForm):
# date input widget from: https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/
    # first_name = forms.CharField(initial = 'First Name', required=True)
    # last_name = forms.CharField(initial = 'Last Name', required=True)
    # pitch_ID = forms.MultipleChoiceField(initial = '', required=True)
    # check_in_date = forms.DateField(initial=date.today, required=True) 
    # check_out_date = forms.DateField(initial=date.today, required=True) 
    # number_of_guests = forms.IntegerField(initial=1, required=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'pitch_ID', 'check_in_date', 'check_out_date', 'number_of_guests']
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
        # self.fields['check_out_date'].widget.attrs.update({
        #     'min': self.check_in_date
        # })