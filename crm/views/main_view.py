import getpass
import Constantes.constantes as constante
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.padding import Padding
from rich.text import Text
from rich.theme import Theme
from validators import validate_email


custom_theme = Theme(
    {
        "": "#8896cb",
    }
)
console = Console(theme=custom_theme)


class MainView:
    def show_main_menu(self, is_authenticated):
        """Displays main menu, with authentication"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline] EPICEVENT Authentication menu [/bold white underline]---",
                    (2, 2),
                )
            ),
            justify="center",
        )

        if is_authenticated:
            console.print(Padding(f"{constante.DISCONNECT}. Disconnect ", (0, 4)))
        else:
            console.print(Padding(f"{constante.LOGIN}. Connect ", (0, 4)))
        console.print(Padding("0. Quit ", (0, 4)))
        return console.input("[bold #a575ef]Select an option: [/bold #a575ef]")

    def get_login_credentials(self):
        """Displays input prompts for the connection"""
        while True:
            email = console.input("[bold #ff8133]Email : [/bold #ff8133]").strip()
            if validate_email(email):
                break
        prompt = Text("Password: ", style="bold #ff8133")
        console.print(prompt, end="")
        password = getpass.getpass("")
        return email, password

    @staticmethod
    def show_login_success():
        """Displays success login message"""
        console.print("Login successful.")

    @staticmethod
    def show_login_failure():
        """Displays failure login message"""
        print("[bold red] Authentication failed. Please try again.[/bold red]")

    @staticmethod
    def show_disconnection_success():
        """Displays success disconnection message"""
        console.print("[bold white]Disconnected![/bold white]")

    @staticmethod
    def show_invalid_option_message():
        """Displays error message if the entry is invalid"""
        print("[bold red]Invalid option. Please try again.[/bold red]")

    @staticmethod
    def show_exit_message():
        """Displays goodbye message"""
        console.print("Goodbye!")

    @staticmethod
    def show_session_expiring_message():
        """Displays soon expiring session message"""
        print(
            "[italic red underline ]Your session is about to expire. Please reconnect.[/italic red underline]"
        )

    @staticmethod
    def show_unauthorized_access():
        """Displays unauthorized access message"""
        print("[italic red] Unauthorized access. Please log in again.[/italic red]")
