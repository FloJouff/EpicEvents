from crm.database import Session
from crm.models import Event
from crm.views import event_view
import Constantes.constantes as constante

# from crm.controllers.permissions import requires_permission
from crm.controllers.permissions import requires_permission


def view_event():
    session = Session()
    event_list = session.query(Event).all()
    for event in event_list:
        print(f"Liste des évènements : {event}")


def view_user_own_event(user_id):
    session = Session()
    user_event_list = session.query(Event).filter_by(support_id=user_id).all()
    for event in user_event_list:
        print(f"Liste des évènements : {event}")


@requires_permission("create_event")
def create_event(
    client_id,
    contract_id,
    start_date,
    end_date,
    location,
    attendees,
    current_user_role_id,
):
    session = Session()
    try:

        new_event = Event(
            client_id=client_id,
            contract_id=contract_id,
            start_date=start_date,
            end_date=end_date,
            location=location,
            attendees=attendees,
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


def update_event(
    user_id,
    event_id,
    start_date=None,
    end_date=None,
    location=None,
    attendees=None,
    notes=None,
):
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            print("Event not found.")
            return False
        if start_date:
            event.start_date = start_date
        if end_date:
            event.end_date = end_date
        if location:
            event.location = location
        if attendees:
            event.attendees = attendees
        if notes:
            event.notes = notes

        session.commit()
        print("Event updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating event: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def delete_event(user_id, event_id):
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            print(f"User with id {event_id} not found")
            return False
        session.delete(event)
        session.commit()
        print(f"Event with ID {event_id} has been deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting event: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def view_no_support_event():
    session = Session()
    no_support_event_list = session.query(Event).filter_by(support_id=None).all()
    for event in no_support_event_list:
        print(f"List of event with no affected support : {event}")


def update_no_support_event(user_id, event_id, support_id):
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            print("Contract not found.")
            return False

        event.support_id = support_id
        session.commit()
        print("New support affected successfully to this event.")
        return True
    except Exception as e:
        print(f"Error updating event: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def update_event_menu(user_id, event_id):
    while True:
        update_event_choice = event_view.EventView.show_update_event_menu()
        if update_event_choice == constante.EVENT_UPDATE_START_DATE:
            new_start_date = event_view.EventView.get_new_event_start_date()
            update_event(user_id, event_id, start_date=new_start_date)
        elif update_event_choice == constante.EVENT_UPDATE_END_DATE:
            new_end_date = event_view.EventView.get_new_event_end_date()
            update_event(user_id, event_id, end_date=new_end_date)
        elif update_event_choice == constante.EVENT_UPDATE_LOCATION:
            new_location = event_view.EventView.get_new_location()
            update_event(user_id, event_id, location=new_location)
        elif update_event_choice == constante.EVENT_UPDATE_ATTENDEES:
            new_attendees = event_view.EventView.get_new_attenddes()
            update_event(user_id, event_id, attendees=new_attendees)
        elif update_event_choice == constante.EVENT_UPDATE_NOTES:
            new_notes = event_view.EventView.get_new_event_notes()
            update_event(user_id, event_id, notes=new_notes)
        elif update_event_choice == "0":
            break
