
# Create your views here.
# from django.shortcuts import render
 from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# GET (all), POST


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # GET (single), PUT, DELETE


# class StudentRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(request, *args, **kwargs)

#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)

#     # def delete(self, request, *args, **kwargs):
#     #     return self.destroy(request, *args, **kwargs)
