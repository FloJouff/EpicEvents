from sqlalchemy import ForeignKey, Column, String, Integer
from crm.models import Base
from sqlalchemy.orm import relationship

from argon2 import PasswordHasher, exceptions

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
    # events = relationship("User", back_populates="user")

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
        # Si le mot de passe est déjà haché, ne pas le hacher à nouveau
        if not password.startswith("$argon2id$"):
            self.hash_password(password)
        else:
            self.password = password

    def hash_password(self, password):
        """Hash the password using Argon2."""
        self.password = ph.hash(password)

    def check_password(self, password):
        """Vérifie que le mot de passe correspond au hash"""
        try:
            return ph.verify(self.password, password)
        except exceptions.VerifyMismatchError:
            return False

    def __repr__(self):
        return f"User: id: {self.user_id}, name: {
            self.name}, firstname: {
                self.firstname}, email: {
                    self.email}, role: {self.role_id}"


# INSERT INTO users (`name`, `firstname`, `email`, `role_id`)
# VALUES ('Admin', 'admin', 'admin@test.com', '4');
