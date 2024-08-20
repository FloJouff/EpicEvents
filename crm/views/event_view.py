import Constantes.constantes as constante


class AdminEventView:
    @staticmethod
    def show_admin_event_menu():
        print("\n--- Admin Event Menu ---")
        print(f"{constante.ADMIN_VIEW_EVENT}. View events list")
        print(f"{constante.ADMIN_UPDATE_EVENT}. Update an event ")
        print(f"{constante.ADMIN_DELETE_EVENT}. Delete an event ")
        print("0. Back")
        return input("Select an option : ")


class ManagementEventView:
    @staticmethod
    def show_manager_event_menu():
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


def update_event_menu():
    print("\n--- Update Event ---")
    print(f"{constante.EVENT_UPDATE_START_DATE}. Update start date")
    print(f"{constante.EVENT_UPDATE_END_DATE}. Update end date")
    print(f"{constante.EVENT_UPDATE_LOCATION}. Update location")
    print(f"{constante.EVENT_UPDATE_ATTENDEES}. Update attendees")
    print(f"{constante.EVENT_UPDATE_NOTES}. Update Notes")
    print("0. Back")
    return input("Select an option : ")


def get_new_event_info():
    client_id = input("Client's id : ")
    contract_id = input("Contract's id : ")
    start_date = input("Starting date : ")
    end_date = input("Ending date : ")
    attendees = input("Attendees : ")
    return client_id, contract_id, start_date, end_date, attendees
