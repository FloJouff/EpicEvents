import getpass
import Constantes.constantes as constante
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.padding import Padding
from rich.text import Text
from rich.theme import Theme


custom_theme = Theme(
    {
        "": "#8896cb",
    }
)
console = Console(theme=custom_theme)


class MainView:
    def show_main_menu(self, is_authenticated):
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
        email = console.input("[bold #ff8133] Email: [/bold #ff8133]")
        prompt = Text("Password: ", style="bold #ff8133")
        console.print(prompt, end="")
        password = getpass.getpass("")
        return email, password

    def show_login_success(self):
        console.print("Login successful.")

    def show_login_failure(self):
        print("[bold red] Authentication failed. Please try again.[/bold red]")

    def show_disconnection_success(self):
        console.print("[bold white]Disconnected![/bold white]")

    def show_invalid_option_message(self):
        print("[bold red]Invalid option. Please try again.[/bold red]")

    def show_exit_message(self):
        console.print("Goodbye!")

    def show_session_expiring_message(self):
        print(
            "[italic red underline ]Your session is about to expire. Please reconnect.[/italic red underline]"
        )

    def show_unauthorized_access(self):
        print("[italic red] Unauthorized access. Please log in again.[/italic red]")
