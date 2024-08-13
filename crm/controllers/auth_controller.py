import jwt
import datetime
from crm.database import Session
from crm.models.user import User
from crm.models.role import Role
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os

# Utiliser un secret sécurisé pour les JWT
JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # token expire after 1h

# Initialiser l'outil de hachage des mots de passe
ph = PasswordHasher()


def authenticate(email, password):
    """User authentication and return token if user is authentified"""
    session = Session()
    user = session.query(User).filter_by(email=email).first()

    if user:
        try:
            ph.verify(user.password, password)
            payload = {
                "user_id": user.user_id,
                "role": user.role_id,
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            }
            token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            return token
        except VerifyMismatchError:
            return None
    return None


def authorize(token, required_role=None):
    """Check if a user has authorization to perform an action"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if required_role and payload["role"] != required_role:
            return False
        return True
    except jwt.ExpiredSignatureError:
        print("the token has expired. Please Re connect")
        return False
    except jwt.InvalidTokenError:
        print("Invalide token.")
        return False


def register_user(username, password):
    session = Session()
    try:
        # Vérification si l'utilisateur existe déjà
        existing_user = (
            session.query(User).filter_by(username=username).first()
        )
        if existing_user:
            print("Cet utilisateur existe déjà.")
            return False

        # Hachage du mot de passe avec Argon2
        password_hash = ph.hash(password)

        # Création d'un nouvel utilisateur
        new_user = User(username=username, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        print("Utilisateur enregistré avec succès.")
        return True
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")
        session.rollback()
        return False
    finally:
        session.close()
