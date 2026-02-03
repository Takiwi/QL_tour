from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]

    search_fields = ('status',)
