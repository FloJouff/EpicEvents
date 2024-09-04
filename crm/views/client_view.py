import Constantes.constantes as constante
from validators import (
    validate_email,
    validate_phone_number,
    validate_name,
    validate_date,
    validate_id,
)
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.theme import Theme
from rich.console import Console
from rich.table import Table


custom_theme = Theme(
    {
        "": "#8896cb",
    }
)
console = Console(theme=custom_theme)


class AdminClientView:
    @staticmethod
    def show_admin_client_menu():
        """Displays admin's client menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Admin Client Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.ADMIN_VIEW_CLIENT}. View clients list", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_UPDATE_CLIENT}. Update client's data", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_DELETE_CLIENT}. Delete a client", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class ManagementClientView:
    @staticmethod
    def show_management_client_menu():
        """Displays management's client menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]Manager Client Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_VIEW_CLIENT}. View clients list", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.MANAGEMENT_UPDATE_CLIENT_SALES}. Update client's sales",
                (0, 4),
            )
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SalesClientView:
    @staticmethod
    def show_sales_client_menu():
        """Displays sales's client menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]Sales Client Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SALES_VIEW_CLIENT}. View clients list", (0, 4))
        )
        console.print(
            Padding(f"{constante.SALES_CREATE_CLIENT}. Create new client", (0, 4))
        )
        console.print(
            Padding(f"{constante.SALES_UPDATE_CLIENT}. Update a client", (0, 4))
        )
        console.print(
            Padding(f"{constante.SALES_VIEW_OWN_CLIENT}. view own client list", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_client_info():
        """Display input prompts to create a new client

        Returns:
            tuple: new client's datas
        """
        while True:
            name = console.input("[bold #ff8133]Name : [/bold #ff8133]")
            if validate_name(name):
                break
        while True:
            firstname = console.input("[bold #ff8133]Firstname : [/bold #ff8133]")
            if validate_name(firstname):
                break
        while True:
            email = console.input("[bold #03d01a]Email : [/bold #03d01a]")
            if validate_email(email):
                break
        while True:
            phone = console.input("[bold #03d01a]Phone : (+33)[/bold #03d01a]")
            if validate_phone_number(phone):
                break
        company = console.input("[bold #03d01a]Client's company : [/bold #03d01a]")
        return name, firstname, email, phone, company

    def update_client_menu():
        """Displays update's client menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]Update Client Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(Padding(f"{constante.CLIENT_UPDATE_EMAIL}. Update email", (0, 4)))
        console.print(Padding(f"{constante.CLIENT_UPDATE_PHONE}. Update phone", (0, 4)))
        console.print(
            Padding(f"{constante.CLIENT_UPDATE_COMPANY}. Update entreprise", (0, 4))
        )
        console.print(Padding(f"{constante.CLIENT_UPDATE_NAME}. Update name", (0, 4)))
        console.print(
            Padding(
                f"{constante.CLIENT_UPDATE_LAST_CONTACT}. Update last contact's date",
                (0, 4),
            )
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SupportClientView:
    @staticmethod
    def show_support_client_menu():
        """Displays support's client menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]Support Client Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SUPPORT_VIEW_CLIENT}. View clients list", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class ClientView:
    @staticmethod
    def show_update_client_menu():
        """Displays update client's menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]Update User Profile [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(Padding(f"{constante.CLIENT_UPDATE_NAME}. Update Name", (0, 4)))
        console.print(
            Padding(f"{constante.CLIENT_UPDATE_FIRSTNAME}. Update Firstname", (0, 4))
        )
        console.print(Padding(f"{constante.CLIENT_UPDATE_EMAIL}. Update Email", (0, 4)))
        console.print(Padding(f"{constante.CLIENT_UPDATE_PHONE}. Update Phone", (0, 4)))
        console.print(
            Padding(f"{constante.CLIENT_UPDATE_COMPANY}. Update Company", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.CLIENT_UPDATE_LAST_CONTACT}. Update last contact date",
                (0, 4),
            )
        )
        console.print(Padding("0. Back to Main Menu", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_client_name():
        """Displays input prompts to get a client new name

        Returns:
            str: name
        """
        while True:
            name = console.input("[bold #ff8133]Enter new Name : [/bold #ff8133]")
            if validate_name(name):
                break
        return name

    @staticmethod
    def get_new_client_firstname():
        """Displays input prompts to get a client new firstname

        Returns:
            str: firstname
        """
        while True:
            firstname = console.input(
                "[bold #ff8133]Enter new Firstame : [/bold #ff8133]"
            )
            if validate_name(firstname):
                break
        return firstname

    @staticmethod
    def get_new_client_email():
        """Displays input prompts to get a client new email

        Returns:
            str: email
        """
        while True:
            email = console.input("[bold #03d01a]Email : [/bold #03d01a]")
            if validate_email(email):
                break
        return email

    @staticmethod
    def get_new_client_phone():
        """Displays input prompts to get a client new phone number

        Returns:
            int: phone number
        """
        while True:
            phone = console.input("[bold #03d01a]Phone : (+33)[/bold #03d01a]")
            if validate_phone_number(phone):
                break
        return phone

    @staticmethod
    def get_new_client_company():
        """Displays input prompts to get a client new company

        Returns:
            str: company name
        """
        while True:
            company = console.input(
                "[bold #ff8133]Enter new company name : [/bold #ff8133]"
            )
            if validate_name(company):
                break
        return company

    @staticmethod
    def get_new_client_last_contact():
        """Displays input prompts to get a client new date of last contact with sales

        Returns:
            date: date of last contact
        """
        while True:
            last_contact = console.input(
                "[bold #ff8133]Enter date of last contact (YYYY-MM-DD): [/bold #ff8133]"
            )
            if validate_date(last_contact):
                break
        return last_contact

    @staticmethod
    def show_create_client_success_message():
        """Displays successfully creating a client"""
        return console.print("[bold blue]Client registered successfully.[/bold blue]")

    @staticmethod
    def get_new_client_contact_id():
        """Displays input prompts to get a client new contact's ID

        Returns:
            int: new sales'ID
        """
        while True:
            new_contact_id = console.input(
                "[bold #03d01a]Enter new contact_ID for this client: [/bold #03d01a]"
            )
            if validate_id(new_contact_id):
                break
        return new_contact_id

    @staticmethod
    def show_update_client_contact_id():
        """Displays successfully updating client's new sales"""
        return console.print("Client's sales updated successfully.")

    @staticmethod
    def get_client_id_for_update():
        """Displays input prompts to get a client's ID

        Returns:
            int: client's ID
        """
        while True:
            client_id = console.input("[bold #03d01a]Enter client_id : [/bold #03d01a]")
            if validate_id(client_id):
                break
        return client_id

    @staticmethod
    def show_update_client_success_message():
        """Displays successfully updating a client"""
        return console.print("Client updated successfully.")

    @staticmethod
    def get_client_id_for_deletion():
        """Displays input prompts to get a client's ID to delete

        Returns:
            int: client's ID
        """
        while True:
            client_id = console.input(
                "[bold #03d01a]Enter the Client ID to delete:  [/bold #03d01a]"
            )
            if validate_id(client_id):
                break
        return int(client_id)

    @staticmethod
    def display_client_list(client_list):
        """Displays list of all clients

        Args:
            client_list (list): list of clients in database
        """
        table = Table(title="List of Clients")

        # Définir les colonnes
        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Name", style="magenta")
        table.add_column("Firstname", style="magenta")
        table.add_column("Company", style="magenta")
        table.add_column("Email", style="green")
        table.add_column("Phone", style="green")
        table.add_column("creation_date", style="#dbe15a")
        table.add_column("last_contact_date", style="#dbe15a")
        table.add_column("contact_id", style="purple")

        # Ajouter les lignes
        for client in client_list:
            table.add_row(
                str(client.client_id),
                client.name,
                client.firstname,
                client.company,
                client.email,
                client.phone,
                str(client.creation_date),
                str(client.last_contact_date),
                str(client.contact_id),
            )

        # Afficher le tableau
        console.print(table)

    @staticmethod
    def show_delete_client_success_message():
        """Displays successfully deleting a client"""
        return console.print("[yellow] Client deleted successfully. [/yellow]")

    @staticmethod
    def show_delete_client_error_message():
        """Displays error message trying to delete a client"""
        return console.print(
            "[italic red]Failed to delete client. Please try again.[/italic red]"
        )

    @staticmethod
    def show_client_error_message():
        """Displays error message trying to create an already existing client"""
        return console.print("[italic red]This client already exists.[/italic red]")
