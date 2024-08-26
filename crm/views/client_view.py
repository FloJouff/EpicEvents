import Constantes.constantes as constante


class AdminClientView:
    @staticmethod
    def show_admin_client_menu():
        print("\n--- Admin Client Menu ---")
        print(f"{constante.ADMIN_VIEW_CLIENT}. View clients list")
        print(f"{constante.ADMIN_UPDATE_CLIENT}. Update client's data")
        print(f"{constante.ADMIN_DELETE_CLIENT}. Delete a client")
        print("0. Back")
        return input("Select an option : ")


class ManagementClientView:
    @staticmethod
    def show_management_client_menu():
        print("\n--- Manager Client Menu ---")
        print(f"{constante.MANAGEMENT_VIEW_CLIENT}. View clients list")
        print(
            f"{constante.MANAGEMENT_UPDATE_CLIENT_SALES}. Update client's sales"
        )
        print("0. Back")
        return input("Select an option : ")


class SalesClientView:
    @staticmethod
    def show_sales_client_menu():
        print("\n--- Sales Client Menu ---")
        print(f"{constante.SALES_VIEW_CLIENT}. View clients list")
        print(f"{constante.SALES_CREATE_CLIENT}. Create new client")
        print(f"{constante.SALES_UPDATE_CLIENT}. Update a client")
        print(f"{constante.SALES_VIEW_OWN_CLIENT}. view own client list")
        print("0. Back")
        return input("Select an option : ")

    @staticmethod
    def get_new_client_info():
        name = input("Name : ")
        firstname = input("Firstname : ")
        email = input("Email : ")
        phone = input("Phone : (+33)")
        company = input("Client's company : ")
        return name, firstname, email, phone, company

    def update_client_menu():
        print("\n--- Update Client Menu ---")
        print(f"{constante.CLIENT_UPDATE_EMAIL}. Update email")
        print(f"{constante.CLIENT_UPDATE_PHONE}. Update phone")
        print(f"{constante.CLIENT_UPDATE_COMPANY}. Update entreprise")
        print(f"{constante.CLIENT_UPDATE_NAME}. Update name")
        print(
            f"{constante.CLIENT_UPDATE_LAST_CONTACT}. Update last contact's date"
        )
        print("6. Back")
        return input("Select an option : ")


class SupportClientView:
    @staticmethod
    def show_support_client_menu():
        print("\n--- Support Client Menu ---")
        print(f"{constante.SUPPORT_VIEW_CLIENT}. View clients list")
        print("0. Back")
        return input("Select an option : ")


# def get_new_client_info():
#     name = input("Name : ")
#     firstname = input("Firstname : ")
#     email = input("Email : ")
#     phone = input("Phone : ")
#     company = input("Client's company) : ")
#     return name, firstname, email, phone, company


class ClientView:
    @staticmethod
    def show_update_client_menu():
        print("\n--- Update User Profile ---")
        print(f"{constante.CLIENT_UPDATE_NAME}. Update Name")
        print(f"{constante.CLIENT_UPDATE_FIRSTNAME}. Update Firstname")
        print(f"{constante.CLIENT_UPDATE_EMAIL}. Update Email")
        print(f"{constante.CLIENT_UPDATE_PHONE}. Update Phone")
        print(f"{constante.CLIENT_UPDATE_COMPANY}. Update Company")
        print(f"{constante.CLIENT_UPDATE_LAST_CONTACT}. Update last contact date")
        print("0. Back to Main Menu")
        return input("Select an option : ")

    @staticmethod
    def get_new_client_name():
        return input("Enter new name: ")

    @staticmethod
    def get_new_client_firstname():
        return input("Enter new firstname: ")

    @staticmethod
    def get_new_client_email():
        return input("Enter new email: ")

    @staticmethod
    def get_new_client_phone():
        return input("Enter new phone: ")

    @staticmethod
    def get_new_client_company():
        return input("Enter new company: ")

    @staticmethod
    def get_new_client_last_contact():
        return input("Enter date of last contact: ")

    @staticmethod
    def get_new_client_contact_id():
        return input("Enter new contact_ID for this client: ")

    @staticmethod
    def get_client_id_for_deletion():
        client_id = input("Enter the Client ID to delete: ")
        return int(client_id)
