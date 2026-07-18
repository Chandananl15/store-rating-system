from models import db


class Store(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    address = db.Column(db.String(400), nullable=False)

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    owner = db.relationship(
        "User",
        back_populates="stores"
    )

    ratings = db.relationship(
        "Rating",
        back_populates="store"
    )

    def __repr__(self):
        return f"<Store {self.name}>"