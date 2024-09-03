from crm.database import Session
from crm.models import Client
from datetime import datetime
from crm.views import client_view
from crm.controllers.permissions import requires_permission
import Constantes.constantes as constante
import sentry_sdk


def view_client():
    session = Session()
    client_list = session.query(Client).all()
    client_view.ClientView.display_client_list(client_list)


@requires_permission("create_client")
def create_client(
    name, firstname, email, phone, company, contact_id, current_user_role_id
):
    session = Session()
    try:
        existing_client = session.query(Client).filter_by(email=email).first()
        if existing_client:
            client_view.ClientView.show_client_error_message()
            return False

        new_client = Client(
            name=name,
            firstname=firstname,
            email=email,
            phone=phone,
            company=company,
            creation_date=datetime.now(),
            last_contact_date=datetime.now(),
            contact_id=contact_id,
        )

        session.add(new_client)
        session.commit()
        client_view.ClientView.show_create_client_success_message()
        return True
    except Exception as e:
        sentry_sdk.capture_message(f"Error during registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def view_own_client(user_id):
    session = Session()
    user_own_client_list = session.query(Client).filter_by(contact_id=user_id).all()
    client_view.ClientView.display_client_list(user_own_client_list)


@requires_permission("update_client")
def update_client(
    user_id,
    client_id,
    current_user_role_id,
    name=None,
    firstname=None,
    email=None,
    phone=None,
    last_contact_date=None,
    contact_id=None,
):
    session = Session()
    try:
        client = session.query(Client).filter_by(client_id=client_id).first()
        if not client:
            client_view.ClientView.show_client_error_message()
            return False
        if name:
            client.name = name
        if firstname:
            client.firstname = firstname
        if email:
            client.email = email
        if phone:
            client.phone = phone
        if last_contact_date:
            client.last_contact_date = last_contact_date
        if contact_id:
            client.contact_id = contact_id

        session.commit()
        client_view.ClientView.show_update_client_success_message()
        return True
    except Exception as e:
        sentry_sdk.capture_message(f"Error updating user: {e}")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("update_client_sales")
def update_client_sales(user_id, client_id, contact_id, current_user_role_id):
    session = Session()
    try:
        client = session.query(Client).filter_by(client_id=client_id).first()
        if not client:
            client_view.ClientView.show_client_error_message()
            return False
        client.contact_id = contact_id

        session.commit()
        client_view.ClientView.show_update_client_contact_id()
        return True
    except Exception as e:
        sentry_sdk.capture_message(f"Error updating user: {e}")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("delete_client")
def delete_client(client_id, current_user_role_id):
    session = Session()
    try:
        client = session.query(Client).filter_by(client_id=client_id).first()
        if not client:
            client_view.ClientView.show_client_error_message()
            return False
        session.delete(client)
        session.commit()
        client_view.ClientView.show_delete_client_success_message()
        return True
    except Exception as e:
        sentry_sdk.capture_message(f"Error deleting client: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def update_client_menu(user_id, client_id, current_user_role_id):
    while True:
        update_choice = client_view.ClientView.show_update_client_menu()
        if update_choice == constante.CLIENT_UPDATE_NAME:
            new_name = client_view.ClientView.get_new_client_name()
            update_client(user_id, client_id, current_user_role_id, name=new_name)
        elif update_choice == constante.CLIENT_UPDATE_FIRSTNAME:
            new_firstname = client_view.ClientView.get_new_client_firstname()
            update_client(
                user_id, client_id, current_user_role_id, firstname=new_firstname
            )
        elif update_choice == constante.CLIENT_UPDATE_EMAIL:
            new_email = client_view.ClientView.get_new_client_email()
            update_client(user_id, client_id, current_user_role_id, email=new_email)
        elif update_choice == constante.CLIENT_UPDATE_PHONE:
            new_phone = client_view.ClientView.get_new_client_phone()
            update_client(user_id, client_id, current_user_role_id, phone=new_phone)
        elif update_choice == constante.CLIENT_UPDATE_COMPANY:
            new_company = client_view.ClientView.get_new_client_company()
            update_client(user_id, client_id, current_user_role_id, company=new_company)
        elif update_choice == constante.CLIENT_UPDATE_LAST_CONTACT:
            new_last_contact = client_view.ClientView.get_new_client_last_contact()
            update_client(
                user_id,
                client_id,
                current_user_role_id,
                last_contact_date=new_last_contact,
            )
        elif update_choice == "0":
            break
