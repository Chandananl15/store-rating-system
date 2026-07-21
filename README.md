# 🏪 Store Rating System

A full-stack **Store Rating System** built using **Flask**, **MySQL**, **SQLAlchemy**, and **Flask-Login** with secure authentication, **Email-based Two-Factor Authentication (2FA)**, and **Role-Based Access Control (RBAC)**.

The application enables users to discover stores, submit and update ratings, while providing dedicated dashboards for **Admins**, **Store Owners**, and **Users** with secure role-based access.

---

# 🚀 Live Demo

**Live Application**

> https://YOUR-RENDER-LINK.onrender.com

---

# ✨ Features

## 🔐 Authentication & Security

- User Registration
- Secure Login & Logout
- Password Hashing using Werkzeug
- Email-based Two-Factor Authentication (2FA)
- 6-Digit OTP Verification
- OTP Expiry (5 Minutes)
- OTP Resend Functionality
- Maximum OTP Attempt Limit
- Session-Based Authentication
- Role-Based Access Control (RBAC)
- Protected Routes using Flask-Login
- Secure Email Delivery using Gmail SMTP

---

## 👨‍💼 Admin

- Secure Login with 2FA
- Dashboard with system statistics
- Add, Edit and Delete Users
- Add, Edit and Delete Stores
- Assign Store Owners
- View all submitted ratings
- Manage the entire application

---

## 👤 User

- Create a New Account
- Secure Login with 2FA
- Browse Stores
- Search Stores
- Submit Ratings
- Update Existing Ratings
- View Personal Ratings
- Logout Securely

---

## 🏬 Store Owner

- Secure Login with 2FA
- View Assigned Store
- View Average Store Rating
- View All Ratings Submitted by Users
- Monitor Store Performance

---

# 🔒 Authentication Flow

```text
                 Login
                   │
                   ▼
        Verify Email & Password
                   │
                   ▼
          Generate 6-Digit OTP
                   │
                   ▼
         Send OTP via Gmail SMTP
                   │
                   ▼
          User Enters the OTP
                   │
                   ▼
             Verify OTP
                   │
                   ▼
          Create User Session
                   │
                   ▼
 Redirect Based on User Role
(Admin / Store Owner / User)
```

---

# 🛡 Security Features

- Password Hashing using Werkzeug
- Email-based Two-Factor Authentication (2FA)
- Session-Based Authentication
- Role-Based Access Control (RBAC)
- OTP Expiration
- OTP Attempt Limitation
- OTP Resend Support
- Protected Routes with Flask-Login
- Secure Email Communication using Gmail SMTP

---

# 🛠 Tech Stack

## Backend

- Flask
- SQLAlchemy
- Flask-Login
- Flask-Mail
- PyMySQL
- Werkzeug Security

## Database

- MySQL
- Aiven Cloud MySQL

## Frontend

- HTML5
- CSS3
- Bootstrap
- Jinja2 Templates

## Deployment

- Render

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
Store-Rating-System/
│
├── constants/
├── models/
├── routes/
├── services/
├── static/
├── templates/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Chandananl15/store-rating-system.git
```

---

## 2. Navigate to the Project

```bash
cd store-rating-system
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

SECRET_KEY=

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_DEFAULT_SENDER=
```

> ⚠️ Never commit your `.env` file or credentials to GitHub.

---

# 📌 Database Configuration

This project uses **Aiven Cloud MySQL**.

Copy the following details from your Aiven dashboard:

| Variable | Description |
|----------|-------------|
| DB_HOST | Database Host |
| DB_PORT | Database Port |
| DB_NAME | Database Name |
| DB_USER | Database Username |
| DB_PASSWORD | Database Password |

---

# 🔑 Generate SECRET_KEY

Run the following command:

```python
import secrets
print(secrets.token_hex(32))
```

Example:

```env
SECRET_KEY=your_generated_secret_key
```

---

# ▶️ Run the Application

```bash
python app.py
```

Application runs at:

```
http://127.0.0.1:5000
```

---

# 🧪 Usage

## New Users

Visit

```
/signup
```

Create a new account using your email and password.

---

## Existing Users

1. Login using Email and Password.
2. Receive a 6-digit OTP via email.
3. Enter the OTP.
4. Access the dashboard based on your role.

---

# 👥 Demo Accounts

## Admin

```
Email: admin@example.com
Password: Admin@123
```

---

## Store Owner

Store Owners are created by the Admin.

Login using the credentials assigned by the administrator.

---

## User

Create a new account via:

```
/signup
```

---

# 🌐 Deployment

- Render (Web Application)
- Aiven Cloud MySQL (Database)
- Gmail SMTP (Email OTP Service)

---

# 🚀 Future Enhancements

- Email Verification During Signup
- Forgot Password via Email
- Password Reset using Secure Token
- Store Images
- Rating Analytics Dashboard
- REST API
- Docker Support
- JWT Authentication
- Responsive UI Improvements
- Admin Activity Logs

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is developed for educational and learning purposes.

---

# 👩‍💻 Author

**Chandana N L**

**GitHub**

https://github.com/Chandananl15

**LinkedIn**

https://www.linkedin.com/in/chandu15/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
