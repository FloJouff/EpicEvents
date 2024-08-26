from crm.views.user_view import SupportView, UserView
from crm.controllers.user_controller import change_password
import Constantes.constantes as constante
from crm.views.client_view import SupportClientView
from crm.views.contract_view import SupportContractView
from crm.views.event_view import SupportEventView

from crm.controllers.client_controller import (
    view_client,
)
from crm.controllers.contracts_controller import (
    view_contract,
)
from crm.controllers.event_controller import (
    view_event,
    view_user_own_event,
    update_event,
)


class SupportController:

    @staticmethod
    def handle_support_menu(user_id, role_id):
        while True:
            choice = SupportView.show_support_menu()
            if choice == constante.SUPPORT_MODIFY_PASSWORD:
                old_password, new_password = UserView.change_password_menu()
                success = change_password(user_id, old_password, new_password)
                if success:
                    print("Password changed successfully.")
                else:
                    print("Failed to change password. Please try again.")
            elif choice == constante.SUPPORT_CLIENTS_MENU:
                SupportController.support_client_menu(user_id, role_id)
            elif choice == constante.SUPPORT_CONTRACTS_MENU:
                SupportController.support_contract_menu()
            elif choice == constante.SUPPORT_EVENTS_MENU:
                SupportController.support_event_menu()
            elif choice == "0":
                break

    @staticmethod
    def support_client_menu(user_id, role_id):
        while True:
            support_client_choice = SupportClientView.show_support_client_menu()
            if support_client_choice == constante.SUPPORT_VIEW_CLIENT:
                view_client()
            elif support_client_choice == "0":
                break

    @staticmethod
    def support_contract_menu(user_id, role_id):
        while True:
            support_contract_choice = SupportContractView.show_support_contract_menu()
            if support_contract_choice == constante.SUPPORT_VIEW_CONTRACT:
                view_contract()
            elif support_contract_choice == "0":
                break

    @staticmethod
    def support_event_menu(user_id, role_id):
        while True:
            support_event_choice = SupportEventView.show_support_event_menu()
            if support_event_choice == constante.SUPPORT_VIEW_EVENT:
                view_event()
            elif support_event_choice == constante.SUPPORT_VIEW_OWN_EVENT:
                view_user_own_event(user_id, role_id)
            elif support_event_choice == constante.SUPPORT_UPDATE_EVENT:
                event_id = input("Event_id you need to update : ")
                update_event(user_id, event_id)
            elif support_event_choice == "0":
                break
