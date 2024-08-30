from crm.database import Session
from crm.models import User
from argon2 import PasswordHasher
from crm.views.user_view import UserView
from crm.controllers.permissions import requires_permission

ph = PasswordHasher()


@requires_permission("create_user")
def create_user(
    name, firstname, email, password, role_id, current_user_role_id
):
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
        return True
    except Exception as e:
        print(f"Error during registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def view_users():
    session = Session()
    user_list = session.query(User).all()
    UserView.display_user_list(user_list)


@requires_permission("update_user")
def update_user(
    user_id, current_user_role_id, name=None, firstname=None, email=None, password=None
):
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
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def change_password(user_id, old_password, new_password):
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
        print(f"Error updating user's password: {e}")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("delete_user")
def delete_user(user_id, current_user_role_id):
    session = Session()
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            UserView.show_no_user_error_message()
            return False
        session.delete(user)
        session.commit()
        UserView.show_delete_success_message(user_id)
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        session.rollback()
        return False
    finally:
        session.close()
