from rest_framework import serializers

from .models import Announcement


class AnnouncementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'description']
        

class AnnouncementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        

class AnnouncemenDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
    
    
    