from rest_framework import serializers

from citysound.tours.models import Tour, Stop, Comment

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'coordinates', 'audio', 'image', 'description')


class TourSerializer(serializers.ModelSerializer[Tour]):
    """Tour serializer."""
    created_by = serializers.SerializerMethodField()
    
    class Meta:
        model = Tour
        fields =  ( 'id', 'name', 'duration', 'description', 'photo', 'audio', 'location', 'is_active', 'created_by')
        

    def get_created_by(self, obj):
        return obj.created_by.id
    
class StopSerializer(serializers.ModelSerializer[Stop]):
    """Stop serializer."""
    class Meta:
        model = Stop
        fields = ('id', 'name', 'location_latitude', 'location_longitude', 'audio', 'image', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'tour', 'text', 'created_at')