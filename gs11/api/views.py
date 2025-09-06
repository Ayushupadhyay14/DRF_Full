from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle
from .models import Student
from rest_framework.authentication import SessionAuthentication

# Create your views here.


# Fixed ModelSet -> ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Fixed authentication_class -> authentication_classes
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        return Response({"message": "Welcome! You are allowed"})
