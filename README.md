# Notes Backend Assignment

This is a simple backend service for managing notes, designed with maintainability and async performance in mind. The project uses **FastAPI** for the API, **MongoDB** as the database, and **Motor** for async database operations. It also supports API versioning so future changes won’t break existing clients.

## Tech Stack

* **FastAPI** – Lightweight, async-friendly Python framework for building APIs
* **MongoDB** – Flexible NoSQL database for storing notes
* **Motor** – Async MongoDB driver for non-blocking DB operations
* **Environment Variables** – `.env` file to keep configuration separate from code

## Features

* Create, read, update, and delete notes
* Soft delete notes so data isn’t permanently lost
* Track activities / audit log for changes
* API versioning (v1 & v2) 
* Clean two-model design for clarity and maintainability

## Getting Started

## Setup

1. Clone the repository

```bash
git clone https://github.com/Pranavi000/notes_python_service
```

2. Create a `.env` file (use the example)
```bash
cp .env.example .env
```
Update values in `.env` if needed.

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run MongoDB locally


```
mongodb://localhost:27017
```

5. Start the application

```bash
uvicorn app.main:app --reload
```

6. Open API docs

```
http://localhost:8000/docs
```

---


## How the APIs Work

**v1 – Basic Notes CRUD**

* `POST /api/v1/notes` – Add a new note
* `GET /api/v1/notes` – Get all notes
* `GET /api/v1/notes/{id}` – Fetch a specific note by ID
* `PUT /api/v1/notes/{id}` – Update a note
* `DELETE /api/v1/notes/{id}` – Soft delete a note

**v2 – Filter by Tag**

* `GET /api/v2/notes/by-tag/{tag}` – Fetch notes with a specific tag

v2 was introduced to show how API versioning can support new features without affecting existing clients.
