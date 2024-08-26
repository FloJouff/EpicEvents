import jwt
import datetime
from crm.database import Session
from crm.models import User
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os


JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXP_DELTA_SECONDS = 3600  # token expire after 1h


ph = PasswordHasher()


def authenticate(email, password):
    """User authentication and return token if user is authenticated"""
    session = Session()
    user = session.query(User).filter_by(email=email).first()

    if user:
        try:
            ph.verify(user.password, password)
            payload = {
                "user_id": user.user_id,
                "role": user.role_id,
                "exp": datetime.datetime.now()
                + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            }
            token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            print(f"Bienvenue {user.name} {user.firstname}")
            return token, user.role_id

        except VerifyMismatchError:
            return None, None
    return None, None


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

