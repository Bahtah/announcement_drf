from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser

from users.permissions import isOwnerOrReadOnly
from .pagination import AnnouncementPagination

from .models import Announcement, Category, Subcategory
from .serializers import  AnnouncementSerializer, CategorySerializer, SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.filter(price__gt=2000)
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    

class CategoryViewSet(ModelViewSet):    
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SubcategorySerializer