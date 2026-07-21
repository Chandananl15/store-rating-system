from flask_mail import Mail, Message

mail = Mail()


def send_otp_email(recipient, otp):
    subject = "Store Rating System - Login Verification"

    body = f"""
Hello,

Your One-Time Password (OTP) for logging in to the Store Rating System is:

{otp}

This OTP is valid for 5 minutes.

If you did not request this login, please ignore this email.

Regards,
Store Rating System
"""

    msg = Message(
        subject=subject,
        recipients=[recipient],
        body=body
    )

    mail.send(msg)