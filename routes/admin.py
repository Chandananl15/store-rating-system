from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from constants.roles import USER, OWNER

from utils.decorators import admin_required
from utils.validators import (
    validate_name,
    validate_email,
    validate_password,
    validate_address,
)

from models import db
from models.user import User
from models.store import Store
from models.rating import Rating


admin_bp = Blueprint("admin", __name__)


# ==========================
# Dashboard
# ==========================

@admin_bp.route("/admin/dashboard")
@login_required
@admin_required
def dashboard():

    total_users = User.query.count()
    total_stores = Store.query.count()
    total_ratings = Rating.query.count()

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        total_stores=total_stores,
        total_ratings=total_ratings,
    )


# ==========================
# Add User
# ==========================

@admin_bp.route("/admin/add-user", methods=["GET", "POST"])
@login_required
@admin_required

def add_user():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        address = request.form["address"]
        role = request.form["role"]

        if role.lower() == "user":
            role = USER

        elif role.lower() == "owner":
            role = OWNER

        error = validate_name(name)
        if error:
            return render_template(
                "admin/add_user.html",
                error=error
            )

        error = validate_email(email)
        if error:
            return render_template(
                "admin/add_user.html",
                error=error
            )

        error = validate_password(password)
        if error:
            return render_template(
                "admin/add_user.html",
                error=error
            )

        error = validate_address(address)
        if error:
            return render_template(
                "admin/add_user.html",
                error=error
            )

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return render_template(
                "admin/add_user.html",
                error="Email already exists."
            )

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            address=address,
            role=role,
        )

        db.session.add(user)
        db.session.commit()

        flash("User created successfully!", "success")

        return redirect("/admin/dashboard")

    return render_template("admin/add_user.html")


# ==========================
# View Users
# ==========================

@admin_bp.route("/admin/users")
@login_required
@admin_required
def users():

    search = request.args.get("search", "")
    sort = request.args.get("sort", "name")
    order = request.args.get("order", "asc")

    users = User.query

    if search:

        users = users.filter(

            (User.name.ilike(f"%{search}%")) |
            (User.email.ilike(f"%{search}%")) |
            (User.address.ilike(f"%{search}%")) |
            (User.role.ilike(f"%{search}%"))

        )

    columns = {
        "name": User.name,
        "email": User.email,
        "address": User.address,
        "role": User.role
    }

    sort_column = columns.get(sort, User.name)

    if order == "desc":
        users = users.order_by(sort_column.desc())
    else:
        users = users.order_by(sort_column.asc())

    users = users.all()

    return render_template(
        "admin/users.html",
        users=users,
        search=search,
        sort=sort,
        order=order
    )

# ==========================
# User Details
# ==========================

@admin_bp.route("/admin/user/<int:user_id>")
@login_required
@admin_required
def user_details(user_id):

    user = User.query.get_or_404(user_id)

    store = None
    average_rating = None

    if user.role == OWNER and user.stores:

        store = user.stores[0]

        if store.ratings:

            average_rating = round(
                sum(r.rating for r in store.ratings) /
                len(store.ratings),
                1
            )

        else:

            average_rating = "No Ratings"

    return render_template(
        "admin/user_details.html",
        user=user,
        store=store,
        average_rating=average_rating
    )

@admin_bp.route("/admin/user/<int:user_id>/delete")
@login_required
@admin_required
def delete_user(user_id):

    user = User.query.get_or_404(user_id)

    # Delete user's ratings
    Rating.query.filter_by(user_id=user.id).delete()

    # Delete stores owned by this user
    stores = Store.query.filter_by(owner_id=user.id).all()

    for store in stores:
        Rating.query.filter_by(store_id=store.id).delete()
        db.session.delete(store)

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully!", "success")

    return redirect("/admin/users")

# ==========================
# Add Store
# ==========================

@admin_bp.route("/admin/add-store", methods=["GET", "POST"])
@login_required
@admin_required
def add_store():

    owners = User.query.filter_by(role=OWNER).all()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        address = request.form["address"]
        owner_id = request.form["owner_id"]

        existing_store = Store.query.filter_by(email=email).first()

        if existing_store:
            flash("Store email already exists.", "danger")
            return redirect("/admin/add-store")

        owner_store = Store.query.filter_by(owner_id=owner_id).first()

        if owner_store:
            flash("This Store Owner already owns a store.", "danger")
            return redirect("/admin/add-store")

        store = Store(
            name=name,
            email=email,
            address=address,
            owner_id=owner_id
        )

        db.session.add(store)
        db.session.commit()

        flash("Store created successfully!", "success")

        return redirect("/admin/dashboard")

    return render_template(
        "admin/add_store.html",
        owners=owners
    )


# ==========================
# View Stores
# ==========================

@admin_bp.route("/admin/stores")
@login_required
@admin_required
def stores():

    search = request.args.get("search", "")
    sort = request.args.get("sort", "name")
    order = request.args.get("order", "asc")

    stores = Store.query

    if search:

        stores = stores.filter(

            (Store.name.ilike(f"%{search}%")) |
            (Store.email.ilike(f"%{search}%")) |
            (Store.address.ilike(f"%{search}%"))

        )

    columns = {
        "name": Store.name,
        "email": Store.email,
        "address": Store.address
    }

    sort_column = columns.get(sort, Store.name)

    if order == "desc":
        stores = stores.order_by(sort_column.desc())
    else:
        stores = stores.order_by(sort_column.asc())

    stores = stores.all()

    store_data = []

    for store in stores:

        if store.ratings:
            average_rating = round(
                sum(r.rating for r in store.ratings) /
                len(store.ratings),
                1
            )
        else:
            average_rating = "No Ratings"

        store_data.append({
            "id": store.id,
            "name": store.name,
            "email": store.email,
            "address": store.address,
            "owner": store.owner.name,
            "average_rating": average_rating
        })

    return render_template(
        "admin/stores.html",
        stores=store_data,
        search=search,
        sort=sort,
        order=order
    )

# ==========================
# Store Details
# ==========================

@admin_bp.route("/admin/store/<int:store_id>")
@login_required
@admin_required
def store_details(store_id):

    store = Store.query.get_or_404(store_id)

    if store.ratings:

        average_rating = round(
            sum(r.rating for r in store.ratings) /
            len(store.ratings),
            1
        )

    else:

        average_rating = "No Ratings"

    return render_template(
        "admin/store_details.html",
        store=store,
        average_rating=average_rating
    )

@admin_bp.route("/admin/store/<int:store_id>/delete")
@login_required
@admin_required
def delete_store(store_id):

    store = Store.query.get_or_404(store_id)

    # Delete all ratings for this store
    Rating.query.filter_by(store_id=store.id).delete()

    db.session.delete(store)
    db.session.commit()

    flash("Store deleted successfully!", "success")

    return redirect("/admin/stores")