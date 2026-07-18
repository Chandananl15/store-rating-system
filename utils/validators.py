import re


def validate_name(name):

    if len(name) < 20 or len(name) > 60:
        return "Name must be between 20 and 60 characters."

    return None


def validate_email(email):

    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

    if not re.match(pattern, email):
        return "Invalid email format."

    return None


def validate_password(password):

    if len(password) < 8 or len(password) > 16:
        return "Password must be 8 to 16 characters."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return None


def validate_address(address):

    if len(address) > 400:
        return "Address cannot exceed 400 characters."

    return None