from sqlalchemy import ForeignKey, Column, String, Integer
from crm.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(65))
    firstname = Column("fisrtname", String(65))
    email = Column("email", String(255), unique=True)
    password = Column("password", String(65))
    role = Column("role", ForeignKey("roles.role_id", ondelete="SET NULL"))

    def __init__(self, user_id, name, firstname, email, password, role):
        """Player constructor

        Args:
            user_id (int): user.id
            name (str): user's name
            first_name (str): user's first_name
            email (str): player's eamil
            password (str): player's password
            role (str): player's role
        """
        self.user_id = user_id
        self.name = name
        self.firstname = firstname
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User: {self.name} {self.firstname}"
