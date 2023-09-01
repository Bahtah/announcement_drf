from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .models import Announcement
from .serializers import AnnouncementListSerializer, AnnouncementCreateSerializer, AnnouncementRetrieveSerializer, AnnouncementUpdateSerializer, AnnouncemenDeleteSerializer

class MentorView(APIView):
    
    def get(self, request, *args, **kwargs):
        ads = Announcement.objects.all()
        ads_json = AnnouncementListSerializer(ads, many=True) 
        return Response(ads_json.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = AnnouncementCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

class AnnoiuncementRetrieveView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementRetrieveSerializer
    
    
class AnnoiuncementUpdateView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementUpdateSerializer
    
    
class AnnoiuncementDeleteView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncemenDeleteSerializer
    

class AnnoiuncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementRetrieveSerializer
