import uuid
import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField

PITCH_CHOICES = (("Tent", "Tent"), ("Caravan", "Caravan"),
                ("Motorhome", "Motorhome"), ("Van", "Van"),
                ("Glamping", "Glamping"))
CHECK_OUT_TIME = ((11, "11am"), (11, "11am"))
CHECK_IN_TIME = ((3, "3pm"), (3, "3pm"))


class Product(models.Model):
    pitch_type = models.TextField(choices=PITCH_CHOICES, default=0)
    pitch_ID = models.CharField(max_length=6, unique=True)
    check_in_time = models.IntegerField(choices=CHECK_IN_TIME, default=0)
    check_out_time = models.IntegerField(choices=CHECK_OUT_TIME, default=0)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    pitch_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.pitch_ID


# UUID field from StackOverflow resource:
# https://stackoverflow.com/questions/32528224/how-to-use-uuid
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name="user")
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    pitch_ID = models.ForeignKey(Product, on_delete=models.CASCADE,
                related_name="booking_pitch", to_field="pitch_ID")
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False,
                unique=True)
    check_in_date = models.DateField(default=date.today)
    check_out_date = models.DateField(default=date.today)
    duration = models.IntegerField()
    number_of_guests = models.IntegerField(default=1,
                    validators=[MinValueValidator(1), MaxValueValidator(10)])
    booking_price = models.FloatField()

    def duration_of_stay(self):
        duration = self.check_out_date - self.check_in_date
        duration_of_stay = duration.days
        return duration_of_stay

    def total_price(self):
        duration_of_stay = Booking.duration_of_stay(self)
        total_price = self.pitch_ID.price * int(duration_of_stay)
        return total_price

    def __str__(self):
        return f"{self.booking_id} for {self.pitch_ID.pitch_type}"

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.duration_of_stay()

        if not self.booking_price:
            self.booking_price = self.total_price()

        super(Booking, self).save(*args, **kwargs)
