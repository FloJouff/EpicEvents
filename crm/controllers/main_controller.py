import jwt
from crm.controllers.auth_controller import authenticate
from crm.controllers import auth_controller
from crm.controllers.admin_controller import AdminController
from crm.controllers.management_controller import ManagementController
from crm.controllers.sales_controller import SalesController
from crm.controllers.support_controller import SupportController
from crm.views.main_view import MainView
import os
import Constantes.constantes as constante
from datetime import datetime, timedelta

JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


class MainController:
    def __init__(self):
        self.token = None
        self.role_id = None
        self.user_id = None
        self.token_expiry = None
        self.view = MainView()

    def main_menu(self):
        while True:
            if self.token and self.token_expiry:
                if datetime.now() >= self.token_expiry - timedelta(minutes=5):
                    self.view.show_session_expiring_message()
                    self.handle_disconnection()

            choice = self.view.show_main_menu(self.token is not None)

            if choice == constante.LOGIN:
                self.handle_authentication()
            elif choice == constante.DISCONNECT:
                self.handle_disconnection()
            elif choice == "0":
                self.view.show_exit_message()
                break
            else:
                self.view.show_invalid_option_message()

    def handle_authentication(self):
        if not self.token:
            self.login()

    def login(self):
        email, password = self.view.get_login_credentials()
        self.token, self.role_id = authenticate(email, password)
        print(self.role_id)
        if self.token:
            decoded_token = jwt.decode(
                self.token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
            )
            self.user_id = decoded_token["user_id"]
            self.token_expiry = datetime.fromtimestamp(decoded_token["exp"])
            self.view.show_login_success()
            self.handle_role_specific_actions()
        else:
            self.view.show_login_failure()

    def handle_role_specific_actions(self):
        if self.role_id == 4:
            AdminController.handle_admin_menu(self.user_id, self.role_id)
        elif self.role_id == 1:
            ManagementController.handle_management_menu(self.user_id, self.role_id)
        elif self.role_id == 2:
            SalesController.handle_sales_menu(self.user_id, self.role_id)
        elif self.role_id == 3:
            SupportController.handle_support_menu(self.user_id, self.role_id)

    def handle_disconnection(self):
        if self.token:
            self.token = None
            self.role_id = None
            self.user_id = None
            self.token_expiry = None
            self.view.show_disconnection_success()
        else:
            self.view.show_invalid_option_message()


def run_main_menu():
    controller = MainController()
    controller.main_menu()
