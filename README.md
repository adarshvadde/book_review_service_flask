# 📚 Book Review API (Flask)

This is a Book Review REST API built with **Flask**, **SQLAlchemy**, and **Redis**. It supports book and review management, with Redis caching and Swagger documentation.

---

## 📌 Features

- ✅ Add/List Books
- ✅ Add/List Reviews for each book
- ✅ Redis caching on `/books`
- ✅ Error fallback if Redis is down
- ✅ SQLite/SQLAlchemy ORM with DB migrations
- ✅ Swagger/OpenAPI docs (`/apidocs`)
- ✅ Unit & Integration Tests

---

## 📁 Folder Structure

```
book_review_service/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── extensions.py
│   ├── routes.py
│   └── __init__.py
├── tests/
│   ├── test_app.py
│   └── test_integration_cache.py
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🛠️ Step-by-Step Setup Guide

### 1️⃣ Prerequisites

- Python 3.9+
- Redis (locally or via Docker)

### 2️⃣ Clone the Repo

```bash
git clone https://github.com/yourname/book-review-service.git
cd book-review-service
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
# Activate:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Start Redis Server

**Option A: Docker (recommended)**
```bash
docker run -d -p 6379:6379 redis
```

**Option B: Local Redis**
- Windows: Install Memurai or Redis Stack
- Mac: `brew install redis && redis-server`

---

### 6️⃣ Initialize the Database

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

---

### 7️⃣ Run the Flask App

```bash
python manage.py
```

Visit:
- 📘 Swagger Docs: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
- 📚 Books API: [http://localhost:5000/books](http://localhost:5000/books)

---

## 🔍 API Endpoints Summary

| Endpoint                     | Method | Description               |
|-----------------------------|--------|---------------------------|
| `/books`                    | GET    | List all books (cached)   |
| `/books`                    | POST   | Add a new book            |
| `/books/<book_id>/reviews` | GET    | List reviews for a book   |
| `/books/<book_id>/reviews` | POST   | Add review to a book      |

---

## ✅ Swagger/OpenAPI

Integrated with [Flasgger](https://github.com/flasgger/flasgger). Access:

👉 [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## 🧪 Testing

### 1. Unit Tests

```bash
python -m unittest tests/test_app.py
```

### 2. Integration Tests (with Redis mock)

```bash
python -m unittest tests/test_integration_cache.py
```

### 3. All Tests at Once

```bash
python -m unittest discover tests
```

(Optional: Use `pytest` if preferred)

```bash
pip install pytest
pytest
```

---

## ⚠️ Troubleshooting

| Issue                                      | Fix |
|-------------------------------------------|-----|
| `ModuleNotFoundError: No module named 'app'` | Run from project root or set `PYTHONPATH=.` |
| `redis.exceptions.ConnectionError`        | Make sure Redis is running |
| `flask db` errors                         | Ensure `FLASK_APP=manage.py` is set |
| Windows venv errors                       | Use PowerShell: `./venv/Scripts/Activate.ps1` |

---

## 🧠 Tech Used

- Flask
- SQLAlchemy
- Alembic (migrations)
- Redis
- Flask-Caching
- Flasgger (Swagger docs)
- Unittest + Mock

---

## ✅ Take-Home Task Checklist

| Task                                            | Status |
|-------------------------------------------------|--------|
| `GET/POST /books`, `GET/POST /books/<id>/reviews` | ✅ Done |
| Swagger/OpenAPI                                | ✅ Done |
| ORM + Migrations                               | ✅ Done |
| Redis caching + fallback                       | ✅ Done |
| Unit Tests for 2 endpoints                     | ✅ Done |
| Integration test with cache-miss + Redis down  | ✅ Done |

---

## 👨‍💻 Author

Adarsh — Take-Home Flask Book API – 2025
#
