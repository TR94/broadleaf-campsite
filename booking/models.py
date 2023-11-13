from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# import datetime
# def duration_of_stay():
#     check_out = datetime.datetime(2023, 1, 31)
#     check_in = datetime.datetime(2023, 1, 29)
#     duration_of_stay = check_out - check_in
#     return duration_of_stay

class Products(models.Model):

    PITCH_CHOICES = ((0, "Tent"), (1, "Caravan"), (2, "Motorhome"), (3, "Van"), (4, "Glamping"))
    CHECK_OUT_TIME = ((0, "11am"))
    CHECK_IN_TIME = ((0, "3pm"))

    pitch_type = models.IntegerField(choices=PITCH_CHOICES, default=0)
    check_in_time = models.IntegerField(choices=CHECK_IN_TIME, default=0)
    check_out_time = models.IntegerField(choices=CHECK_OUT_TIME, default=0)
    price = models.FloatField()
    date = models.DateField()
    available = models.BooleanField()
    pitch_image = CloudinaryField('image', default='placeholder')

    # def is_available(self):
        # how to check dates are not already booked? 
        # needs to look at pitch_type and then if booked is true for any given date return available as false


class Booking(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name="product_type")
    booking_id = models.AutoField(primary_key=True)
    check_in_date = models.DateTimeField(default=datetime.now)
    check_out_date = models.DateTimeField(default=datetime.now)
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
        return f"Booking made for {self.check_in_date} for {self.duration_of_stay()}"
