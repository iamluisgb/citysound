from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django.db.models import Q
from django.shortcuts import get_object_or_404

from citysound.tours.models import Tour, Stop, Comment
from citysound.users.models import User

from .serializers import TourSerializer, StopSerializer, CommentSerializer

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
    
class TourCommentViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tour_id = self.kwargs.get('tour_id')
        if tour_id is not None:
            queryset = Comment.objects.filter(tour_id=tour_id).order_by('-created_at')
        else:
            queryset = Comment.objects.none()
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tour_id = self.kwargs.get('tour_id')
        serializer.save(user=request.user, tour_id=tour_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)