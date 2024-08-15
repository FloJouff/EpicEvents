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
        # Vérification si l'utilisateur existe déjà
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            print("This user already exists.")
            return False

        # Hachage du mot de passe avec Argon2
        hashed_password = ph.hash(password)

        # Création d'un nouvel utilisateur
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
