from datetime import date
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# import datetime
# def duration_of_stay():
#     check_out = datetime.datetime(2023, 1, 31)
#     check_in = datetime.datetime(2023, 1, 29)
#     duration_of_stay = check_out - check_in
#     return duration_of_stay

PITCH_CHOICES = ((0, "Tent"), (1, "Caravan"), (2, "Motorhome"), (3, "Van"), (4, "Glamping"))
CHECK_OUT_TIME = ((11, "11am"), (11, "11am"))
CHECK_IN_TIME = ((3, "3pm"), (3, "3pm"))

class Product(models.Model):

    pitch_type = models.IntegerField(choices=PITCH_CHOICES, default=0)
    pitch_ID = models.CharField(max_length = 6, unique = True)
    check_in_time = models.IntegerField(choices=CHECK_IN_TIME, default=0)
    check_out_time = models.IntegerField(choices=CHECK_OUT_TIME, default=0)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField()
    available = models.BooleanField()
    pitch_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.pitch_ID

    # def is_available(self):
        # how to check dates are not already booked? 
        # needs to look at pitch_type and then if booked is true for any given date return available as false


class Booking(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_type")
    booking_id = models.AutoField(primary_key=True)
    check_in_date = models.DateField(default=date.today)
    check_out_date = models.DateField(default=date.today)
    num_guests = models.IntegerField()
    booking_price = models.FloatField()

    def duration_of_stay(self):
        duration_of_stay = self.check_out_date - self.check_in_date
        return duration_of_stay

    def total_price(self):
        duration_of_stay = self.duration_of_stay()
        total_price = self.product.price * duration_of_stay.days
        return total_price

    def __str__(self):
        return f"{self.booking_id} for {self.product}"
