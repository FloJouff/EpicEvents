from crm.database import Session
from crm.models import Event

# from crm.controllers.permissions import requires_permission


def view_event():
    session = Session()
    event_list = session.query(Event).all()
    for event in event_list:
        print(f"Liste des évènements : {event}")
