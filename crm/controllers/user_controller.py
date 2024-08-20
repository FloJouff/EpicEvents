# from crm.controllers.auth_controller import authenticate, authorize
from crm.database import Session
from crm.models import User
from argon2 import PasswordHasher

# from argon2.exceptions import VerifyMismatchError
from crm.controllers.permissions import requires_permission

ph = PasswordHasher()


# class UserController:
#     def login(self, email, password):
#         token = authenticate(email, password)
#         if token:
#             # Retourner le token ou l'envoyer à la vue
#             return token
#         else:
#             raise Exception("Authentication failed")

#     def secure_action(self, token):
#         if authorize(token, required_role="gestion"):
#             # Effectue l'action sécurisée
#             pass
#         else:
#             raise Exception("This user is not authorized to see this")


@requires_permission("create_user")
def create_user(
    name, firstname, email, password, role_id, current_user_role_id
):
    session = Session()
    try:

        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            print("This user already exists.")
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
        print("User registered successfully.")
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
    for user in user_list:
        print(f"Users list : {user}")


def update_user(user_id, name=None, firstname=None, email=None, password=None):
    session = Session()
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            print("User not found.")
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
        print("User updated successfully.")
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
            print("User not found.")
            return False

        if not user.check_password(old_password):
            print("Incorrect old password.")
            return False

        user.password = ph.hash(new_password)
        session.commit()
        print("Password updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating user's password: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def delete_user(user_id):
    session = Session
    try:
        user = session.query(User).fiter_by(user_id=user_id).first()
        if not user:
            print(f"User with id {user_id} not found")
            return False
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} has been deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        session.rollback()
        return False
    finally:
        session.close()
