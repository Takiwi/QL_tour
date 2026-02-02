from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from apps.tours.models.tour_schedules import TourSchedules

class Status(models.TextChoices):
    PENDING = 'PENDING', 'Chua dat'
    CONFIRMED = 'CONFIRMED', 'Da xac nhan'
    CANCELLED = 'CANCELLED', 'Da huy'

class Bookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour_schedule = models.ForeignKey(TourSchedules, on_delete=models.CASCADE)
    total_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=Status.choices, default=Status.PENDING)
    create_at = models.DateTimeField(auto_now_add=True)