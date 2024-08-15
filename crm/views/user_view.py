import getpass


class AdminView:
    @staticmethod
    def show_admin_menu():
        print("\n--- Admin Main Menu ---")
        print("1. Create new user")
        print("2. Update users")
        print("3. Clients Menu")
        print("4. Contracts Menu")
        print("5. Events Menu")
        print("6. Logout")
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


class ManagementView:
    @staticmethod
    def show_management_menu():
        print("\n--- Management Main Menu ---")
        print("1. Change password")
        print("2. Users Menu")
        print("3. Clients Menu")
        print("4. Contracts Menu")
        print("5. Events Menu")
        print("6. Logout")
        return input("Select an option : ")


class SalesView:
    @staticmethod
    def show_sales_menu():
        print("\n--- Sales Main Menu ---")
        print("1. Change password")
        print("2. Clients Menu")
        print("3. Contracts Menu")
        print("4. Events Menu")
        print("5. Logout")
        return input("Select an option : ")


class SupportView:
    @staticmethod
    def show_support_menu():
        print("\n--- Support Main Menu Support ---")
        print("1. Change password")
        print("2. Clients Menu")
        print("3. Contracts Menu")
        print("4. Events Menu")
        print("5. Logout")
        return input("Select an option : ")
