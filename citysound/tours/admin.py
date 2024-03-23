from django.contrib import admin

# Models
from .models import Tour, Stop


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
    
class TourStopFilter(admin.SimpleListFilter):
    title = 'tour'
    parameter_name = 'tour_id'
    
    def lookups(self, request, model_admin):
        tours = Tour.objects.all()
        return [(tour.id, tour.name) for tour in tours]
    
    def queryset(self, request, queryset):
        tour_id = self.value()
        if tour_id:
            return queryset.filter(tour_id=tour_id)
        return queryset
    

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    """Stop admin."""
    list_display = (
        'name',
        'tour',
        'audio',
        'image',
    )

    list_filter = (TourStopFilter,)
