from crm.views.user_view import ManagementView, UserView, AdminView
from crm.controllers.user_controller import change_password
import Constantes.constantes as constante
from crm.views.client_view import ManagementClientView
from crm.views.contract_view import ManagementContractView, ContractView
from crm.views.event_view import ManagementEventView, EventView
from crm.controllers import user_controller

from crm.controllers.client_controller import (
    view_client,
    update_client_sales,
)
from crm.controllers.contracts_controller import (
    view_contract,
    create_contract,
    update_contract_menu,
)
from crm.controllers.event_controller import (
    view_event,
    view_no_support_event,
    update_no_support_event,
)
from validators import validate_password, validate_email


class ManagementController:

    @staticmethod
    def handle_management_menu(user_id, role_id):
        while True:
            choice = ManagementView.show_management_menu()
            if choice == constante.MANAGEMENT_MODIFY_PASSWORD:
                old_password, new_password = UserView.change_password_menu()
                success = change_password(user_id, old_password, new_password)
                if success:
                    print("Password changed successfully.")
                else:
                    print("Failed to change password. Please try again.")
            elif choice == constante.MANAGEMENT_USERS_MENU:
                ManagementController.user_menu(user_id, role_id)
            elif choice == constante.MANAGEMENT_CLIENTS_MENU:
                ManagementController.management_client_menu(user_id, role_id)
            elif choice == constante.MANAGEMENT_CONTRACTS_MENU:
                ManagementController.management_contract_menu(user_id, role_id)
            elif choice == constante.MANAGEMENT_EVENTS_MENU:
                ManagementController.management_event_menu(user_id, role_id)
            elif choice == "0":
                break

    @staticmethod
    def update_user_menu(user_id, role_id):
        while True:
            update_choice = UserView.show_update_menu()
            if update_choice == constante.UPDATE_NAME:
                new_name = UserView.get_new_name()
                user_controller.update_user(user_id, name=new_name)
            elif update_choice == constante.UPDATE_FIRSTNAME:
                new_firstname = UserView.get_new_firstname()
                user_controller.update_user(user_id, firstname=new_firstname)
            elif update_choice == constante.UPDATE_EMAIL:
                new_email = UserView.get_new_email()
                user_controller.update_user(user_id, email=new_email)
            elif update_choice == constante.UPDATE_PASSWORD:
                new_password = UserView.get_new_password()
                user_controller.update_user(user_id, password=new_password)
            elif update_choice == "0":
                break

    @staticmethod
    def user_menu(user_id, role_id):
        while True:
            user_choice = ManagementView.show_management_user_menu()
            if user_choice == constante.MANAGEMENT_VIEW_USERS:
                user_controller.view_users()
            elif user_choice == constante.MANAGEMENT_CREATE_USER:
                results = AdminView.get_new_user_info()
                user_controller.create_user(*results, current_user_role_id=role_id)
            elif user_choice == constante.MANAGEMENT_UPDATE_USER:
                user_id = input("User_id needing an update : ")
                ManagementController.update_user_menu(user_id)
            elif user_choice == constante.MANAGEMENT_DELETE_USER:
                user_id_to_delete = AdminView.get_user_id_for_deletion()
                success = user_controller.delete_user(user_id_to_delete)
                if success:
                    print("User deleted successfully.")
                else:
                    print("Failed to delete user. Please try again.")
            elif user_choice == "0":
                break

    @staticmethod
    def management_client_menu(user_id, role_id):
        while True:
            manag_client_choice = ManagementClientView.show_management_client_menu()
            if manag_client_choice == constante.MANAGEMENT_VIEW_CLIENT:
                view_client()
            elif manag_client_choice == constante.MANAGEMENT_UPDATE_CLIENT_SALES:
                client_id = input("Client_id needing an update : ")
                contact_id = input("User_id as contact: ")
                update_client_sales(
                    user_id, client_id, contact_id, current_user_role_id=role_id
                )
            elif manag_client_choice == "0":
                break

    @staticmethod
    def management_contract_menu(user_id, role_id):
        while True:
            manag_contract_choice = (
                ManagementContractView.show_management_contract_menu()
            )
            if manag_contract_choice == constante.MANAGEMENT_VIEW_CONTRACT:
                view_contract()
            elif manag_contract_choice == constante.MANAGEMENT_CREATE_CONTRACT:
                result = ContractView.get_new_contract_info()
                create_contract(*result, current_user_role_id=role_id)
            elif manag_contract_choice == constante.MANAGEMENT_UPDATE_CONTRACT:
                contract_id = input("Contract_id needing an update : ")
                update_contract_menu(user_id, contract_id)
            elif manag_contract_choice == "0":
                break

    @staticmethod
    def management_event_menu(user_id, role_id):
        while True:
            manag_event_choice = ManagementEventView.show_management_event_menu()
            if manag_event_choice == constante.MANAGEMENT_VIEW_EVENT:
                view_event()
            elif manag_event_choice == constante.MANAGEMENT_VIEW_NO_SUPPORT:
                view_no_support_event()
            elif manag_event_choice == constante.MANAGEMENT_UPDATE_NO_SUPPORT:
                result = EventView.get_no_support_event_info()
                update_no_support_event(user_id, *result)
            elif manag_event_choice == "0":
                break
