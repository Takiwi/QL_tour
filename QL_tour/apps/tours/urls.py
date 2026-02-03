from django.urls import path
from .views import tour_detail

urlpatterns = [
    path('detail/<int:id>', tour_detail, name='tour_detail')
]