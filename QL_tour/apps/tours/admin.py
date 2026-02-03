from django.contrib import admin
from .models.categories import Category
from .models.tours import Tour
from .models.tour_schedules import TourSchedule

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ('name',)

@admin.register(Tour)
class ToursAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tour._meta.fields]

    search_fields = ('title', 'price', 'category')

@admin.register(TourSchedule)
class TourSchedulesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TourSchedule._meta.fields]

    search_fields = ('name', 'latitude', 'longitude')