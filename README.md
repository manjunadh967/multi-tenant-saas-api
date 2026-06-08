# Multi-Tenant SaaS Project Management API

A production-style backend application built with Django REST Framework that allows organizations to manage projects and tasks in a multi-tenant environment.

Each organization has its own users, projects, and tasks, ensuring proper data isolation between tenants.

## Features

### Authentication & Authorization

* JWT Authentication
* Custom User Model
* Role-Based Access Control
* Protected API Endpoints

### Multi-Tenant Architecture

* Organizations
* Organization Users
* Data Isolation Between Organizations
* Tenant-Aware Queries

### Project Management

* Create Projects
* Update Projects
* Delete Projects
* Organization-Specific Projects

### Task Management

* Create Tasks
* Update Tasks
* Delete Tasks
* Assign Tasks to Projects
* Admin-Only Task Deletion

### Infrastructure

* PostgreSQL Database
* Docker Containerization
* Docker Compose
* Gunicorn Application Server
* Nginx Reverse Proxy
* Environment Variables (.env)
* GitHub Actions CI Pipeline

---

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Authentication

* Simple JWT

### DevOps

* Docker
* Docker Compose
* Gunicorn
* Nginx
* GitHub Actions

---

## Project Structure

```text
accounts/
organizations/
projects/
tasks/

Dockerfile
docker-compose.yml
requirements.txt
manage.py
```

---

## Architecture

```text
Browser
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django REST Framework
   ↓
PostgreSQL
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd multi-tenant-saas-api
```

### Create Environment File

Create a `.env` file:

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=saas_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432
```

### Run Using Docker

```bash
docker compose up --build
```

### Apply Migrations

```bash
docker compose exec web python manage.py migrate
```

### Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

## API Endpoints

### Authentication

```http
POST /api/register/
POST /api/login/
```

### Projects

```http
GET    /api/projects/
POST   /api/projects/
GET    /api/projects/<id>/
PUT    /api/projects/<id>/
DELETE /api/projects/<id>/
```

### Tasks

```http
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/<id>/
PUT    /api/tasks/<id>/
DELETE /api/tasks/<id>/
```

---

## CI/CD

GitHub Actions automatically:

* Installs dependencies
* Runs Django configuration checks
* Validates application setup
* Builds Docker images

---

## Future Improvements

* Automated API Tests
* Task Comments
* Activity Logs
* Notifications
* API Rate Limiting
* Cloud Deployment

---

## Author

Manjunadh
