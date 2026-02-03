from django.db import models

class TourSchedule(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    available_slots = models.IntegerField()