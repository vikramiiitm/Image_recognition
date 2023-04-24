from django.urls import path, include
from rest_framework import routers

from recognize import views

router = routers.DefaultRouter()
router.register(r'image', views.ImageViewset, basename='images')

urlpatterns = [
    path("", include(router.urls))
    ]