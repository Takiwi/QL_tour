from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]

    search_fields = ('status',)