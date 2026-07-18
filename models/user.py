from models import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(60), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    address = db.Column(db.String(400), nullable=False)

    role = db.Column(db.String(20), nullable=False)

    # Relationship with Store
    stores = db.relationship(
        "Store",
        back_populates="owner"
    )

    # Relationship with Rating
    ratings = db.relationship(
        "Rating",
        back_populates="user"
    )

    def __repr__(self):
        return f"<User {self.name}>"

