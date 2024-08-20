import getpass
import jwt
import Constantes.constantes as constante

from crm.controllers.auth_controller import (
    authenticate,
    refresh_token,
)

from crm.controllers.user_controller import (
    create_user,
    view_users,
    update_user,
    change_password,
    delete_user,
)
from crm.views.user_view import (
    AdminView,
    ManagementView,
    SalesView,
    SupportView,
    UserView,
)

from crm.views.client_view import (
    AdminClientView,
    ManagementClientView,
    SalesClientView,
    SupportClientView,
)
from crm.views.contract_view import (
    AdminContractView,
    ManagementContractView,
    SalesContractView,
    SupportContractView,
)
from crm.views.event_view import (
    AdminEventView,
    ManagementEventView,
    SalesEventView,
    SupportEventView,
)

import os

JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


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
                    user_id = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])[
                        "user_id"
                    ]
                    print("Connexion réussie.")
                    if role_id == 4:
                        choice = AdminView.show_admin_menu()
                        if choice == constante.ADMIN_CREATE_USER:
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
                        elif choice == constante.ADMIN_UPDATE_USERS:
                            user_id = input(" User_id needing an update : ")
                            update_choice = UserView.show_update_menu()
                            if update_choice == constante.UPDATE_NAME:
                                new_name = UserView.get_new_name()
                                update_user(user_id, name=new_name)

                            elif update_choice == constante.UPDATE_FIRSTNAME:
                                new_firstname = UserView.get_new_firstname()
                                update_user(user_id, firstname=new_firstname)

                            elif update_choice == constante.UPDATE_EMAIL:
                                new_email = UserView.get_new_email()
                                update_user(user_id, email=new_email)

                            elif update_choice == constante.UPDATE_PASSWORD:
                                new_password = UserView.get_new_password()
                                update_user(user_id, password=new_password)

                            elif update_choice == "0":
                                break
                        elif choice == constante.ADMIN_VIEW_USERS:
                            view_users()
                        elif choice == constante.ADMIN_DELETE_USER:
                            user_id_to_delete = AdminView.get_user_id_for_deletion()
                            success = delete_user(user_id_to_delete)
                            if success:
                                print("User deleted successfully.")
                            else:
                                print("Failed to delete user. Please try again.")
                        elif choice == constante.ADMIN_CLIENTS_MENU:
                            AdminClientView.show_admin_client_menu()
                        elif choice == constante.ADMIN_CONTRACTS_MENU:
                            AdminContractView.show_admin_contract_menu()
                        elif choice == constante.ADMIN_EVENTS_MENU:
                            AdminEventView.show_admin_event_menu()
                        elif choice == "0":
                            print("Bye")
                            break
                    elif role_id == 1:
                        manag_choice = ManagementView.show_management_menu()
                        if manag_choice == constante.MANAGEMENT_MODIFY_PASSWORD:
                            old_password, new_password = UserView.change_password_menu()
                            success = change_password(
                                user_id, old_password, new_password
                            )
                            if success:
                                print("Password changed successfully.")
                            else:
                                print("Failed to change password. Please try again.")
                        elif manag_choice == "2":
                            m_choice = ManagementView.show_user_menu()

                    elif role_id == 2:
                        sales_choice = SalesView.show_sales_menu()
                        if sales_choice == constante.SALES_MODIFY_PASSWORD:
                            old_password, new_password = UserView.change_password_menu()
                            success = change_password(
                                user_id, old_password, new_password
                            )
                            if success:
                                print("Password changed successfully.")
                            else:
                                print("Failed to change password. Please try again.")

                    elif role_id == 3:
                        support_choice = SupportView.show_support_menu()
                        if support_choice == constante.SUPPORT_MODIFY_PASSWORD:
                            old_password, new_password = UserView.change_password_menu()
                            success = change_password(
                                user_id, old_password, new_password
                            )
                            if success:
                                print("Password changed successfully.")
                            else:
                                print("Failed to change password. Please try again.")

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
