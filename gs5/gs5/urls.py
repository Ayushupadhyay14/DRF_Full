
from django.contrib import admin
from django.urls import path
from api import views
# from api.views import StudentRetrieveUpdateDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentListCreate.as_view(),
         name='student-list-create'),

]
