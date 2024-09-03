from crm.views.user_view import SalesView, UserView
from crm.views.main_view import MainView
from crm.controllers.user_controller import change_password
import Constantes.constantes as constante
from crm.views.client_view import SalesClientView, ClientView
from crm.views.contract_view import SalesContractView, ContractView
from crm.views.event_view import SalesEventView, EventView
from crm.controllers import client_controller
from crm.models import User
from crm.controllers import contracts_controller
from crm.controllers import event_controller
import sentry_sdk


class SalesController:

    @staticmethod
    def handle_sales_menu(user_id, role_id, token):
        if User.authorize(token, role_id):
            while True:
                choice = SalesView.show_sales_menu()
                if choice == constante.SALES_MODIFY_PASSWORD:
                    old_password, new_password = UserView.change_password_menu()
                    success = change_password(user_id, old_password, new_password)
                    if success:
                        UserView.show_password_change_successfully()
                    else:
                        UserView.show_password_change_failed()
                elif choice == constante.SALES_CLIENTS_MENU:
                    SalesController.sales_client_menu(user_id, role_id, token)
                elif choice == constante.SALES_CONTRACTS_MENU:
                    SalesController.sales_contract_menu(user_id, role_id, token)
                elif choice == constante.SALES_EVENTS_MENU:
                    SalesController.sales_event_menu(user_id, role_id, token)
                elif choice == "0":
                    break
        else:
            MainView.show_unauthorized_access()
            sentry_sdk.set_tag("controller", "sales")
            sentry_sdk.capture_message(
                MainView.show_unauthorized_access(), level="warning"
            )
            return

    @staticmethod
    def sales_client_menu(user_id, role_id, token):
        if User.authorize(token, role_id):
            while True:
                sales_client_choice = SalesClientView.show_sales_client_menu()
                if sales_client_choice == constante.SALES_VIEW_CLIENT:
                    client_controller.view_client()
                elif sales_client_choice == constante.SALES_CREATE_CLIENT:
                    result = SalesClientView.get_new_client_info()
                    client_controller.create_client(
                        *result, contact_id=user_id, current_user_role_id=role_id
                    )
                elif sales_client_choice == constante.SALES_UPDATE_CLIENT:
                    client_id = ClientView.get_client_id_for_update()
                    client_controller.update_client_menu(
                        user_id, client_id, current_user_role_id=role_id
                    )
                elif sales_client_choice == constante.SALES_VIEW_OWN_CLIENT:
                    client_controller.view_own_client(user_id)
                elif sales_client_choice == "0":
                    break
        else:
            MainView.show_unauthorized_access()
            sentry_sdk.set_tag("controller", "sales")
            sentry_sdk.capture_message(
                MainView.show_unauthorized_access(), level="warning"
            )
            return

    @staticmethod
    def sales_contract_menu(user_id, role_id, token):
        if User.authorize(token, role_id):
            while True:
                sales_contract_choice = SalesContractView.show_sales_contract_menu()
                if sales_contract_choice == constante.SALES_VIEW_CONTRACT:
                    contracts_controller.view_contract()
                elif sales_contract_choice == constante.SALES_UPDATE_OWN_CONTRACT:
                    contract_id = ContractView.get_contract_id()
                    # SalesContractView.show_sales_update_contract_menu()
                    contracts_controller.update_own_contract_menu(
                        user_id, contract_id, role_id
                    )
                elif sales_contract_choice == constante.SALES_UNSIGNED_CONTRACT:
                    contracts_controller.view_unsigned_contract()
                elif sales_contract_choice == constante.SALES_UNPAID_CONTRACT:
                    contracts_controller.view_unpaid_contract()
                elif sales_contract_choice == constante.SALES_VIEW_OWN_CONTRACT:
                    contracts_controller.view_user_own_contracts(user_id)
                elif sales_contract_choice == "0":
                    break
        else:
            MainView.show_unauthorized_access()
            sentry_sdk.set_tag("controller", "sales")
            sentry_sdk.capture_message(
                MainView.show_unauthorized_access(), level="warning"
            )
            return

    @staticmethod
    def sales_event_menu(user_id, role_id, token):
        if User.authorize(token, role_id):
            while True:
                sales_event_choice = SalesEventView.show_sales_event_menu()
                if sales_event_choice == constante.SALES_VIEW_EVENT:
                    event_controller.view_event()
                elif sales_event_choice == constante.SALES_CREATE_EVENT:
                    result = EventView.get_new_event_info()
                    event_controller.create_event(*result, current_user_role_id=role_id)
                elif sales_event_choice == "0":
                    break
        else:
            MainView.show_unauthorized_access()
            sentry_sdk.set_tag("controller", "sales")
            sentry_sdk.capture_message(
                MainView.show_unauthorized_access(), level="warning"
            )
            return
