from rest_framework.viewsets import ModelViewSet

from .models import Announcement
from .serializers import  AnnouncementSerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer