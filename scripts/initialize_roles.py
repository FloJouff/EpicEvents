from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crm.models.role import Role
from dotenv import load_dotenv
import os

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
