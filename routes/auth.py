from flask import Blueprint, render_template, request, redirect, flash, session 

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import login_user, logout_user

from models import db
from models.user import User

from services.email_service import send_otp_email
from services.otp_service import (
    generate_otp,
    save_otp,
    verify_otp,
    clear_otp,
)

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

        # Generate OTP
        otp = generate_otp()

        # Save OTP in session
        save_otp(user.id, otp)

        # Store user temporarily
        session["pending_user_id"] = user.id

        # Send OTP Email
        send_otp_email(user.email, otp)

        flash("OTP sent to your registered email.", "success")

        return redirect("/verify-otp")

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


@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp_page():

    pending_user_id = session.get("pending_user_id")

    if not pending_user_id:
        flash("Please login first.", "warning")
        return redirect("/login")

    user = User.query.get(pending_user_id)

    if request.method == "POST":

        entered_otp = request.form["otp"]

        is_valid, message = verify_otp(user.id, entered_otp)

        if not is_valid:
            flash(message, "danger")
            return redirect("/verify-otp")

        session.pop("pending_user_id", None)

        login_user(user)

        flash("Login successful!", "success")

        if user.role == ADMIN:
            return redirect("/admin/dashboard")

        elif user.role == OWNER:
            return redirect("/owner/dashboard")

        else:
            return redirect("/user/dashboard")

    return render_template("verify_otp.html")


@auth_bp.route("/resend-otp")
def resend_otp():

    pending_user_id = session.get("pending_user_id")

    if not pending_user_id:
        flash("Please login first.", "warning")
        return redirect("/login")

    user = User.query.get(pending_user_id)

    clear_otp()

    otp = generate_otp()

    save_otp(user.id, otp)

    send_otp_email(user.email, otp)

    flash("A new OTP has been sent to your email.", "success")

    return redirect("/verify-otp")

# ==========================
# Logout
# ==========================

@auth_bp.route("/logout")
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect("/login")