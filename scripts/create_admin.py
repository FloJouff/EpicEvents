from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from crm.models.user import User
from crm.models.role import Role
from argon2 import PasswordHasher

load_dotenv()

db_url = f"mysql+mysqlconnector://{os.getenv("DB_USER")}:{
    os.getenv("DB_PASSWORD")}@{
        os.getenv("DB_HOST")}:{
            os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


def create_admin(name, firstname, email, password):
    ph = PasswordHasher()

    admin_role = session.query(Role).filter_by(role_id=4).first()
    if not admin_role:
        admin_role = Role(role_id=4, role_name='ADMIN')
        session.add(admin_role)
        session.commit()

    admin_user = User(
        name=name,
        firstname=firstname,
        email=email,
        password=ph.hash(password),
        role_id=admin_role.role_id
    )

    session.add(admin_user)
    session.commit()
    print(f"Administrateur {name} créé avec succès !")


if __name__ == "__main__":
    name = input("Input admin name : ")
    firstname = input("Input admin firstname : ")
    email = input("Input admin Email : ")
    password = input("Input Admin password : ")

    create_admin(name, firstname, email, password)
