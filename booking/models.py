from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your models here.
from django.db import models
from home.models import Schedule, Stop, Seat
from accounts.models import User

from django.core.mail import send_mail
from flight_booking import settings

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_location = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="source_bookings"
    )
    destination_location = models.ForeignKey(
        Stop, on_delete=models.CASCADE, related_name="destination_bookings"
    )
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    seats = models.ManyToManyField(Seat)
    total_seats = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="pending")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    travel_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.schedule.route.departure_location} to {self.schedule.route.arrival_location}"


@receiver(pre_delete, sender=Booking)
def set_seats_available(sender, instance, **kwargs):
    for seat in instance.seats.all():
        seat.is_available = True
        seat.save()


@receiver(post_save, sender=Booking)
def update_schedule_total_available_seats_on_flight(sender, instance, **kwargs):
    schedule = instance.schedule
    total_available_seats_on_flight = schedule.flight.seat_set.filter(
        is_available=True
    ).count()
    schedule.total_available_seats_on_flight = total_available_seats_on_flight
    schedule.save()


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    )

    METHOD_CHOICES = (
        ("credit_card", "Credit Card"),
        ("debit_card", "Debit Card"),
        ("upi", "UPI"),
    )

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking.user.username} - {self.booking.schedule.route.departure_location} to {self.booking.schedule.route.arrival_location} - {self.amount}"


