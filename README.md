# 🏪 Store Rating System

A Backend Store Rating System built using Flask, MySQL, SQLAlchemy, and Jinja2. The application allows users to rate stores while providing separate dashboards for Admins, Store Owners, and Users.

---

## 🚀 Features

### Admin
- Login securely
- Dashboard with statistics
- Add, edit, and delete stores
- Add, edit, and delete users
- Assign store owners
- View all ratings

### User
- Sign up and login
- Browse available stores
- Search stores
- Submit ratings
- Update ratings
- View personal ratings

### Store Owner
- Login securely
- View owned store
- View average store rating
- View ratings given by users

---

## 🛠 Tech Stack

### Backend
- Flask
- Flask-Login
- SQLAlchemy
- PyMySQL

### Database
- MySQL (Aiven Cloud Database)

### Frontend
- HTML
- CSS
- Bootstrap
- Jinja2 Templates

### Deployment
- Render

---

## 📂 Project Structure

```
Store-Rating-System/
│
├── routes/
├── models/
├── templates/
├── static/
├── utils/
├── constants/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd Store-Rating-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
```

Run the application

```bash
python app.py
```

---

## Live Demo

https://store-rating-system-bm11.onrender.com

---

## Future Enhancements

- Email verification
- Password reset
- Store images
- Rating analytics dashboard
- REST API
- Docker support

---

## Author

**Chandana N L**

GitHub: https://github.com/Chandananl15
