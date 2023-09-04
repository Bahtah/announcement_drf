from django.urls import path
from rest_framework.routers import DefaultRouter

from announcement.api import AnnouncementViewSet, CategoryViewSet, SubcategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('subcategory', SubcategoryViewSet, basename='subcategory')
router.register("", AnnouncementViewSet, basename="announcement")

urlpatterns = []

urlpatterns += router.urls
