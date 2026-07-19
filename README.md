# 🏪 Store Rating System

A full-stack **Store Rating System** built using **Flask**, **MySQL**, **SQLAlchemy**, and **Flask-Login** with secure authentication and role-based access control.

The application allows users to register, browse stores, submit ratings, and update their ratings. It also provides dedicated dashboards for **Admins**, **Store Owners**, and **Users**.

---

# 🚀 Live Demo

**Live Application:**

> https://YOUR-RENDER-LINK.onrender.com

---

# ✨ Features

## 👨‍💼 Admin

- Secure login
- Dashboard with system statistics
- Add, edit, and delete stores
- Add, edit, and delete users
- Assign Store Owners
- View all submitted ratings

---

## 👤 User

- Create a new account
- Secure login/logout
- Browse stores
- Search stores
- Submit ratings
- Update existing ratings
- View personal ratings

---

## 🏬 Store Owner

- Secure login
- View owned store
- View average store rating
- View all ratings submitted by users

---

# 🛠 Tech Stack

### Backend

- Flask
- SQLAlchemy
- Flask-Login
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

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Store-Rating-System/
│
├── constants/
├── models/
├── routes/
├── static/
├── templates/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Store-Rating-System.git
```

## 2️⃣ Navigate to the Project

```bash
cd Store-Rating-System
```

## 3️⃣ Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a file named **`.env`** in the project's root directory.

Add the following variables:

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
```

⚠️ **Do not commit your `.env` file to GitHub.**

---

# 📌 Where to Get the Environment Variables

## Database Credentials

This project uses **Aiven MySQL**.

Login to your Aiven account.

Open your MySQL service.

Copy the following values:

| Variable | Description |
|----------|-------------|
| DB_HOST | Host |
| DB_PORT | Port |
| DB_NAME | Database Name |
| DB_USER | Username |
| DB_PASSWORD | Password |

---

## SECRET_KEY

Generate a secure secret key using Python:

```python
import secrets
print(secrets.token_hex(32))
```

Copy the generated value into:

```env
SECRET_KEY=your_generated_secret_key
```

---

# ▶️ Run the Application

```bash
python app.py
```

The application will run on:

```
http://127.0.0.1:5000
```

---

# 🧪 How to Use

When the application starts, you'll be redirected to the **Login** page.

### New Users

If you don't have an account, visit:

```
/signup
```

Example:

```
https://YOUR-RENDER-LINK.onrender.com/signup
```

Create a new account and then log in using your registered email and password.

---

# 🔑 Demo Accounts (Optional)

If you have created demo accounts, you can add them here.

### Admin

```
Email: admin@example.com
Password:Admin@123
```

### Store Owner

Admin can create new store owner
login using admin then create store owner and use that

### User

Create a new account using:

```
/signup
```

---

# 🌐 Deployment

The application is deployed on **Render**.

Database is hosted on **Aiven MySQL Cloud**.

---


# 🚀 Future Enhancements

- Password Reset
- Email Verification
- Store Images
- Rating Analytics Dashboard
- REST API
- Docker Support
- JWT Authentication
- Responsive UI Improvements

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👩‍💻 Author

**Chandana N L**

GitHub:
https://github.com/Chandananl15

LinkedIn:
https://www.linkedin.com/in/chandu15/

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
