from django.shortcuts import render
from django.views import generic
from .models import Product, Booking
from datetime import datetime

# create, view, edit, cancel 

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.values_list("pitch_type")
    template_name = 'index.html'

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(check_in_date=datetime.now())
    template_name = 'booking.html'


