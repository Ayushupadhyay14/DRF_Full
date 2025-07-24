from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer


def student_api(request):
    if request.method == 'GET':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)

            id = pythondata.get('id', None)

            if id is not None:
                try:
                    stu = Student.objects.get(id=id)  # ✅ Use dynamic id
                    serializer = StudentSerializer(stu)
                except Student.DoesNotExist:
                    res = {'error': 'Student not found'}
                    json_data = JSONRenderer().render(res)
                    return HttpResponse(json_data, content_type='application/json')
            else:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu, many=True)

            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        except Exception as e:
            res = {'error': f'Invalid JSON or request: {str(e)}'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

    res = {'error': 'Only GET method is allowed'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')
