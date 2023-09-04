from rest_framework.viewsets import ModelViewSet

from .models import Announcement, Category, Subcategory
from .serializers import  AnnouncementSerializer, CategorySerializer, SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    

class CategoryViewSet(ModelViewSet):    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer