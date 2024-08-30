import re
from datetime import datetime
from rich import print


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    else:
        print("[bold red]Invalid email[/bold red]")


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        print("[bold red]Incorrect date format (YYYY-MM-DD)[/bold red]")
        return False


def validate_phone_number(phone_number):
    phone_regex = r"^\d{10}$"
    if re.match(phone_regex, phone_number):
        return True
    else:
        print("[bold red]Invalid phone number, must be 10 digits[/bold red]")


def validate_password(password):
    if len(password) >= 8:
        return True
    # if not re.search(r"[A-Z]", password):
    #     return False
    # if not re.search(r"[a-z]", password):
    #     return False
    # if not re.search(r"[0-9]", password):
    #     return False


def validate_name(name):
    name_regex = r"^[A-Za-z\s-]{2,50}$"
    if re.match(name_regex, name):
        return True
    else:
        print(
            "[bold red]Invalid name. Must be 2-50 characters long and contain only letters, spaces, or hyphens.[/bold red]"
        )
        return False


def validate_id(id_input):
    id_regex = r"^\d+$"
    if re.match(id_regex, id_input):
        return True
    else:
        print("[bold red]Invalid ID. Must contain only digits.[/bold red]")
        return False
