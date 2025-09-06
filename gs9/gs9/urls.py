
# from django.contrib import
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.views import StudentModelViewSet
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'students', StudentModelViewSet, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gottoken/', obtain_auth_token),
    path('', include(router.urls)),
]
