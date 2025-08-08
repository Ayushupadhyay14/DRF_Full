Alright — let’s go step-by-step and learn **Function-Based API Views in Django REST Framework (DRF)** in English.

---

## **1. What is a Function-Based API View?**

In DRF, you can create APIs in two main ways:

- **Function-Based Views (FBVs)** — APIs are written as Python functions.
- **Class-Based Views (CBVs)** — APIs are written as Python classes.

FBVs are simpler for beginners and are similar to normal Django views, but they work with DRF tools like **serializers**, **parsers**, **renderers**, etc.

---

## **2. Example: Function-Based API View**

Let’s say we have a `Student` model and want to create an API that:

- **GET** → Fetch all students or a single student.
- **POST** → Add a new student.

---

### **models.py**

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

---

### **serializers.py**

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

---

### **views.py (Function-Based API View)**

```python
import io
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_api(request):
    # GET request
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST request
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save to DB
            return JsonResponse({'msg': 'Data Created'}, status=201)
        return JsonResponse(serializer.errors, status=400)
```

---

### **urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.student_api),
]
```

---

## **3. How it Works**

- **`@api_view(['GET', 'POST'])`** → DRF decorator that converts a normal Django function into an API View and allows only GET and POST methods.
- **`request.data`** → Automatically parses JSON data from the request.
- **`serializer.is_valid()`** → Validates the incoming data.
- **`serializer.save()`** → Saves data to the database.
- **`JsonResponse`** → Returns JSON response to the client.

---

## **4. Testing with Python Requests**

```python
import requests

URL = "http://127.0.0.1:8000/studentapi/"

# POST request (Create data)
data = {
    'name': 'John',
    'roll': 101,
    'city': 'Indore'
}
r = requests.post(url=URL, json=data)
print(r.json())

# GET request (Fetch all data)
r = requests.get(url=URL)
print(r.json())
```

---

## **5. When to Use FBVs**

✅ Simple APIs with less logic
✅ Quick prototyping
✅ When you want easy-to-read and short code

❌ For complex logic, **Class-Based Views** or **ViewSets** are better.

---

If you want, I can also make the **full CRUD Function-Based API View** (GET, POST, PUT, DELETE) so you can **read, insert, update, and delete** in one API. That way it’s production-ready.
