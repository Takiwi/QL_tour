from django.urls import path

from .api import TourMapAPI, TourStopMapAPI
from .views import tour_detail

urlpatterns = [
    path('detail/<int:id>', tour_detail, name='tour_detail'),
    path('map/', TourMapAPI.as_view(), name='tour_list_api'),
    path('map_stops/<int:id>', TourStopMapAPI.as_view(), name='tour_stops_list_api'),
]