from django.db import models

class TourSchedules(models.Model):
    tour = models.ForeignKey('Tours', on_delete=models.CASCADE)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    available_slots = models.IntegerField()