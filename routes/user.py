from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.store import Store
from utils.decorators import user_required

from flask import request, redirect, flash
from models import db
from models.rating import Rating

from flask import render_template, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash

from models import db
from models.user import User
from models.store import Store
from models.rating import Rating

from utils.decorators import user_required
from utils.validators import validate_password

from models import db
from flask_login import UserMixin

from . import user_bp

user_bp = Blueprint("user", __name__)


@user_bp.route("/user/dashboard")
@login_required
@user_required
def dashboard():

    return render_template("user/dashboard.html")


@user_bp.route("/user/stores")
@login_required
@user_required
def stores():

    search = request.args.get("search", "")

    stores = Store.query

    if search:

        stores = stores.filter(

            (Store.name.ilike(f"%{search}%")) |

            (Store.address.ilike(f"%{search}%"))

        )

    stores = stores.all()

    store_data = []

    for store in stores:

        # Overall Rating
        if store.ratings:
            overall_rating = round(
                sum(r.rating for r in store.ratings) / len(store.ratings),
                1
            )
        else:
            overall_rating = "No Ratings"

        # Current User Rating
        my_rating = Rating.query.filter_by(
            user_id=current_user.id,
            store_id=store.id
        ).first()

        if my_rating:
            user_rating = my_rating.rating
            action = "Update Rating"
        else:
            user_rating = "Not Rated"
            action = "Rate"

        store_data.append({

            "id": store.id,

            "name": store.name,

            "email": store.email,

            "address": store.address,

            "overall_rating": overall_rating,

            "user_rating": user_rating,

            "action": action

        })

    return render_template(
        "user/stores.html",
        stores=store_data
    )

@user_bp.route("/user/store/<int:store_id>")
@login_required
@user_required
def store_details(store_id):

    store = Store.query.get_or_404(store_id)

    if store.ratings:
        overall_rating = round(
            sum(r.rating for r in store.ratings) /
            len(store.ratings),
            1
        )
    else:
        overall_rating = "No Ratings"

    my_rating = Rating.query.filter_by(
        user_id=current_user.id,
        store_id=store.id
    ).first()

    if my_rating:
        user_rating = my_rating.rating
        action = "Update Rating"
    else:
        user_rating = "Not Rated"
        action = "Rate Store"

    return render_template(
        "user/store_details.html",
        store=store,
        overall_rating=overall_rating,
        user_rating=user_rating,
        action=action
    )

@user_bp.route("/user/rate/<int:store_id>", methods=["GET", "POST"])
@login_required
@user_required
def rate_store(store_id):

    store = Store.query.get_or_404(store_id)

    existing_rating = Rating.query.filter_by(
        user_id=current_user.id,
        store_id=store.id
    ).first()

    if request.method == "POST":

        rating = int(request.form["rating"])

        if rating < 1 or rating > 5:
            flash("Rating must be between 1 and 5.", "danger")
            return redirect(f"/user/rate/{store.id}")

        if existing_rating:
            existing_rating.rating = rating
            flash("Rating updated successfully!", "success")

        else:
            new_rating = Rating(
                rating=rating,
                user_id=current_user.id,
                store_id=store.id
            )

            db.session.add(new_rating)
            flash("Rating submitted successfully!", "success")

        db.session.commit()

        return redirect("/user/stores")

    return render_template(
        "user/rate_store.html",
        store=store,
        existing_rating=existing_rating
    )

@user_bp.route("/user/change-password", methods=["GET", "POST"])
@login_required
@user_required
def change_password():

    if request.method == "POST":

        current_password = request.form["current_password"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        # Check current password
        if not check_password_hash(current_user.password, current_password):

            return render_template(
                "user/change_password.html",
                error="Current password is incorrect."
            )

        # Validate new password
        error = validate_password(new_password)

        if error:

            return render_template(
                "user/change_password.html",
                error=error
            )

        # Check confirmation
        if new_password != confirm_password:

            return render_template(
                "user/change_password.html",
                error="New passwords do not match."
            )

        # Update password
        # New password cannot be same as current password
        if check_password_hash(current_user.password, new_password):

            return render_template(
                "user/change_password.html",
                error="New password cannot be the same as current password."
            )

        # Check confirmation
        if new_password != confirm_password:

            return render_template(
                "user/change_password.html",
                error="New passwords do not match."
            )

        # Update password
        current_user.password = generate_password_hash(new_password)

        db.session.commit()

        flash("Password changed successfully!", "success")

        return redirect("/user/dashboard")

# Check confirmation
        if new_password != confirm_password:

            return render_template(
                "user/change_password.html",
                error="New passwords do not match."
            )

# Update password
        current_user.password = generate_password_hash(new_password)

    return render_template("user/change_password.html")

        