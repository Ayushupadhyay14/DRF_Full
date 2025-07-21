from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
# Mdel Object -Single Student Data


def student_details(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializers(stu)
    print(stu)  # here print id serizer model id
    # it help to get dat showe all serilizer data
    json_data = JSONRenderer().render(serializer.data)
    # here print Serilizers all object when user are create :
    print(serializer)
    print(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    # print(serializer)# here print Serilizers all object when user are create :
    # print(serializer.data)#
    return HttpResponse(json_data, content_type='application/json')
