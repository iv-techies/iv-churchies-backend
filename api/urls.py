from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
