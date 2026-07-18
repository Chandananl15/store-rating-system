from functools import wraps

from flask_login import current_user
from flask import abort

from constants.roles import ADMIN, USER, OWNER

def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role != ADMIN:
            abort(403)

        return func(*args, **kwargs)

    return wrapper

from constants.roles import USER


def user_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role != USER:
            abort(403)

        return func(*args, **kwargs)

    return wrapper

from constants.roles import OWNER


def owner_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role != OWNER:
            abort(403)

        return func(*args, **kwargs)

    return wrapper