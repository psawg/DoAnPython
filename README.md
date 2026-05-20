# Luxury Hotel AI - Setup Guide

## 1. Clone Project

```bash
git clone YOUR_GITHUB_LINK
```

---

## 2. Open Project

### PyCharm

* Open Folder Project

### VSCode

* File → Open Folder

---

## 3. Create Virtual Environment

Open Terminal:

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.\.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 6. Run Database Migration

```bash
python manage.py migrate
```

---

## 7. Run Server

```bash
python manage.py runserver
```

---

## 8. Open Website

```text
http://127.0.0.1:8000
```

---

# Database

Project uses SQLite database:

```text
Project_hotel
```

### VSCode SQLite Extension:

* SQLite Viewer
  or
* SQLite

---

# Important Notes

* Do NOT upload `.venv`
* Pull latest code before push:

```bash
git pull
```

* Push source code only

