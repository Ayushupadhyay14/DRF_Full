# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)  # Register ViewSet

urlpatterns = [
    path('student/<int:pk>', include(router.urls)),
]
