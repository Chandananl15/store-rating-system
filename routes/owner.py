from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.store import Store
from utils.decorators import owner_required

owner_bp = Blueprint("owner", __name__)


@owner_bp.route("/owner/dashboard")
@login_required
@owner_required
def dashboard():

    store = Store.query.filter_by(owner_id=current_user.id).first()

    average_rating = "No Ratings"

    if store and store.ratings:

        average_rating = round(
            sum(r.rating for r in store.ratings) /
            len(store.ratings),
            1
        )

    return render_template(
        "owner/dashboard.html",
        store=store,
        average_rating=average_rating
    )