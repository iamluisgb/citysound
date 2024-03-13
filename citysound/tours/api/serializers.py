from rest_framework import serializers

from citysound.tours.models import Tour

class TourSerializer(serializers.ModelSerializer[Tour]):
    created_by = serializers.SerializerMethodField()
    
    class Meta:
        model = Tour
        fields =  ('id', 'name', 'duration', 'description', 'photo', 'audio', 'location', 'is_active', 'created_by')

    def get_created_by(self, obj):
        return obj.created_by.name