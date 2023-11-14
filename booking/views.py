from django.shortcuts import render
from django.views import generic
from .models import Product

# create, view, edit, cancel 

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.values_list("pitch_type")
    template_name = 'booking.html'


