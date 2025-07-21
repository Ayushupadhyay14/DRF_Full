```markdown
# 🚀 Learn Django REST Framework (DRF)

Welcome to the **Learn Django REST Framework (DRF)** repository!  
This project is a hands-on learning path for mastering DRF — a powerful toolkit for building **RESTful APIs** using Django.

---

## 📚 What You'll Learn

This course covers the **fundamentals to advanced** concepts of Django REST Framework:

- ✅ What is REST API vs RESTful API
- ✅ Introduction to Django REST Framework
- ✅ Serializers (Basic to ModelSerializer)
- ✅ Views: APIView, Generic Views, ViewSets
- ✅ Routers and URL Routing
- ✅ CRUD Operations with DRF
- ✅ Authentication & Permissions (Token, Session, JWT)
- ✅ Pagination & Filtering
- ✅ Django Models and ORM Integration
- ✅ Working with Postman
- ✅ Building a Complete REST API Project
- ✅ Testing and Debugging API

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **SQLite / PostgreSQL**
- **Postman** (for API testing)

---

## 🗂️ Project Structure

```

learn-drf/
│
├── drf\_tutorial/            # Main Django project
│   ├── settings.py
│   ├── urls.py
│
├── api/                     # Django app for APIs
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── requirements.txt         # Python dependencies
├── manage.py
└── README.md

````

---

## 🚦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/learn-drf.git
cd learn-drf
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

### 5. Test APIs in Postman

Example endpoint:

```
GET http://127.0.0.1:8000/api/items/
```

---

## 🔐 Authentication Setup

* Token-based authentication using DRF's built-in `TokenAuthentication`
* JWT implementation using `djangorestframework-simplejwt`

---

## ✅ Testing

To run test cases (if included):

```bash
python manage.py test
```

> Make sure you’ve written test cases inside a `tests.py` file or `tests/` directory inside your app.

---

## 📁 requirements.txt

```txt
Django>=5.0,<6.0
djangorestframework
djangorestframework-simplejwt
```

---

## 📝 Author

**Ayush Upadhyay**
💼 CEO, Growthify Services
🔗 [LinkedIn](https://linkedin.com/in/ayush-upadhyay)
🐙 [GitHub](https://github.com/Ayushupadhyay14)

---

## 🌟 Star the Repo

If you find this project helpful, please give it a ⭐ and share it with others learning DRF!

---

## 📌 License

This project is licensed under the [MIT License](LICENSE).
