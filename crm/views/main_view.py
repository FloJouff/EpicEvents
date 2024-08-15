import getpass

from crm.controllers.auth_controller import (
    authenticate,
    authorize,
    refresh_token,
)
from crm.controllers.user_controller import create_user, view_users
from crm.views.user_view import (
    AdminView,
    ManagementView,
    SalesView,
    SupportView,
)


def main_menu():
    token = None
    role_id = None

    while True:
        print("\n--- CRM Authentication System ---")
        if token:
            print("1. Refresh Token")
            print("2. Disconnect")
        else:
            print("1. Connect")
        print("3. Quit")

        choice = input("Select an option : ")

        if choice == "1":
            if token:
                new_token = refresh_token(token)
                if new_token:
                    token = new_token
                    print("Token refresh successfully.")
                else:
                    print("Failed to refresh token.")
            else:
                email = input("Email : ")
                password = getpass.getpass("Password : ")
                token, role_id = authenticate(email, password)
                if token:
                    print("Connexion réussie. Accès au CRM...")
                    # Ici, vous pouvez ajouter la logique pour accéder au CRM
                    if role_id == 4:
                        choice = AdminView.show_admin_menu()
                        if choice == "1":
                            results = AdminView.get_new_user_info()
                            print(results)
                            create_user(
                                results[0],
                                results[1],
                                results[2],
                                results[3],
                                results[4],
                                current_user_role_id=role_id,
                            )
                        elif choice == "2":
                            view_users()
                        elif choice == "5":
                            print("Bye")
                            break
                    elif role_id == 1:
                        choice = ManagementView.show_management_menu()

                    elif role_id == 2:
                        choice = SalesView.show_sales_menu()

                    elif role_id == 3:
                        choice = SupportView.show_support_menu()

                else:
                    print("Authentication failed. Please try again.")

        elif choice == "2":
            if token:
                print("Disconnected !")
                token = None
                role_id = None
            else:
                print("Invalid option. Please try again.")
        elif choice == "3":
            print("Bye")
            break
        else:
            print("Invalid option. Please try again.")
