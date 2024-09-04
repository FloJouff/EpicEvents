from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
import os
from sqlalchemy.orm import declarative_base

Base = declarative_base()

load_dotenv()

db_url = f"mysql+mysqlconnector://{os.getenv("DB_USER")}:{
    os.getenv("DB_PASSWORD")}@{
        os.getenv("DB_HOST")}:{
            os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


DEFAULT_ROLES = [
    {"role_id": 1, "role_name": "GESTION"},
    {"role_id": 2, "role_name": "COMMERCIAL"},
    {"role_id": 3, "role_name": "SUPPORT"},
    {"role_id": 4, "role_name": "ADMIN"}
]


class Role(Base):
    __tablename__ = "roles"

    role_id = Column("role_id", Integer, primary_key=True)
    role = Column(
        "role", Enum("gestion", "commercial", "support", "admin"), unique=True
    )
    users = relationship("User", back_populates="role")

    def __init__(self, role_id, role):
        """Role constructor

        Args:
            role_id(int):
            role (Enum): event's contract's id


        """
        self.role_id = role_id
        self.role = role

    def __repr__(self):
        return f"Role: {self.role}"


def initialize_roles():
    """Initialize roles in database"""
    for role in DEFAULT_ROLES:
        existing_role = session.query(Role).filter_by(role_id=role["role_id"]).first()
        if not existing_role:
            new_role = Role(role_id=role["role_id"], role_name=role["role_name"])
            session.add(new_role)
            print(f"Role {role['role_name']} added.")
    session.commit()


if __name__ == "__main__":
    initialize_roles()
    print("Roles initialization done.")
