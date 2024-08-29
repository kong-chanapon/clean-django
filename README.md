# Project นี้จัดทำขึ้นมาเพื่อนำความรู้เรื่อง Clean Architecture ที่ได้จาก Gofive Bootcamp มาประยุกต์ใช้งาน

## Run

Navigate to the Project Directory

```bash
  cd clean-django
```

Set Up Virtual Environment

```bash
  python3 -m venv venv
  Window -> venv\Scripts\activate
  macOS -> source venv/bin/activate
```

Build and Start the Database with Docker

```bash
  docker-compose up --build -d
```

Running the Application

```bash
  pip install -r requirements.txt
```

Apply Migrations

```bash
  python3 manage.py migrate
```

Create a Superuser

```bash
  python3 manage.py createsuperuser
```

Start the Django Development Server
```bash
  python3 manage.py runserver
```

Stopping the Application
```bash
  docker-compose down
```

## Admin Dashboard
```bash
  http://localhost:8000/admin/
```

## API

Postman
```bash
  https://www.postman.com/mission-geoscientist-50927451/workspace/chanapon-django-clean/collection/37942682-f150b8f8-c0d6-4f44-9f89-136843b4d1b8?action=share&creator=37942682
```