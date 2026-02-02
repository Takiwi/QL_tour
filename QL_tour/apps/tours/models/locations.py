from django.db import models

class Location(models.Model):
    name = models.CharField()
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()