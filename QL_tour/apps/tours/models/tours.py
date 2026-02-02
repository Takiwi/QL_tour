from django.db import models
from .locations import Location
from .categories import Categories

class Status(models.TextChoices):
    DRAFT = 'DRAFT', 'Nhap'
    ACTIVE = 'ACTIVE', 'Kich hoat'
    HIDDEN = 'HIDDEN', 'An'

class Tours(models.Model):
    title = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.DateTimeField()
    max_people = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    status = models.CharField(choices=Status.choices, default=Status.ACTIVE)
    create_at = models.DateTimeField(auto_now_add=True)
