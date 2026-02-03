from django.db import models
from django.contrib.gis.db import models
from .tours import Tour

class TourStop(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="stops"
    )
    name = models.CharField(max_length=255)
    location = models.PointField(geography=True, srid=4326)
    order = models.PositiveIntegerField()
