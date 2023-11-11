import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# import datetime
# def duration_of_stay():
#     check_out = datetime.datetime(2023, 1, 31)
#     check_in = datetime.datetime(2023, 1, 29)
#     duration_of_stay = check_out - check_in
#     return duration_of_stay

PITCH_CHOICES = ((0, "Tent"), (1, "Caravan"), (2, "Motorhome"), (3, "Van"), (4, "Glamping") )

class Book(models.Model):
    booking_id = models.AutoField(primary_key=True)
    pitch_type = Products.pitch_type
    pitch_image = Products.pitch_image
    check_in = models.DateTimeField() #what is needed in brackets?
    check_out = models.DateTimeField()
    duration = duration_of_stay(self)
    availability = products.availabile 
    num_guests = models.IntegerField()
    booking_price = total_price(self)

    def duration_of_stay(self):
        duration_of_stay = self.check_out - self.check_in
        return duration_of_stay

    def total_price(self):
        total_price = products.price * self.duration
        return total_price

class Products(models.Model):
    pitch_type = models.IntegerField(choices=PITCH_CHOICES, default=0)
    price = models.FloatField()
    available = models.BooleanField().is_available()
    pitch-image = loudinaryField('image', default='placeholder')

    def is_available(self):
        #how to check dates are not already booked? 
        # needs to look at pitch_type and then if booked is true for any given date return available as false