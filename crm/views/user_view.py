import getpass
import Constantes.constantes as constante


class AdminView:
    @staticmethod
    def show_admin_menu():
        print("\n--- Admin Main Menu ---")
        print(f"{constante.ADMIN_VIEW_USERS}. View all users")
        print(f"{constante.ADMIN_CREATE_USER}. Create new user")
        print(f"{constante.ADMIN_UPDATE_USERS}. Update user")
        print(f"{constante.ADMIN_DELETE_USER}. Delete user")
        print(f"{constante.ADMIN_CLIENTS_MENU}. Clients Menu")
        print(f"{constante.ADMIN_CONTRACTS_MENU}. Contracts Menu")
        print(f"{constante.ADMIN_EVENTS_MENU}. Events Menu")
        print("0. Logout")
        return input("Select an option : ")

    @staticmethod
    def get_new_user_info():
        name = input("Name : ")
        firstname = input("Firstname : ")
        email = input("Email : ")
        password = getpass.getpass("Password : ")
        role = input("User's role (management/sales/support/admin) : ")
        role_id = int(role)
        return name, firstname, email, password, role_id

    @staticmethod
    def get_user_id_for_deletion():
        user_id = input("Enter the User ID to delete: ")
        return int(user_id)


class ManagementView:
    @staticmethod
    def show_management_menu():
        print("\n--- Management Main Menu ---")
        print(f"{constante.MANAGEMENT_MODIFY_PASSWORD}. Change password")
        print(f"{constante.MANAGEMENT_USERS_MENU}. Users Menu")
        print(f"{constante.MANAGEMENT_CLIENTS_MENU}. Clients Menu")
        print(f"{constante.MANAGEMENT_CONTRACTS_MENU}. Contracts Menu")
        print(f"{constante.MANAGEMENT_EVENTS_MENU}. Events Menu")
        print("0. Logout")
        return input("Select an option : ")

    @staticmethod
    def show_user_menu():
        print("\n--- Users Menu ---")
        print(f"{constante.VIEW_USER_LIST}. View users list")
        print(f"{constante.CREATE_USER}. Create new user")
        print(f"{constante.UPDATE_USER}. Update users")
        print(f"{constante.DELETE_USER}. Delete users")
        print("0. Logout")
        return input("Select an option : ")


class SalesView:
    @staticmethod
    def show_sales_menu():
        print("\n--- Sales Main Menu ---")
        print(f"{constante.SALES_MODIFY_PASSWORD}. Change password")
        print(f"{constante.SALES_CLIENTS_MENU}. Clients Menu")
        print(f"{constante.SALES_CONTRACTS_MENU}. Contracts Menu")
        print(f"{constante.SALES_EVENTS_MENU}. Events Menu")
        print("0. Logout")
        return input("Select an option : ")


class SupportView:
    @staticmethod
    def show_support_menu():
        print("\n--- Support Main Menu Support ---")
        print(f"{constante.SUPPORT_MODIFY_PASSWORD}. Change password")
        print(f"{constante.SUPPORT_CLIENTS_MENU}. Clients Menu")
        print(f"{constante.SUPPORT_CONTRACTS_MENU}. Contracts Menu")
        print(f"{constante.SUPPORT_EVENTS_MENU}. Events Menu")
        print("0. Logout")
        return input("Select an option : ")


class UserView:
    @staticmethod
    def show_update_menu():
        print("\n--- Update User Profile ---")
        print(f"{constante.UPDATE_NAME}. Update Name")
        print(f"{constante.UPDATE_FIRSTNAME}. Update Firstname")
        print(f"{constante.UPDATE_EMAIL}. Update Email")
        print(f"{constante.UPDATE_PASSWORD}. Update Password")
        print("0. Back to Main Menu")
        return input("Select an option : ")

    @staticmethod
    def get_new_name():
        return input("Enter new name: ")

    @staticmethod
    def get_new_firstname():
        return input("Enter new firstname: ")

    @staticmethod
    def get_new_email():
        return input("Enter new email: ")

    @staticmethod
    def get_new_password():
        return getpass.getpass("Enter new password: ")

    @staticmethod
    def change_password_menu():
        print("\n--- Change Password ---")
        old_password = getpass.getpass("Enter your current password: ")
        new_password = getpass.getpass("Enter your new password: ")
        return old_password, new_password
