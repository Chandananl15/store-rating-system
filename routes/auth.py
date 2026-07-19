from flask import Blueprint, render_template, request, redirect, flash

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import login_user, logout_user

from models import db
from models.user import User

from constants.roles import ADMIN, OWNER, USER

from utils.validators import (
    validate_name,
    validate_email,
    validate_password,
    validate_address,
)


auth_bp = Blueprint("auth", __name__)



# ==========================
# Login
# ==========================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Invalid Email", "danger")
            return redirect("/login")

        if not check_password_hash(user.password, password):
            flash("Invalid Password", "danger")
            return redirect("/login")

        login_user(user)

        if user.role == ADMIN:
            return redirect("/admin/dashboard")

        elif user.role == OWNER:
            return redirect("/owner/dashboard")

        else:
            return redirect("/user/dashboard")

    return render_template("login.html")


# ==========================
# Signup
# ==========================

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        address = request.form["address"]

        error = validate_name(name)
        if error:
            flash(error, "danger")
            return redirect("/signup")

        error = validate_email(email)
        if error:
            flash(error, "danger")
            return redirect("/signup")

        error = validate_password(password)
        if error:
            flash(error, "danger")
            return redirect("/signup")

        error = validate_address(address)
        if error:
            flash(error, "danger")
            return redirect("/signup")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists.", "danger")
            return redirect("/signup")

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            address=address,
            role=USER
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")

        return redirect("/login")

    return render_template("signup.html")


# ==========================
# Logout
# ==========================

@auth_bp.route("/logout")
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect("/login")