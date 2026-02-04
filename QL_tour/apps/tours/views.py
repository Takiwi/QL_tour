from django.http import HttpResponse
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from .models import Tour
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour
from .serializers import TourSerializer

def tour_detail(request, id):
    tour = get_object_or_404(Tour, pk=id)
    return render(request, 'detail.html', {'tour': Tour})