class ManagementClientView:
    @staticmethod
    def show_management_client_menu():
        print("\n--- Manager Client Menu ---")
        print("1. View clients list")
        print("2. Update client's sales")
        print("3. Back")
        print("4. Logout")
        return input("Select an option : ")


class SalesClientView:
    @staticmethod
    def show_sales_client_menu():
        print("\n--- Sales Client Menu ---")
        print("1. View clients list")
        print("2. Create new client")
        print("3. Update a client")
        print("4. view own client list")
        print("5. Back")
        print("6. Logout")
        return input("Select an option : ")

    def update_client_menu():
        print("\n--- Update Client Menu ---")
        print("1. Update email")
        print("2. Update phone")
        print("3. Update entreprise")
        print("4. Update name")
        print("5. Update last contact's date")
        print("6. Back")
        print("7. Logout")
        return input("Select an option : ")


class SupportClientView:
    @staticmethod
    def show_support_client_menu():
        print("\n--- Support Client Menu ---")
        print("1. View clients list")
        print("2. Back")
        print("3. Logout")
        return input("Select an option : ")
