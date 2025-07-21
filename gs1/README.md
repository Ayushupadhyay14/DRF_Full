```markdown
# 🌐 Django REST Framework (DRF) Notes with Definitions & Use Cases
## 📘 What is Django REST Framework (DRF)?

**Django REST Framework (DRF)** is a **powerful and flexible toolkit** for building **Web APIs** using the Django web framework.

It allows developers to expose Django models and data to frontend apps, mobile apps, or other services in the form of **RESTful APIs** (typically using JSON over HTTP).
---
## ✅ Why Use DRF?

| Feature            | Definition                                                    | Use Case Example                                    |
| ------------------ | ------------------------------------------------------------- | --------------------------------------------------- |
| 🔹 RESTful APIs    | A standard way to allow apps to **read/write data over HTTP** | Mobile app fetches user profile via API             |
| 🔹 Authentication  | Built-in support for **login, token, permissions**            | Protect API access using Token Auth or JWT          |
| 🔹 Serializers     | Converts Django models to **JSON** and vice versa             | Send product data to frontend in JSON format        |
| 🔹 Browsable API   | Beautiful web-based UI to test your API endpoints             | Developers can test endpoints without Postman       |
| 🔹 Reusability     | Use same logic across web app and API                         | Reuse `ModelSerializer` for both web forms and APIs |
| 🔹 ORM Integration | Fully integrates with Django's ORM and QuerySets              | Query all users and return as API response          |
---
## 🛠 Installation

### Step 1: Install via pip

```bash
pip install djangorestframework
```
````
### Step 2: Add to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
]
```
---
## ❌ How to Uninstall DRF

```bash
pip uninstall djangorestframework
```
---
## ⚙️ Quick Setup Example

### 🔹 1. Create a Serializer

#### ✅ Definition:

A **Serializer** in DRF is used to convert complex data like Django QuerySets into **native Python datatypes**, which can then be easily converted into **JSON**.

#### 🔧 Use Case:

Send a list of user profiles in JSON format to a React frontend.

```python
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
```

---

### 🔹 2. Create a View using `APIView`

#### ✅ Definition:

**APIView** is a class-based view in DRF that gives you **full control** over how to handle HTTP methods like `GET`, `POST`, etc.

#### 🔧 Use Case:

Build a custom API endpoint that returns a list of profiles when accessed via `GET`.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
```

---

### 🔹 3. Add URL in `urls.py`

#### ✅ Definition:

Defines the endpoint (route) for your API so clients can access it via a URL.

#### 🔧 Use Case:

The mobile app fetches user profile data by hitting `/api/profiles/`.

```python
from django.urls import path
from .views import ProfileList

urlpatterns = [
    path('api/profiles/', ProfileList.as_view(), name='profile-list'),
]
```

---

## 🔗 Useful Links

- 🔗 [Official DRF Documentation](https://www.django-rest-framework.org/)
- 🔗 [Django Official Docs](https://docs.djangoproject.com/)

---

## 📌 What's Next?

| Feature                    | Definition                                     | Use Case Example                              |
| -------------------------- | ---------------------------------------------- | --------------------------------------------- |
| **Generic Views**          | DRF views that reduce boilerplate using mixins | Quickly build CRUD endpoints                  |
| **ViewSet + Router**       | Automatically handle routing for views         | Define all API logic in one class             |
| **JWT Authentication**     | Secure way to manage tokens for login/logout   | Used for securing mobile/SPA access           |
| **Filtering & Pagination** | Return paginated or filtered results           | Show 10 products per page, filter by category |
| **Permissions**            | Controls access to views based on user role    | Only admin can delete users                   |
