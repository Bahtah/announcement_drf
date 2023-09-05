from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from users.permissions import isOwnerOrReadOnly

from .models import Announcement, Category, Subcategory
from .serializers import  AnnouncementSerializer, CategorySerializer, SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = AnnouncementSerializer
    

class CategoryViewSet(ModelViewSet):    
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
     permission_classes = [IsAdminUser]
    serializer_class = SubcategorySerializer