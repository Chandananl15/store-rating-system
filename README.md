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

## 📝 Note

The application opens on the **Login** page by default.

To create a new user account, visit:

```
/signup
```

Example:

```
https://your-app-name.onrender.com/signup
```

After signing up, log in using your registered email and password.

## 🔑 Demo Accounts

### Admin
Email: admin@example.com
Password: ********

### Store Owner
Email: owner@example.com
Password: ********

### User
Create a new account using the `/signup` page.

## Author

**Chandana N L**

GitHub: https://github.com/Chandananl15
