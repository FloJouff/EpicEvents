import getpass
import Constantes.constantes as constante
from validators import validate_password, validate_email, validate_name, validate_id
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme(
    {
        "": "#8896cb",
    }
)
console = Console(theme=custom_theme)


class AdminView:
    @staticmethod
    def show_admin_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Admin Main Menu [/bold white]---",
                    (1, 4),
                )
            )
        )
        console.print(Padding(f"{constante.ADMIN_VIEW_USERS}. View all users", (0, 4)))
        console.print(Padding(f"{constante.ADMIN_CREATE_USER}. Create new user", (0, 4)))
        console.print(Padding(f"{constante.ADMIN_UPDATE_USER}. Update user", (0, 4)))
        console.print(Padding(f"{constante.ADMIN_DELETE_USER}. Delete user", (0, 4)))
        console.print(Padding(f"{constante.ADMIN_CLIENTS_MENU}. Clients Menu", (0, 4)))
        console.print(
            Padding(f"{constante.ADMIN_CONTRACTS_MENU}. Contracts Menu", (0, 4))
        )
        console.print(Padding(f"{constante.ADMIN_EVENTS_MENU}. Events Menu", (0, 4)))
        console.print(Padding("0. Logout", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_user_info():
        while True:
            name = console.input("[bold #ff8133]Name : [/bold #ff8133]")
            if validate_name(name):
                break
        while True:
            firstname = console.input("[bold #ff8133]Firstname : [/bold #ff8133]")
            if validate_name(firstname):
                break
        while True:
            email = console.input("[bold #ff8133]Email : [/bold #ff8133]")
            if validate_email(email):
                break
        while True:
            password = getpass.getpass(
                "Password (Your password must contain 8 characters): "
            )
            if validate_password(email):
                break
        role = console.input(
            "[bold #ff8133]User's role ( 1:management \n 2:sales \n 3:support \n 4:admin) : [bold #ff8133]"
        )
        role_id = int(role)
        return name, firstname, email, password, role_id

    @staticmethod
    def get_user_id_for_deletion():
        while True:
            user_id = console.input(
                "[bold #03d01a]Enter user id you need to delete: [/bold #03d01a]"
            )
            if validate_id(user_id):
                break
        return int(user_id)


class ManagementView:
    @staticmethod
    def show_management_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Management Main Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_MODIFY_PASSWORD}. Change password", (0, 4))
        )
        console.print(Padding(f"{constante.MANAGEMENT_USERS_MENU}. Users Menu", (0, 4)))
        console.print(
            Padding(f"{constante.MANAGEMENT_CLIENTS_MENU}. Clients Menu", (0, 4))
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_CONTRACTS_MENU}. Contracts Menu", (0, 4))
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_EVENTS_MENU}. Events Menu", (0, 4))
        )
        console.print(Padding("0. Logout", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def show_management_user_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Users Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_VIEW_USERS}. View users list", (0, 4))
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_CREATE_USER}. Create new user", (0, 4))
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_UPDATE_USER}. Update users", (0, 4))
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_DELETE_USER}. Delete users", (0, 4))
        )
        console.print(Padding("0. Logout", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SalesView:
    @staticmethod
    def show_sales_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Sales Main Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SALES_MODIFY_PASSWORD}. Change password", (0, 4))
        )
        console.print(Padding(f"{constante.SALES_CLIENTS_MENU}. Clients Menu", (0, 4)))
        console.print(
            Padding(f"{constante.SALES_CONTRACTS_MENU}. Contracts Menu", (0, 4))
        )
        console.print(Padding(f"{constante.SALES_EVENTS_MENU}. Events Menu", (0, 4)))
        console.print(Padding("0. Logout", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SupportView:
    @staticmethod
    def show_support_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Support Main Menu Support [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SUPPORT_MODIFY_PASSWORD}. Change password", (0, 4))
        )
        console.print(Padding(f"{constante.SUPPORT_CLIENTS_MENU}. Clients Menu", (0, 4)))
        console.print(
            Padding(f"{constante.SUPPORT_CONTRACTS_MENU}. Contracts Menu", (0, 4))
        )
        console.print(Padding(f"{constante.SUPPORT_EVENTS_MENU}. Events Menu", (0, 4)))
        console.print(Padding("0. Logout", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class UserView:
    @staticmethod
    def show_update_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Update User Profile [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(Padding(f"{constante.UPDATE_NAME}. Update Name", (0, 4)))
        console.print(Padding(f"{constante.UPDATE_FIRSTNAME}. Update Firstname", (0, 4)))
        console.print(Padding(f"{constante.UPDATE_EMAIL}. Update Email", (0, 4)))
        console.print(Padding(f"{constante.UPDATE_PASSWORD}. Update Password", (0, 4)))
        console.print(Padding("0. Back to Main Menu", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_user_id():
        while True:
            user_id = console.input(
                "[bold #03d01a]Enter user id you need to update: [/bold #03d01a]"
            )
            if validate_id(user_id):
                break
        return user_id

    @staticmethod
    def get_new_name():
        while True:
            name = console.input("[bold #ff8133]Enter new Name : [/bold #ff8133]")
            if validate_name(name):
                break
        return name

    @staticmethod
    def get_new_firstname():
        while True:
            firstname = console.input(
                "[bold #ff8133]Enter new firstname : [/bold #ff8133]"
            )
            if validate_name(firstname):
                break
        return firstname

    @staticmethod
    def get_new_email():
        while True:
            email = console.input("[bold #03d01a]Enter new email : [/bold #03d01a]")
            if validate_email(email):
                break
        return email

    @staticmethod
    def get_new_password():
        return getpass.getpass(
            "Enter new password (Your password must contain 8 characters): "
        )

    @staticmethod
    def change_password_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Change password Menu[/bold white]---",
                    (1, 2),
                )
            )
        )
        old_password = getpass.getpass("Enter your current password: ")
        while True:
            new_password = getpass.getpass(
                "Enter your new password (Your password must contain at least 8 characters): "
            )
            if validate_password(new_password):
                break
        return old_password, new_password

    @staticmethod
    def show_delete_success_message(user_id):
        return console.print(
            f"[yellow] User [bold]{user_id} [/bold] has been deleted successfully. [/yellow]"
        )

    @staticmethod
    def show_delete_error_message():
        return console.print(
            "[italic red]Failed to delete user. Please try again.[/italic red]"
        )

    @staticmethod
    def show_invalid_old_password():
        return console.print("[italic red]Incorrect old password. [/italic red]")

    @staticmethod
    def show_password_change_successfully():
        return console.print("Password changed successfully.")

    @staticmethod
    def show_password_change_failed():
        return console.print(
            "[italic red]Failed to change password. Please try again.[/italic red]"
        )

    @staticmethod
    def show_user_already_exists_error_message():
        return console.print("[italic red]This user already exists.[/italic red]")

    @staticmethod
    def show_no_user_error_message():
        return console.print("[italic red]User not found.[/italic red]")

    @staticmethod
    def show_create_user_success():
        return console.print("User registered successfully.")

    @staticmethod
    def display_user_list(users):
        table = Table(title="List of Users")

        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Name", style="magenta")
        table.add_column("Firstname", style="magenta")
        table.add_column("Email", style="green")
        table.add_column("Role ID", style="yellow")

        for user in users:
            table.add_row(
                str(user.user_id),
                user.name,
                user.firstname,
                user.email,
                str(user.role_id),
            )

        console.print(table)

    @staticmethod
    def show_update_user_success():
        return console.print("User updated successfully.")

    @staticmethod
    def display_welcome_message(name, firstname):
        console.print(
            Panel.fit(
                Padding(
                    f"[green]Bienvenue [/green] [bold white] {name} {firstname} [/bold white]",
                    (1, 2),
                )
            )
        )
