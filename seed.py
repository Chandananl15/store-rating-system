from werkzeug.security import generate_password_hash

from app import create_app
from models import db
from models.user import User
from models.store import Store


app = create_app()


with app.app_context():

    # ------------------------
    # Create tables
    # ------------------------
    db.create_all()

    # ------------------------
    # Admin
    # ------------------------
    admin = User.query.filter_by(email="admin@example.com").first()

    if not admin:
        admin = User(
            name="System Administrator",
            email="admin@example.com",
            password=generate_password_hash("Admin@123"),
            address="Bangalore",
            role="admin"
        )

        db.session.add(admin)

    # ------------------------
    # Store Owner
    # ------------------------
    owner = User.query.filter_by(email="owner@example.com").first()

    if not owner:
        owner = User(
            name="Fresh Mart Store Owner",
            email="owner@example.com",
            password=generate_password_hash("Owner@123"),
            address="Bangalore",
            role="owner"
        )

        db.session.add(owner)
        db.session.commit()

    else:
        db.session.commit()

    # ------------------------
    # Store
    # ------------------------
    store = Store.query.filter_by(email="freshmart@example.com").first()

    if not store:

        owner = User.query.filter_by(email="owner@example.com").first()

        store = Store(
            name="Fresh Mart",
            email="freshmart@example.com",
            address="Bangalore",
            owner_id=owner.id
        )

        db.session.add(store)

    db.session.commit()

    print("Database seeded successfully!")