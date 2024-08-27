import getpass
import Constantes.constantes as constante


class MainView:
    def show_main_menu(self, is_authenticated):
        print("\n--- CRM Authentication System ---")

        if is_authenticated:
            print(f"{constante.DISCONNECT}. Disconnect")
        else:
            print(f"{constante.LOGIN}. Connect")
        print("0. Quit")
        return input("Select an option: ")

    def get_login_credentials(self):
        email = input("Email: ")
        password = getpass.getpass("Password: ")
        return email, password

    def show_login_success(self):
        print("Login successful.")

    def show_login_failure(self):
        print("Authentication failed. Please try again.")

    def show_disconnection_success(self):
        print("Disconnected!")

    def show_invalid_option_message(self):
        print("Invalid option. Please try again.")

    def show_exit_message(self):
        print("Goodbye!")

    def show_session_expiring_message(self):
        print("Your session is about to expire. Please reconnect.")
