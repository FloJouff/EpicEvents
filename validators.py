import re
from datetime import datetime


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    else:
        print("Invalid email")


def validate_date(date_text):
    if datetime.strptime(date_text, "%Y-%m-%d"):
        return True
    else:
        print("Incorrect date format (YYYY-MM-DD)")


def validate_phone_number(phone_number):
    phone_regex = r"^\d{10}$"
    if re.match(phone_regex, phone_number):
        return True
    else:
        print("Invalid phone number, must be 10 digits")


def validate_password(password):
    if len(password) >= 8:
        return True
    # if not re.search(r"[A-Z]", password):
    #     return False
    # if not re.search(r"[a-z]", password):
    #     return False
    # if not re.search(r"[0-9]", password):
    #     return False
