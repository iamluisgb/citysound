from django.contrib import admin

# Models
from .models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    """Tour admin."""
    list_display = (
                    'name', 
                    'duration', 
                    'description', 
                    'location',
                    'created_by',
                    'is_active',
                    )
