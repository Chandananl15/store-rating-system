import random
from datetime import datetime, timedelta
from flask import session


OTP_EXPIRY_MINUTES = 5


def generate_otp():
    """Generate a random 6-digit OTP."""
    return str(random.randint(100000, 999999))

def save_otp(user_id, otp):

    session["otp"] = otp
    session["otp_user_id"] = user_id
    session["otp_attempts"] = 0
    session["otp_expiry"] = (
        datetime.now() + timedelta(minutes=OTP_EXPIRY_MINUTES)
    ).timestamp()


def verify_otp(user_id, entered_otp):
    """Verify OTP."""

    stored_otp = session.get("otp")
    stored_user = session.get("otp_user_id")
    expiry = session.get("otp_expiry")

    if not stored_otp or not expiry:
        return False, "OTP not found."

    if stored_user != user_id:
        return False, "Invalid OTP."

    if datetime.now().timestamp() > expiry:
        clear_otp()
        return False, "OTP has expired."

    attempts = session.get("otp_attempts", 0)

    if attempts >= 3:
        clear_otp()
        return False, "Maximum OTP attempts exceeded."

    if entered_otp != stored_otp:
        session["otp_attempts"] = attempts + 1
        return False, "Incorrect OTP."

    clear_otp()
    return True, "OTP verified successfully."

def clear_otp():

    session.pop("otp", None)
    session.pop("otp_user_id", None)
    session.pop("otp_expiry", None)
    session.pop("otp_attempts", None)