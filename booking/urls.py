from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('view_booking/', views.BookingList.as_view(), name='view_booking'),
    path('make_booking/', views.make_booking, name='make_booking'),
    path('my_bookings/', views.MyBookings.as_view(), name='my_bookings'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('cancel/<booking_id>', views.cancel_booking, name='cancel'),
]