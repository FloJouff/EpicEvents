from crm.views.user_view import AdminView, UserView
from crm.models import User
from crm.views.client_view import AdminClientView
from crm.views.contract_view import AdminContractView
from crm.views.event_view import AdminEventView
from crm.views.client_view import ClientView
from crm.views.contract_view import ContractView
from crm.views.event_view import EventView
from crm.controllers.user_controller import (
    create_user,
    update_user,
    view_users,
    delete_user,
)
from crm.controllers import client_controller
from crm.controllers.contracts_controller import (
    view_contract,
    create_contract,
    update_contract_menu,
)
from crm.controllers.event_controller import (
    view_event,
    create_event,
    update_event_menu,
    delete_event,
)
import Constantes.constantes as constante


class AdminController:
    @staticmethod
    def handle_admin_menu(user_id, role_id):
        while True:
            choice = AdminView.show_admin_menu()
            if choice == constante.ADMIN_CREATE_USER:
                results = AdminView.get_new_user_info()
                create_user(*results, current_user_role_id=role_id)
            elif choice == constante.ADMIN_UPDATE_USER:
                user_id = input("User_id needing an update : ")
                AdminController.update_user_menu(user_id)
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
                AdminController.admin_client_menu(user_id, role_id)
            elif choice == constante.ADMIN_CONTRACTS_MENU:
                AdminController.admin_contract_menu(user_id, role_id)
            elif choice == constante.ADMIN_EVENTS_MENU:
                AdminController.admin_event_menu(user_id, role_id)
            elif choice == "0":
                break

    @staticmethod
    def update_user_menu(user_id):
        while True:
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

    @staticmethod
    def admin_client_menu(user_id, role_id):
        while True:
            adm_client_choice = AdminClientView.show_admin_client_menu()
            if adm_client_choice == constante.ADMIN_VIEW_CLIENT:
                client_controller.view_client()
            elif adm_client_choice == constante.ADMIN_UPDATE_CLIENT:
                client_id = input("Client_id needing an update : ")
                client_controller.update_client_menu(
                    user_id, client_id, current_user_role_id=role_id
                )
            elif adm_client_choice == constante.ADMIN_DELETE_CLIENT:
                client_id_to_delete = ClientView.get_client_id_for_deletion()
                success = client_controller.delete_client(
                    client_id_to_delete, current_user_role_id=role_id
                )
                if success:
                    print("Client deleted successfully.")
                else:
                    print("Failed to delete client. Please try again.")
            elif adm_client_choice == "0":
                break

    @staticmethod
    def admin_contract_menu(user_id, role_id):
        while True:
            adm_contract_choice = AdminContractView.show_admin_contract_menu()
            if adm_contract_choice == constante.ADMIN_VIEW_CONTRACT:
                view_contract()
            elif adm_contract_choice == constante.ADMIN_CREATE_CONTRACT:
                result = ContractView.get_new_contract_info()
                create_contract(*result, current_user_role_id=role_id)
            elif adm_contract_choice == constante.ADMIN_UPDATE_CONTRACT:
                contract_id = input("Contract_id needing an update : ")
                update_contract_menu(user_id, contract_id, current_user_role_id=role_id)
            # elif adm_contract_choice == constante.ADMIN_DELETE_CONTRACT:
            #     contract_id_to_delete = ContractView.get_contract_id_for_deletion()
            #     success = delete_contract(
            #         user_id, contract_id_to_delete, current_user_role_id=role_id
            #     )
            #     if success:
            #         print("Contract deleted successfully.")
            #     else:
            #         print("Failed to delete Contract. Please try again.")
            elif adm_contract_choice == "0":
                break

    @staticmethod
    def admin_event_menu(user_id, role_id):
        while True:
            adm_event_choice = AdminEventView.show_admin_event_menu()
            if adm_event_choice == constante.ADMIN_VIEW_EVENT:
                view_event()
            elif adm_event_choice == constante.ADMIN_CREATE_EVENT:
                result = EventView.get_new_event_info()
                create_event(*result, current_user_role_id=role_id)
            elif adm_event_choice == constante.ADMIN_UPDATE_EVENT:
                event_id = input("Event_id needing an update : ")
                update_event_menu(user_id, event_id, role_id)
            elif adm_event_choice == constante.ADMIN_DELETE_EVENT:
                event_id_to_delete = EventView.get_event_id_for_deletion()
                success = delete_event(event_id_to_delete, role_id)
                if success:
                    print("Event deleted successfully.")
                else:
                    print("Failed to delete Event. Please try again.")
            elif adm_event_choice == "0":
                break
