from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentModelViewSet   # import directly from app

# DRF Router
router = DefaultRouter()
router.register(r'students', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),   # single include
]
