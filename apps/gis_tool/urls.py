from django.urls import path
from .views import gis_map

urlpatterns = [
    path('show_map/',gis_map, name='show_map'),
]