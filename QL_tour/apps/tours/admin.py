from django.contrib import admin
from .models.categories import Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ('id', 'name')