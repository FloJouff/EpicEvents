from crm.database import Session
from crm.models import User
from argon2 import PasswordHasher
from crm.views.user_view import UserView
from crm.controllers.permissions import requires_permission
import sentry_sdk

ph = PasswordHasher()


@requires_permission("create_user")
def create_user(
    name, firstname, email, password, role_id, current_user_role_id
):
    """Create a new user

    Args:
        name (str): new user's name
        firstname (str): new user's firstname
        email (str): new user's email
        password (str): new user's password
        role_id (int): new user's role_id
        current_user_role_id (int): role of connected user

    """
    session = Session()
    try:

        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            UserView.show_user_already_exists_error_message()
            return False

        hashed_password = ph.hash(password)

        new_user = User(
            name=name,
            firstname=firstname,
            email=email,
            password=hashed_password,
            role_id=role_id,
        )

        session.add(new_user)
        session.commit()
        UserView.show_create_user_success()
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"User created : {name}", level="info")
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"Error during registration: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


def view_users():
    """Query to get all users in database"""
    session = Session()
    user_list = session.query(User).all()
    UserView.display_user_list(user_list)


@requires_permission("update_user")
def update_user(
    user_id, current_user_role_id, name=None, firstname=None, email=None, password=None
):
    """Update existing user

    Args:
        user_id (int): user id to be updated
        current_user_role_id (int): role of connected user
        name (str, optional): new user's name. Defaults to None.
        firstname (str, optional): new user firstname. Defaults to None.
        email (str, optional): new user email. Defaults to None.
        password (str, optional): new user password. Defaults to None.

    Returns:
        _type_: _description_
    """
    session = Session()
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            UserView.show_no_user_error_message()
            return False
        if name:
            user.name = name
        if firstname:
            user.firstname = firstname
        if email:
            user.email = email
        if password:
            user.password = ph.hash(password)

        session.commit()
        UserView.show_update_user_success()
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"User updated : {name}", level="info")
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"Error updating user: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


def change_password(user_id, old_password, new_password):
    """function for changing the user's password

    Args:
        user_id (int): connected user
        old_password (str): old_password
        new_password (str): new_password


    """
    session = Session()
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            UserView.show_no_user_error_message()
            return False

        if not user.check_password(old_password):
            UserView.show_invalid_old_password()
            return False

        user.password = ph.hash(new_password)
        session.commit()
        UserView.show_password_change_successfully()
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"Error updating user's password: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("delete_user")
def delete_user(user_id, current_user_role_id):
    """function for deleting a user

    Args:
        user_id (int): user to be deleted
        current_user_role_id (int): role of connected user

    """
    session = Session()
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            UserView.show_no_user_error_message()
            return False
        session.delete(user)
        session.commit()
        UserView.show_delete_success_message(user_id)
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"User deleted : {user_id}", level="info")
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "user")
        sentry_sdk.capture_message(f"Error deleting user: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()
