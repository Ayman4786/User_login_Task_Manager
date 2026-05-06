# Procedural Django Backend (Task & User Management System)

A production-style Django backend built entirely with Function-Based Views (FBVs).  
It demonstrates clean separation of concerns, explicit request/response handling, and strong backend fundamentals without relying on heavy abstractions or complex frontends.

---

## Tech Stack

| Layer          | Technology            |
|----------------|-----------------------|
| Backend        | Django 4.x / 5.x      |
| Language       | Python 3.10+          |
| Database       | SQLite (development)  |
| Authentication | Django Auth System    |
| Frontend       | HTML, CSS (minimal)   |

---

## Features

### Authentication & Authorization
- User registration, login, and logout
- Secure password handling via Django's built-in auth
- Route protection using `@login_required`
- Staff-only pages with role-based access control

### User Profile Management
- `UserProfile` model with `OneToOneField` to `User`
- Edit username, email, and profile image
- Default profile image fallback
- Account deletion with cascade cleanup
- Django signals for:
  - Automatic profile creation on user signup
  - Media file cleanup on profile update and delete

### Task Management
- Task model with user ownership
- Full CRUD (Create, Read, Update, Delete) via FBVs
- User-specific task access enforcement
- Task completion toggle
- Search functionality using `Q` objects
- Pagination on task list view

### Django ORM & Data Handling
- Complex queries with `filter()` and `Q` objects
- Dataset ordering and filtering
- Aggregation with `annotate()` and `Count()`
- ORM logic validated through Django shell

### Staff Dashboard
- System-wide analytics view (staff only)
- Displays total users, total tasks
- User rankings sorted by task count

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (for admin and staff access)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
