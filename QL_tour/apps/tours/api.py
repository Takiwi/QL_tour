# api.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tour

class TourMapAPI(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        return Response([
            {
                "id": t.id,
                "title": t.title,
                "lat": t.location.y,  # latitude
                "lng": t.location.x,  # longitude
            }
            for t in tours
        ])
