# api.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tour, TourStop

class TourMapAPI(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        return Response([
            {
                "id": t.id,
                "title": t.title,
                "lat": t.location.y,  # latitude
                "lng": t.location.x,  # longitude
                "thumbnail_url": t.thumbnail.url if t.thumbnail else None
            }
            for t in tours
        ])
    
class TourStopMapAPI(APIView):
    def get(self, request, id):
        tour_stops = TourStop.objects.filter(tour_id=id)
        return Response([
            {
                "id": t.id,
                "name": t.name,
                "lat": t.location.y,  # latitude
                "lng": t.location.x,  # longitude
            }
            for t in tour_stops
        ])
