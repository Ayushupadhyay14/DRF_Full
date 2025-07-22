from rest_framework import serializers
from serializers import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


def create(self,validate_data):
    return Student.objects.create(**validate_data)