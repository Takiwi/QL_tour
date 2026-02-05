from django.shortcuts import render
from ..tours.models.tours import Tour

# Create your views here.
def gis_map(request):
    tours = Tour.objects.all()
    return render(request, 'map.html', {'tours': tours})