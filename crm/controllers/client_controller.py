from crm.database import Session
from crm.models import Client
from datetime import datetime

from crm.controllers.permissions import requires_permission


def view_client():
    session = Session()
    client_list = session.query(Client).all()
    for client in client_list:
        print(f"Liste des clients : {client}")


def view_user_clients(user_id):
    session = Session()
    user_client_list = (
        session.query(Client).filter_by(contact_id=user_id).all()
    )
    for client in user_client_list:
        print(f"Liste des évènements : {client}")


@requires_permission("create_client")
def create_client(name, firstname, email, phone, company, user_id):
    session = Session()
    try:
        # Vérification si l'utilisateur existe déjà
        existing_client = session.query(Client).filter_by(name=name).first()
        if existing_client:
            print("This client already exists.")
            return False

        # Création d'un nouvel utilisateur
        new_client = Client(
            name=name,
            firstname=firstname,
            email=email,
            phone=phone,
            company=company,
            creation_date=datetime.now(),
            last_contact_date=datetime.now(),
            contact_id=user_id,
        )

        session.add(new_client)
        session.commit()
        print("client registered successfully.")
        return True
    except Exception as e:
        print(f"Error during registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()
