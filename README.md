# 🧪 SL3 Lab Project – Fullstack App with Django & Flask

This project integrates a Flask-based microservice alongside a Django-powered main application using Docker Compose. It is structured to be modular and easy to deploy, allowing both apps to run seamlessly together.

---

## 📁 Project Structure

```bash
A_14_SL3_Assessment_3/
│
├── docker-compose.yml
├── Dockerfile-flask
├── Dockerfile-django
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── greeting.html
│
└── django-app/
    ├── manage.py
    ├── requirements.txt
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── documents.html
    │   └── user.html
    └── django_app/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── asgi.py
    ├── dashboard/
    │   └── ...
    ├── documents/
    │   └── ...
    └── user/
        └── ...
```

---

## 🚀 Overview

### Django App:
A full-featured item management web app with a dashboard, user management, and document handling.

- 📂 Modular design  
- 🧑‍💻 Built using Django framework  
- 🧾 Templates: base.html, dashboard.html, user.html, documents.html  

### Flask App:
A microservice that detects programming languages in input text and validates email addresses.

- ⚙️ Built using Flask  
- 🧠 Detects programming languages  
- 📬 Validates emails  
- ✨ Simple UI through greeting.html  

---

## 🐳 Dockerized Setup

Everything is containerized with Docker Compose.

To run the whole stack:

```bash
docker-compose up --build
Make sure you have Docker and Docker Compose installed.

📦 Requirements
Each app has its own dependencies:

Flask
Located in: flask_app/requirements.txt

Django
Located in: django-app/requirements.txt
```
Install them separately if running without Docker:

# Flask
```bash
cd flask_app
pip install -r requirements.txt
```
# Django
```bash
cd ../django-app
pip install -r requirements.txt
```
# ✨ Features
✅ Flask microservice integration

✅ Django with multiple apps (dashboard, user, documents)

✅ Shared templates for a unified UI

✅ Docker Compose for multi-service orchestration

👨‍💻 Developer Notes
Flask app runs on a separate service, accessible via internal Docker network

Django serves as the main frontend

You can easily add more services using the Docker Compose setup

📬 Contact
For questions or suggestions, feel free to raise an issue or reach out on anshulnparate@gmail.com!

Happy coding! 🚀
