from crm.database import Session
from crm.models import Event

# from crm.controllers.permissions import requires_permission
from crm.controllers.permissions import requires_permission


def view_event():
    session = Session()
    event_list = session.query(Event).all()
    for event in event_list:
        print(f"Liste des évènements : {event}")


def view_user_event(user_id):
    session = Session()
    user_event_list = session.query(Event).filter_by(support_id=user_id).all()
    for event in user_event_list:
        print(f"Liste des évènements : {event}")


@requires_permission("create_event")
def create_event(
    client_id, start_date, end_date, contract_id, attendees, location
):
    session = Session()
    try:
        # Vérification si l'utilisateur existe déjà
        existing_event = (
            session.query(Event).filter_by(contract_id=contract_id).first()
        )
        if existing_event:
            print("This client already exists.")
            return False

        # Création d'un nouvel utilisateur
        new_event = Event(
            client_id=client_id,
            start_date=start_date,
            end_date=end_date,
            contract_id=contract_id,
            attendees=attendees,
            location=location,
        )

        session.add(new_event)
        session.commit()
        print("Event created successfully.")
        return True
    except Exception as e:
        print(f"Error during registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()
