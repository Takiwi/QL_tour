from django.db import models
from django.contrib.gis.db import models
from .tours import Tour

class TourRoute(models.Model):
    tour = models.OneToOneField(
        Tour,
        on_delete=models.CASCADE
    )
    route = models.LineStringField(
        geography=True,
        srid=4326
    )
