from django.contrib import admin
from .models import Product, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('pitch_ID', 'check_in_date')
    search_fields = ['pitch_ID', 'check_in_date']
    list_display = ('pitch_ID', 'booking_id', 'check_in_date', 'check_out_date', 'num_guests')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('pitch_ID', 'pitch_type')
    search_fields = ['pitch_ID', 'pitch_type']
    list_display = ('pitch_ID', 'pitch_type', 'price')

