from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('view_booking', views.BookingList.as_view(), name='view_booking'),
    path('make_booking/', views.make_booking, name='make_booking'),
]