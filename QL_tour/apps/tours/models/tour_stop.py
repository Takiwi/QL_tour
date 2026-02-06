from django.db import models
from django.contrib.gis.db import models

class TourStop(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(geography=True, srid=4326)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order}. {self.name}"