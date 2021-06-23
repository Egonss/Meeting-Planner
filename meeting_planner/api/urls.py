from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet, MeetingViewSet
router = routers.DefaultRouter()
router.register('meeting', MeetingViewSet)  # /api/curs
router.register('rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace="rest_framework"))
]
