# Procedural Django Backend (Task & User Management System)

This repository contains a **production-style Django backend** built using **Function-Based Views (FBVs)**. The project focuses on clarity, explicit control, and strong backend fundamentals rather than heavy abstractions or frontend complexity.

It demonstrates how to design and implement a complete backend system using core Django features, following clean and maintainable patterns.

---

## Tech Stack

* **Backend Framework:** Django
* **Language:** Python
* **Database:** SQLite (development)
* **Authentication:** Django Auth System
* **Frontend:** HTML, CSS (minimal, backend-focused)

---

## Key Features

### Authentication & Authorization

* User signup, login, and logout
* Secure password handling with Django authentication
* Route protection using `login_required`
* Role-based access control for staff-only pages

### User Profile Management

* `UserProfile` model linked via `OneToOneField` with `User`
* Profile editing (username, email, profile image)
* Default profile image handling
* Account deletion functionality
* Django signals for:

  * Automatic profile creation
  * Media file cleanup on update and delete

### Task Management System

* Task model with user ownership
* Full CRUD operations using **function-based views**
* User-specific task access enforcement
* Task completion tracking
* Search functionality using Django ORM
* Pagination for scalable task listing

### Django ORM & Data Handling

* Complex querying with `filter()` and `Q` objects
* Ordering and filtering datasets
* Aggregation using `annotate()` and `Count()`
* ORM logic validated via Django shell

### Staff Dashboard

* System-wide analytics view
* Total users and total tasks
* User rankings based on task count
* Access restricted to staff users

---

## Project Philosophy

* Explicit request/response handling
* No hidden abstractions
* Clear separation of concerns
* Backend-first design
