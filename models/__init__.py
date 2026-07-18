from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.store import Store
from models.rating import Rating