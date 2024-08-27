import Constantes.constantes as constante
from validators import validate_date


class AdminEventView:
    @staticmethod
    def show_admin_event_menu():
        print("\n--- Admin Event Menu ---")
        print(f"{constante.ADMIN_VIEW_EVENT}. View events list")
        print(f"{constante.ADMIN_CREATE_EVENT}. Create an event")
        print(f"{constante.ADMIN_UPDATE_EVENT}. Update an event ")
        print(f"{constante.ADMIN_DELETE_EVENT}. Delete an event ")
        print("0. Back")
        return input("Select an option : ")


class ManagementEventView:
    @staticmethod
    def show_management_event_menu():
        print("\n--- Manager Event Menu ---")
        print(f"{constante.MANAGEMENT_VIEW_EVENT}. View events list")
        print(f"{constante.MANAGEMENT_VIEW_NO_SUPPORT}. View events with no support")
        print(
            f"{constante.MANAGEMENT_UPDATE_NO_SUPPORT}. Update an event with no support"
        )
        print("0. Back")
        return input("Select an option : ")


class SalesEventView:
    @staticmethod
    def show_sales_event_menu():
        print("\n--- Sales Event Menu---")
        print(f"{constante.SALES_VIEW_EVENT}. View events list")
        print(f"{constante.SALES_CREATE_EVENT}. Create new event")
        print("0. Back")
        return input("Select an option : ")


class SupportEventView:
    @staticmethod
    def show_support_event_menu():
        print("\n--- Support Event Menu ---")
        print(f"{constante.SUPPORT_VIEW_EVENT}. View events list")
        print(f"{constante.SUPPORT_VIEW_OWN_EVENT}. View my events list")
        print(f"{constante.SUPPORT_UPDATE_EVENT}. Update an event")
        print("0. Back")
        return input("Select an option : ")


class EventView:
    @staticmethod
    def show_update_event_menu():
        print("\n--- Update Event ---")
        print(f"{constante.EVENT_UPDATE_START_DATE}. Update start date (YYYY-MM-DD)")
        print(f"{constante.EVENT_UPDATE_END_DATE}. Update end date (YYYY-MM-DD)")
        print(f"{constante.EVENT_UPDATE_LOCATION}. Update location")
        print(f"{constante.EVENT_UPDATE_ATTENDEES}. Update attendees")
        print(f"{constante.EVENT_UPDATE_NOTES}. Update Notes")
        print("0. Back")
        return input("Select an option : ")

    @staticmethod
    def get_new_event_info():
        client_id = input("Client's id : ")
        contract_id = input("Contract's id : ")
        while True:
            start_date = input("Starting date (YYYY-MM-DD): ")
            if validate_date(start_date):
                break
        while True:
            end_date = input("Ending date (YYYY-MM-DD): ")
            if validate_date(end_date):
                break
        location = input("Location : ")
        attendees = input("Attendees : ")
        return client_id, contract_id, start_date, end_date, location, attendees

    @staticmethod
    def get_new_event_start_date():
        return input("Enter new starting date (YYYY-MM-DD): ")

    @staticmethod
    def get_new_event_end_date():
        return input("Enter new ending date (YYYY-MM-DD): ")

    @staticmethod
    def get_new_location():
        return input("Enter new location: ")

    @staticmethod
    def get_new_attenddes():
        return input("Enter new attendees: ")

    @staticmethod
    def get_new_event_notes():
        return input("Enter your notes: ")

    @staticmethod
    def get_new_support_id():
        support_id = input("Enter the Support ID for this event: ")
        return int(support_id)

    @staticmethod
    def get_event_id_for_deletion():
        event_id = input("Enter the event ID to delete: ")
        return int(event_id)

    @staticmethod
    def get_no_support_event_info():
        event_id = input("Event's id : ")
        support_id = input("User_id you want to afffect to this event : ")
        return event_id, support_id

    @staticmethod
    def get_event_id():
        event_id = input("Enter the event ID: ")
        return int(event_id)
