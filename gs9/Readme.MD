# 🔑 TokenAuthentication in Django REST Framework (DRF)

## 1. 📖 Easy Definition

**Token Authentication** is a way to secure APIs in Django REST Framework.

- Instead of logging in every time with a **username and password**, the server gives a **token** (a random string).
- The client (like React, Flutter, or Postman) uses this token in the **Authorization header** for every request.

👉 Think of it like a movie ticket 🎟️ — you show it every time to prove you’ve paid, instead of carrying cash.

---

## 2. 🎯 Why We Use It (Real-world Use Case)

- **Mobile apps**: Once a user logs in, the app stores the token and uses it for all API calls.
- **Single Page Applications (SPA)**: React, Angular, or Vue frontend apps send tokens to access Django APIs.
- **Stateless APIs**: No need to keep session info on the server.

👉 Example:
A **food delivery app** lets users log in once. After login, the app gets a token and uses it to fetch orders, update cart, or track delivery without asking for credentials again.

---

## 3. 🗂️ Flow Diagram (Mermaid)

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    Client->>Server: POST /api/token/login (username+password)
    Server->>Database: Verify user
    Database-->>Server: Success
    Server-->>Client: Token (unique string)

    Client->>Server: GET /api/orders (Authorization: Token <token>)
    Server->>Database: Validate token & fetch data
    Database-->>Server: Orders data
    Server-->>Client: JSON Response (orders list)
```

---

## 4. 🛠️ Code Example

### Step 1: Install & Setup

```bash
pip install djangorestframework
pip install djangorestframework-authtoken
```

Add to **`settings.py`**:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

Run migrations:

```bash
python manage.py migrate
```

---

### Step 2: Create Model (optional, using default User)

```python
from django.contrib.auth.models import User
```

_(We can use Django’s default User model, no need for a custom one here.)_

---

### Step 3: Serializer

````python
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
### Step 4: Views
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

# Login & generate token
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

# Protected API
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email
        })
````

---

### Step 5: URLs

```python
from django.urls import path
from .views import LoginView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
]
```

---

## 5. 📌 Sample API Request/Response

### 1️⃣ Login Request

**POST** `/login/`

```json
{
  "username": "ayush",
  "password": "mypassword"
}
```

✅ Response:

```json
{
  "token": "9f3c83e2a0a24b8b8a55d7f3ac4ad63c4f7218b9"
}
```

---

### 2️⃣ Access Protected API

**GET** `/profile/`
Header:

```
Authorization: Token 9f3c83e2a0a24b8b8a55d7f3ac4ad63c4f7218b9
```

✅ Response:

```json
{
  "username": "ayush",
  "email": "ayush@example.com"
}
```

---

## 6. 📝 Key Points (Quick Revision)

- Token Authentication = **username+password → token → use token for future requests**.
- Add `'rest_framework.authtoken'` in `INSTALLED_APPS`.
- Run `python manage.py migrate` to create token table.
- Use `TokenAuthentication` in `REST_FRAMEWORK`.
- Clients must send header:

  ```
  Authorization: Token <your_token>
  ```

- Tokens are **stored in DB** (`authtoken_token` table).
- Good for **mobile apps, SPA, APIs**.

---

✅ Beginner-friendly, secure, and widely used in real-world Django projects.

---

Would you like me to also add a **command-line test with `httpie` or `curl`** so you can quickly check APIs without frontend setup?
