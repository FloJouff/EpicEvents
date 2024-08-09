from sqlalchemy import ForeignKey, Column, String, Integer
from crm.database import Base
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from argon2 import PasswordHasher, exceptions

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
ph = PasswordHasher()

class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(65))
    firstname = Column("fisrtname", String(65))
    email = Column("email", String(255), unique=True)
    password = Column("password", String(65))
    role_id = Column(
        "role_id", ForeignKey("roles.role_id", ondelete="SET NULL")
    )

    role = relationship("Role", back_populates="users")

    def __init__(self, name, firstname, email, password, role):
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
        self.role = role
        # Si le mot de passe est déjà haché, ne pas le hacher à nouveau
        if not password.startswith("$argon2id$"):
            self.hash_password(password)
        else:
            self.password_hash = password

    def hash_password(self, password):
        """Hash the password using Argon2."""
        self.password_hash = ph.hash(password)

    def check_password(self, password):
        """Vérifie que le mot de passe correspond au hash"""
        try:
            return ph.verify(self.password_hash, password)
        except exceptions.VerifyMismatchError:
            return False

    def check_permission(self, action):
        """Check if the user has permission to perform an action based on their role."""
        return self.role.has_permission(action)

    def __repr__(self):
        return f"User: {self.name} {self.firstname}"
