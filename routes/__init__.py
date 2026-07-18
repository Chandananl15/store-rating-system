from flask import Blueprint


auth_bp = Blueprint("auth", __name__)
admin_bp = Blueprint("admin", __name__)
user_bp = Blueprint("user", __name__)
owner_bp = Blueprint("owner", __name__)
