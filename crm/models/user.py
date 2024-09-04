from sqlalchemy import ForeignKey, Column, String, Integer
from crm.models import Base
from sqlalchemy.orm import relationship
from crm.views.user_view import UserView

from argon2 import PasswordHasher, exceptions

import jwt
import datetime
from argon2.exceptions import VerifyMismatchError
import os
from rich import print


JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXP_DELTA_SECONDS = 3600  # token expire after 1h


ph = PasswordHasher()


class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(65), nullable=False)
    firstname = Column("firstname", String(65), nullable=False)
    email = Column("email", String(255), unique=True, nullable=False)
    password = Column("password", String(255), nullable=False)
    role_id = Column(
        "role_id", ForeignKey("roles.role_id", ondelete="SET NULL")
    )

    role = relationship("Role", back_populates="users")

    def __init__(self, name, firstname, email, password, role_id):
        """Player constructor

        Args:
            user_id (int): user.id
            name (str): user's name
            first_name (str): user's first_name
            email (str): player's eamil
            password (str): player's password
            role (str): player's role
        """
        self.name = name
        self.firstname = firstname
        self.email = email
        self.role_id = role_id

        if not password.startswith("$argon2id$"):
            self.hash_password(password)
        else:
            self.password = password

    def hash_password(self, password):
        """Hash the password using Argon2."""
        self.password = ph.hash(password)

    def check_password(self, password):
        """Check if password matches the hash"""
        try:
            return ph.verify(self.password, password)
        except exceptions.VerifyMismatchError:
            return False

    def __repr__(self):
        return f"User: id: {self.user_id}, name: {
            self.name}, firstname: {
                self.firstname}, email: {
                    self.email}, role: {self.role_id}"

    @staticmethod
    def authenticate(email, password):
        """User authentication and return token if user is authenticated"""
        from crm.database import Session
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
                UserView.display_welcome_message(user.name, user.firstname)
                return token, user.role_id

            except VerifyMismatchError:
                return None, None
        return None, None

    @staticmethod
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

    @staticmethod
    def decode_token(token):
        decoded_token = jwt.decode(
                token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
            )
        return decoded_token
