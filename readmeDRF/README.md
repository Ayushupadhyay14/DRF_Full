# 🔐 Basic Authentication & Permission Classes in Django REST Framework (DRF)

## 📌 Overview

Django REST Framework (DRF) provides powerful **authentication** and **permission** systems to secure APIs.

- **Authentication** verifies _who_ the user is.
- **Permissions** check _what_ the authenticated user is allowed to do.

## 1️⃣ Basic Authentication in DRF

Basic Authentication uses **HTTP Basic Authentication** headers to verify username and password for each request.

### 🔹 How It Works

- The client sends credentials (`username:password`) in **Base64** format via the HTTP `Authorization` header.
- DRF decodes and validates them against the Django `User` model.
- If valid → request is authenticated; otherwise → `401 Unauthorized`.

---

### 🔹 DRF Settings for Basic Authentication

In `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}
```

---

### 🔹 Example: Applying Basic Authentication

**views.py**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ExampleView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, authenticated user!"})
```

---

## 2️⃣ Permission Classes in DRF

Permission classes define **access rules** after authentication.

### 🔹 Common Built-in Permission Classes

| Permission Class            | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| `AllowAny`                  | Grants access to **everyone**, authenticated or not                 |
| `IsAuthenticated`           | Grants access **only** to authenticated users                       |
| `IsAdminUser`               | Grants access **only** to admin (`is_staff=True`) users             |
| `IsAuthenticatedOrReadOnly` | Read access for everyone; write access only for authenticated users |

---

### 🔹 Example: Using Permissions

**views.py**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogPostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({"message": "Anyone can read this"})

    def post(self, request):
        return Response({"message": "Only authenticated users can create posts"})
```

---

## 3️⃣ Custom Permission Class

You can create your own permission logic.

**permissions.py**

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

**views.py**

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .permissions import IsOwner
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
```

---

## 4️⃣ Testing Basic Authentication

- Use **Postman** or **curl**:

```bash
curl -u username:password http://localhost:8000/api/example/
```

---

## 📌 Summary

- **BasicAuthentication** → Simple username/password check per request.
- **Permission Classes** → Define who can access API endpoints.
- Always use **HTTPS** with Basic Auth to protect credentials.
- Use **Custom Permissions** for complex authorization rules.

---

## 📚 References

- [DRF Authentication Docs](https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication)
- [DRF Permission Docs](https://www.django-rest-framework.org/api-guide/permissions/)

---

If you want, I can now make a **GitHub-ready README** for **CRUD APIs with ModelViewSet** so you have both authentication and CRUD explained in one repo. That way, your repo looks like a complete DRF guide. Would you like me to make that?
