from django.db import models
from django.contrib.gis.db import models
from .tours import Tour
from .tour_stop import TourStop

class TourRoute(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE
    )
    stop = models.ForeignKey(
        TourStop, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    route = models.LineStringField(
        geography=True,
        srid=4326
    )

    def __str__(self):
        return f"Route for {self.tour.title}"
