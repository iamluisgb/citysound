from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


from django.db.models import Q
from django.shortcuts import get_object_or_404

from citysound.tours.models import Tour, Stop
from citysound.users.models import User

from .serializers import TourSerializer, StopSerializer

class TourViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tour.objects.all()
        location = self.request.query_params.get('location', None)
        created_by_name = self.request.query_params.get('created_by', None)
        name = self.request.query_params.get('name', None)

        conditions = Q()
        if location:
            conditions &= Q(location__icontains=location)
        if created_by_name:
            conditions &= Q(created_by__username__icontains=created_by_name)
        if name:
            conditions &= Q(name__icontains=name)

        queryset = queryset.filter(conditions)
        
        return queryset
    
class TourStopViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = StopSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tour_id = self.kwargs.get('tour_id')
        if tour_id is not None:
            queryset = Stop.objects.filter(tour_id=tour_id).order_by('name')
        else:
            queryset = Stop.objects.none()
        return queryset
    