from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from .models import Product, Booking
from .forms import BookingForm
from datetime import datetime

# create, view(read), edit(update), cancel(delete)

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.values_list("pitch_type")
    template_name = 'index.html'

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(check_in_date=datetime.now())
    template_name = 'view_booking.html'

@login_required()
def make_booking(request):

    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['f_name']
            last_name = form.cleaned_data['l_name']
            pitch_ID = form.cleaned_data['pitch_ID']
            check_in = form.cleaned_data['check_in_date']
            check_out = form.cleaned_data['check_out_date']
            num_guests = form.cleaned_data['num_guests']

            # duration = Booking.duration_of_stay(self)
            return_check_in_date = check_in.strftime("%Y%m%d%H%M%S")

            booking_clash = Booking.objects.filter(
                pitch_ID=pitch_ID, check_in_date=check_in).count()

            if booking_clash >= 1:
                messages.error(request, f'{pitch_ID} is not available on {return_check_in_date}.')
                return redirect('make_booking')
            else:
                form.instance.user = user
                form.save()
                messages.success(
                    request, f"Your booking for a {pitch_ID.pitch_type}, number: {pitch_ID}"
                    "has been made successfully.")

                return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'make_booking.html', context)

