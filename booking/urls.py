from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('view_booking/', views.BookingList.as_view(), name='booking_table'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('my_bookings/', views.MyBookings.as_view(), name='my_bookings'),
]