
# 📜 Session Authentication & Permissions in Django REST Framework
## 1️⃣ **Session Authentication**

### **Definition**

- **Session Authentication** in Django REST Framework (DRF) uses **Django’s default session backend** to manage authentication.
- When a user logs in via **`django.contrib.auth`**, Django stores the session ID in a cookie on the client’s browser.
- DRF uses this session to authenticate API requests.

---

### **How It Works**

1. User logs in via Django’s standard login view.
2. Django creates a **session** and stores the session ID in a cookie.
3. DRF reads the cookie to check the user’s identity on API requests.
4. If valid, the request is authenticated.

---

### **Setup in `settings.py`**

```python
INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.sessions',
    'django.contrib.auth',
    # other apps...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

---

### **Example Usage**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SessionAuthExampleView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users can access

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}!"})
```

---

### **Pros**

✅ Works well with web apps using Django templates.
✅ Easy to set up.
✅ Uses Django’s built-in authentication.

### **Cons**

❌ Not suitable for token-based mobile APIs.
❌ Requires CSRF protection for unsafe methods (POST, PUT, DELETE).

---

## 2️⃣ **Permission Classes**

### **Definition**

- Permissions in DRF **control whether a request should be granted or denied** after authentication.
- Even if a user is authenticated, they still need the right **permission**.

---

### **Common Permission Classes**

| Permission Class            | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| `AllowAny`                  | No authentication needed; anyone can access                               |
| `IsAuthenticated`           | Only authenticated users can access                                       |
| `IsAdminUser`               | Only admin users can access                                               |
| `IsAuthenticatedOrReadOnly` | Unauthenticated users get read-only access, authenticated users can write |

---

### **Example**

```python
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class PublicView(APIView):
    permission_classes = [AllowAny]  # Anyone can access

    def get(self, request):
        return Response({"message": "This is public!"})

class PrivateView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}"})
```

---

### **Global Permission Setting**

You can apply a permission globally in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

---

## 3️⃣ **CSRF in Session Authentication**

- **CSRF protection** is required for unsafe methods (`POST`, `PUT`, `DELETE`).
- If you call the API from JavaScript, include the CSRF token in headers:

```javascript
fetch("/api/data/", {
  method: "POST",
  headers: {
    "X-CSRFToken": csrftoken,
  },
  body: JSON.stringify({ name: "Test" }),
});
```

---

## 4️⃣ **When to Use Session Authentication**

- Best for **browser-based clients** that also use Django templates.
- Use **TokenAuthentication** or **JWT** for **mobile apps** or **SPA frontends**.

---

## ✅ Summary

- **Session Authentication** → Uses Django's session framework for logged-in users.
- **Permissions** → Restrict access to resources.
- Combine **Authentication** + **Permissions** for **secure APIs**.


If you want, I can now make a **full working Django REST API project** with **Session Authentication + Permission** that you can run locally for testing. This way, you’ll have both the notes and the code in your GitHub. Would you like me to prepare that?
