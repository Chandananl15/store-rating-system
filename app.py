from flask import Flask, redirect
from flask_login import LoginManager

from config import Config
from models import db
from models.user import User

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.user import user_bp
from routes.owner import owner_bp

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(owner_bp)

    # Home route
    @app.route("/")
    def home():
        return redirect("/login")

    return app


# Create the Flask application
app = create_app()

# Create database tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)