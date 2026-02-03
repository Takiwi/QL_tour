from django.db import models
from .categories import Category
from django.contrib.gis.db import models

class Status(models.TextChoices):
    DRAFT = 'DRAFT', 'Nháp'
    ACTIVE = 'ACTIVE', 'Kích hoạt'
    HIDDEN = 'HIDDEN', 'Ẩn'

class Tour(models.Model):
    title = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.DateTimeField()
    max_people = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.PointField(
        geography=True,  
        srid=4326         
    )
    thumbnail = models.ImageField()
    status = models.CharField(choices=Status.choices, default=Status.ACTIVE)
    create_at = models.DateTimeField(auto_now_add=True)
