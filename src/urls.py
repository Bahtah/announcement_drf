
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from announcement.api import MentorView, AnnoiuncementRetrieveView, AnnoiuncementUpdateView, AnnoiuncementDeleteView, AnnoiuncementCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('announcement/', MentorView.as_view()),
    path('announcement/<int:pk>/', AnnoiuncementRetrieveView.as_view()),
    path('announcement-update/<int:pk>/', AnnoiuncementUpdateView.as_view()),
    path('announcement-delete/<int:pk>/', AnnoiuncementDeleteView.as_view()),
    path('announcement-create/', AnnoiuncementCreateView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

