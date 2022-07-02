from datetime import datetime
from django.shortcuts import get_object_or_404
import pytz
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics, permissions, filters, response, status
from rest_framework.pagination import PageNumberPagination
from givito.permissions import IsOwnerOrReadOnly

from givito.service.models import Category, Project, ProjectRegistrant
from givito.service.serializers import CategorySerializer, ProjectBaseSerializer, ProjectRegistrantBaseSerializer, ProjectRegistrantSerializer, ProjectSerializer


class Pagination(PageNumberPagination):
    page_size = 4
    max_page_size = 100
    page_size_query_param = 'count'

class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.filter(deleted_at__isnull=True)
    serializer_class = ProjectSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'owner__uuid', 'status', 'registrant']
    search_fields = ['owner__name', 'title', 'description']
    ordering_fields = ['title', 'expired_at', 'expected_duration', 'modified_at', 'created_at']
    ordering = ['-created_at']
    
    def create(self, request, *args, **kwargs):
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['owner'] = str(request.user.pk)
        request.data._mutable = mutable

        serializer = ProjectBaseSerializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            serializer = ProjectSerializer(object)
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.filter(deleted_at__isnull=True)
    serializer_class = CategorySerializer
    ordering = ['name']

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'uuid'
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(deleted_at__isnull=True)


class RegistrantView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProjectRegistrant.objects.filter(deleted_at__isnull=True)
    serializer_class = ProjectRegistrantSerializer
    pagination_class = Pagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['owner__uuid', 'project']
    search_fields = ['owner__name', 'description']
    ordering_fields = ['offering_price', 'offering_duration', 'modified_at', 'created_at']
    ordering = ['-created_at']

    def create(self, request, *args, **kwargs):
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['owner'] = str(request.user.pk)
        request.data._mutable = mutable

        if(ProjectRegistrant.objects.filter(owner=request.user, project=request.data['project']).exists()):
            return response.Response({"error":"User has registered"}, status=status.HTTP_409_CONFLICT)

        serializer = ProjectRegistrantBaseSerializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            serializer = ProjectRegistrantSerializer(object)
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrantDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'uuid'
    serializer_class = ProjectRegistrantSerializer
    queryset = ProjectRegistrant.objects.filter(deleted_at__isnull=True)


