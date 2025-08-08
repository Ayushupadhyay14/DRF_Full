from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    class Meta:
        model = Student
        fields = '__all__'
