from crm.database import Session
from crm.models import Event
from crm.views import event_view
from crm.controllers.permissions import requires_permission
import Constantes.constantes as constante
import sentry_sdk


def view_event():
    """Search all events in database"""
    session = Session()
    event_list = session.query(Event).all()
    event_view.EventView.display_event_list(event_list)


def view_user_own_event(user_id):
    """Search all event assigned to connected user in database"""
    session = Session()
    user_event_list = session.query(Event).filter_by(support_id=user_id).all()
    event_view.EventView.display_event_list(user_event_list)


def view_no_support_event():
    """Search all events in database with no assigned support"""
    session = Session()
    no_support_event_list = session.query(Event).filter_by(support_id=None).all()
    event_view.EventView.display_event_list(no_support_event_list)


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
    """Create a new event

    Args:
        client_id (int): client's id related to this event
        contract_id (int): contract's id related to this event
        start_date (date): new event start date
        end_date (date): new event end date
        location (str): new event adress
        attendees (int): new event expected attendees
        current_user_role_id (int): role of connected user

    """
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
        event_view.EventView.show_update_event_success()
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "event")
        sentry_sdk.capture_message(f"Error during registration: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("update_event")
def update_event(
    user_id,
    event_id,
    current_user_role_id,
    start_date=None,
    end_date=None,
    location=None,
    attendees=None,
    notes=None,
):
    """Update an existing event

    Args:
        user_id (int): connected user's ID
        event_id (int): Event's ID
        current_user_role_id (int): role of connected user
        start_date (date, optional): New start date. Defaults to None.
        end_date (date, optional): New end date. Defaults to None.
        location (str, optional): New adress. Defaults to None.
        attendees (int, optional): New number of attendees. Defaults to None.
        notes (str, optional): additional notes for/from support. Defaults to None.

    """
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            event_view.EventView.event_not_found()
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
        event_view.EventView.show_update_event_success()
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "event")
        sentry_sdk.capture_message(f"Error updating event: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("update_assigned_event")
def update_assigned_event(
    user_id,
    event_id,
    current_user_role_id,
    start_date=None,
    end_date=None,
    location=None,
    attendees=None,
    notes=None,
):
    """Update an existing event for assigned support

    Args:
        user_id (int): connected user's ID
        event_id (int): Event's ID
        current_user_role_id (int): role of connected user
        start_date (date, optional): New start date. Defaults to None.
        end_date (date, optional): New end date. Defaults to None.
        location (str, optional): New adress. Defaults to None.
        attendees (int, optional): New number of attendees. Defaults to None.
        notes (str, optional): additional notes for/from support. Defaults to None.

    """
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if event.support_id != user_id:
            event_view.EventView.show_acces_event_denied()
            return None
        if not event:
            event_view.EventView.event_not_found()
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
        event_view.EventView.show_update_event_success()
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "event")
        sentry_sdk.capture_message(f"Error updating event: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("delete_event")
def delete_event(event_id, current_user_role_id):
    """Delete an event

    Args:
        event_id (int): event's ID
        current_user_role_id (int): Role of connected user

    """
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            event_view.EventView.event_not_found()
            return False
        session.delete(event)
        session.commit()
        event_view.EventView.show_delete_event_success(event_id)
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "event")
        sentry_sdk.capture_message(f"Error deleting event: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


def update_no_support_event(user_id, event_id, support_id):
    """Assign a new support to an event with no support

    Args:
        user_id (int): connected user's ID
        event_id (int): event's ID
        support_id (int): new support's ID

    """
    session = Session()
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        if not event:
            event_view.EventView.event_not_found()
            return False

        event.support_id = support_id
        session.commit()
        event_view.EventView.show_new_support_affected()
        return True
    except Exception as e:
        sentry_sdk.set_tag("controller", "event")
        sentry_sdk.capture_message(f"Error updating event: {e}", level="error")
        session.rollback()
        return False
    finally:
        session.close()


def update_event_menu(user_id, event_id, current_user_role_id):
    """Controller displaying event update menu according to the choice made by the connected user

    Args:
        user_id (int): connected user's ID
        event_id (int):  event's ID
        current_user_role_id (int): role of connected user to check permission
    """
    while True:
        update_event_choice = event_view.EventView.show_update_event_menu()
        if update_event_choice == constante.EVENT_UPDATE_START_DATE:
            new_start_date = event_view.EventView.get_new_event_start_date()
            update_event(
                user_id, event_id, current_user_role_id, start_date=new_start_date
            )
        elif update_event_choice == constante.EVENT_UPDATE_END_DATE:
            new_end_date = event_view.EventView.get_new_event_end_date()
            update_event(user_id, event_id, current_user_role_id, end_date=new_end_date)
        elif update_event_choice == constante.EVENT_UPDATE_LOCATION:
            new_location = event_view.EventView.get_new_location()
            update_event(user_id, event_id, current_user_role_id, location=new_location)
        elif update_event_choice == constante.EVENT_UPDATE_ATTENDEES:
            new_attendees = event_view.EventView.get_new_attenddes()
            update_event(
                user_id, event_id, current_user_role_id, attendees=new_attendees
            )
        elif update_event_choice == constante.EVENT_UPDATE_NOTES:
            new_notes = event_view.EventView.get_new_event_notes()
            update_event(user_id, event_id, current_user_role_id, notes=new_notes)
        elif update_event_choice == "0":
            break


def update_event_support_menu(user_id, event_id, current_user_role_id):
    """Controller displaying event update menu according to the choice made by the connected user
    the user must be support staff and be assigned to this event

    Args:
        user_id (int): connected user's ID
        event_id (int):  event's ID
        current_user_role_id (int): role of connected user to check permission
    """
    while True:
        update_event_choice = event_view.EventView.show_update_event_menu()
        if update_event_choice == constante.EVENT_UPDATE_START_DATE:
            new_start_date = event_view.EventView.get_new_event_start_date()
            update_assigned_event(
                user_id, event_id, current_user_role_id, start_date=new_start_date
            )
        elif update_event_choice == constante.EVENT_UPDATE_END_DATE:
            new_end_date = event_view.EventView.get_new_event_end_date()
            update_assigned_event(
                user_id, event_id, current_user_role_id, end_date=new_end_date
            )
        elif update_event_choice == constante.EVENT_UPDATE_LOCATION:
            new_location = event_view.EventView.get_new_location()
            update_assigned_event(
                user_id, event_id, current_user_role_id, location=new_location
            )
        elif update_event_choice == constante.EVENT_UPDATE_ATTENDEES:
            new_attendees = event_view.EventView.get_new_attenddes()
            update_assigned_event(
                user_id, event_id, current_user_role_id, attendees=new_attendees
            )
        elif update_event_choice == constante.EVENT_UPDATE_NOTES:
            new_notes = event_view.EventView.get_new_event_notes()
            update_assigned_event(
                user_id, event_id, current_user_role_id, notes=new_notes
            )
        elif update_event_choice == "0":
            break
