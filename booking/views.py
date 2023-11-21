from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product, Booking
from datetime import datetime
from .filters import BookingFilter

# create, view(read), edit(update), cancel(delete)

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.values_list("pitch_type")
    template_name = 'index.html'

# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.filter(BookingFilter)
#     template_name = 'view_booking.html'

# def booking_table(request):
#     booking_filter = BookingFilter(request.GET, queryset=Booking.objects.all())
#     context = {
#         'form': booking_filter.form,
#         'bookings': booking_filter.qs
#     }
#     return render(request, "view_booking.html", context)

# view with queryset Django filters from Youtube - BugBytes: https://www.youtube.com/watch?v=FTUxl5ZCMb8
# view(read) all bookings 
class BookingList(ListView):
    queryset = Booking.objects.all()
    template_name = 'view_booking.html'
    context_object_name = 'booking'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookingFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

# view(read) only user's bookings
# @method_decorator(login_required, name='booking.views.MyBookings')
# class MyBookings(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.all()
#     template_name = 'my_booking.html'

class MyBookings(TemplateView):
    template_name = "my_booking.html"

    @method_decorator(login_required)
    def my_booking(self, *args, **kwargs):
        return super().my_booking(*args, **kwargs)

# make (create) a booking
@login_required()
def make_booking(request):

    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            pitch_ID = form.cleaned_data['pitch_ID']
            check_in = form.cleaned_data['check_in_date']
            check_out = form.cleaned_data['check_out_date']
            num_guests = form.cleaned_data['number_of_guests']

            return_check_in_date = check_in.strftime("%Y%m%d")

            booking_clash = Booking.objects.filter(pitch_ID=pitch_ID, check_in_date=check_in).count()

            if booking_clash >= 1:
                messages.error(request, f'{pitch_ID} is not available on {return_check_in_date}.')
                return redirect('make_booking')
            else:
                form.instance.user = user
                form.save()
                messages.success(
                    request, f"Your booking for a {pitch_ID.pitch_type}, Pitch Number: {pitch_ID} has been made successfully.")

                return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'make_booking.html', context)
