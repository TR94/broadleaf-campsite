from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Product, Booking
from datetime import datetime, date, timedelta
from .filters import BookingFilter
from .forms import BookingForm


# create, view(read), edit(update), cancel(delete)

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.values_list("pitch_type")
    template_name = 'index.html'

# view with queryset Django filters from Youtube - BugBytes: https://www.youtube.com/watch?v=FTUxl5ZCMb8
# view(read) all bookings 
class BookingList(ListView):
    
    startdate = date.today()
    enddate = startdate + timedelta(days=180)

    queryset = Booking.objects.filter(check_in_date__range=[startdate, enddate]).order_by('check_in_date')
    template_name = 'view_booking.html'
    context_object_name = 'booking'
    context = {'today': datetime.today()}

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookingFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

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

            date = check_in.strftime("%d, %m, %Y")
            
            bookings = Booking.objects.filter(pitch_ID=pitch_ID, check_in_date__lte = check_in, check_out_date__gte = check_in).count()
           
            if bookings >=1:
                messages.error(request, f'{pitch_ID} is not available on {date}. Please check current bookings for availability')
                return redirect('make_booking')
            else:
                form.instance.user = user
                form.save()
                messages.success(
                    request, f"Your booking for a {pitch_ID.pitch_type}, Pitch Number: {pitch_ID} has been made successfully.")

            return redirect('view_booking')
        else:
            messages.warning(
                    request, "Your booking was unsucessful. Please ensure the form was filled in correctly and your request doesn't clash with another booking")
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'make_booking.html', context)



# view(read) only user's bookings
class MyBookings(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'my_booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('check_in_date')

# edit (update) a booking - only bookings specific to that user
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    bookings = Booking.objects.filter(pitch_ID=pitch_ID, check_in_date__lte = check_in, check_out_date__gte = check_in).count()

    if request.method == 'POST':
        form= BookingForm(request.POST, instance=booking)
        if form.is_valid():
            if bookings >=1:
                messages.error(request, f'{pitch_ID} is not available on {date}. Please check current bookings for availability')
                return redirect('view_booking')
            else:
                form.save()
                messages.success(
                    request, f"Your booking for a {pitch_ID.pitch_type}, Pitch Number: {pitch_ID} has been made successfully.")
                return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)
   

# cancel (delete) a booking - user only
@login_required()
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_booking')


