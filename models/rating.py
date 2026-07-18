from models import db


class Rating(db.Model):

    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    store_id = db.Column(
        db.Integer,
        db.ForeignKey("stores.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="ratings"
    )

    store = db.relationship(
        "Store",
        back_populates="ratings"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "store_id",
            name="unique_user_store_rating"
        ),
    )

    def __repr__(self):
        return f"<Rating {self.rating}>"