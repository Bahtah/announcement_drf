from django.urls import path
from rest_framework.routers import DefaultRouter

from announcement.api import AnnouncementViewSet

router = DefaultRouter()
router.register("", AnnouncementViewSet, basename="announcement")

urlpatterns = router.urls
