import Constantes.constantes as constante
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from validators import validate_id, validate_number


custom_theme = Theme(
    {
        "": "#8896cb",
    }
)
console = Console(theme=custom_theme)


class AdminContractView:
    @staticmethod
    def show_admin_contract_menu():
        """Display contract menu for admin user"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Manager Contract Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.ADMIN_VIEW_CONTRACT}. View contracts list", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_CREATE_CONTRACT}. Create new contract", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_UPDATE_CONTRACT}. Update a contrat", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_DELETE_CONTRACT}. Delete a contract", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class ManagementContractView:
    @staticmethod
    def show_management_contract_menu():
        """Display contract menu for management user"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Manager Contract Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_VIEW_CONTRACT}. View contracts list", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.MANAGEMENT_CREATE_CONTRACT}. Create new contract", (0, 4)
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_UPDATE_CONTRACT}. Update a contrat", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SalesContractView:
    @staticmethod
    def show_sales_contract_menu():
        """Display contract menu for sales users"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Sales Contrat Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SALES_VIEW_CONTRACT}. View contracts list", (0, 4))
        )
        # console.print(
        #     Padding(f"{constante.SALES_CREATE_CONTRACT}. Create new contract", (0, 4))
        # )
        console.print(
            Padding(f"{constante.SALES_UPDATE_OWN_CONTRACT}. Update a contrat", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.SALES_UNSIGNED_CONTRACT}. View unsigned contracts", (0, 4)
            )
        )
        console.print(
            Padding(
                f"{constante.SALES_UNPAID_CONTRACT}. View contracts with remaining amount",
                (0, 4),
            )
        )
        console.print(
            Padding(
                f"{constante.SALES_VIEW_OWN_CONTRACT}. View your contracts list", (0, 4)
            )
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def show_sales_update_contract_menu():
        """Display update contract menu for sales users"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Update Contract [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.CONTRACT_UPDATE_CLIENT}. Update Client_id", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_STATUS}. Change contract's status (signed)",
                (0, 4),
            )
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_REMAIN}. Update total outstanding cost",
                (0, 4),
            )
        )
        console.print(Padding("0. Back to Main Menu", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SupportContractView:
    @staticmethod
    def show_support_contract_menu():
        """Display contract menu for support users"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Support contract Menu [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SUPPORT_VIEW_CONTRACT}. View contracts list", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class ContractView:
    @staticmethod
    def update_contract_menu():
        """Display update contract menu for admin or management users"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white] Update contract [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.CONTRACT_UPDATE_CLIENT}. Update client", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_STATUS}. Update contract's status", (0, 4)
            )
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_REMAIN}. Update remaining amount", (0, 4)
            )
        )
        console.print(
            Padding(f"{constante.CONTRACT_UPDATE_SALES}. Update contract's sale", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_contract_info():
        """Display input lignes to get new contract informations"""
        while True:
            client_id = console.input("[bold #03d01a]Client's id :[/bold #03d01a]")
            if validate_id(client_id):
                break
        while True:
            commercial_id = console.input("[bold #03d01a]Sales's id : [/bold #03d01a]")
            if validate_id(commercial_id):
                break
        total_amount = console.input("[bold #03d01a]total cost : [/bold #03d01a]")
        return client_id, commercial_id, total_amount

    @staticmethod
    def show_update_contract_menu():
        """Display update contract menu"""
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white]- Update Contract [/bold white]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.CONTRACT_UPDATE_CLIENT}. Update Client_id", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_STATUS}. Change contract's status (signed)",
                (0, 4),
            )
        )
        console.print(
            Padding(
                f"{constante.CONTRACT_UPDATE_REMAIN}. Update total outstanding cost",
                (0, 4),
            )
        )
        console.print(
            Padding(f"{constante.CONTRACT_UPDATE_SALES}. Update Sales_id", (0, 4))
        )
        console.print(Padding("0. Back to Main Menu", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_contract_client_id():
        """Display input ligne to get new contract client's ID informations"""
        while True:
            client_id = console.input(
                "[bold #03d01a]Enter new client_id: [/bold #03d01a]"
            )
            if validate_id(client_id):
                break
        return client_id

    @staticmethod
    def get_new_contract_remain_cost():
        """Display input ligne to get new contract outstanding cost"""
        while True:
            remain_cost = console.input(
                "[bold #03d01a]Enter the new outstanding amount of this contract:[/bold #03d01a]"
            )
            if validate_number(remain_cost):
                break
        return int(remain_cost)

    @staticmethod
    def get_new_status():
        """Display input ligne to confirm update of contract status"""
        while True:
            response = (
                console.input(
                    "[bold #03d01a]If contract is signed, press [bold yellow] 'Y' [/bold yellow] or [bold yellow] 'y' [/bold yellow]: [/bold #03d01a]"
                )
                .strip()
                .lower()
            )

            if response in ["y"]:
                return response
            else:
                console.print(
                    "[bold red]Invalid input. Please enter 'Y' or 'y'.[/bold red]"
                )

    @staticmethod
    def get_new_contract_contact_id():
        """Display input ligne to get new contract contact's ID"""
        while True:
            commercial_id = console.input(
                "[bold #03d01a]Enter sales in charge of this contract: [/bold #03d01a]"
            )
            if validate_id(commercial_id):
                break
        return commercial_id

    @staticmethod
    def get_contract_id_for_deletion():
        """Displays the command line for entering the id of the contract to be deleted"""
        while True:
            contract_id = console.input(
                "[bold #03d01a]Enter the Contract ID to delete: [/bold #03d01a]"
            )
            if validate_id(contract_id):
                break
        return str(contract_id)

    @staticmethod
    def get_contract_id():
        """Displays the command line for entering the id of the contract"""
        return console.input("[bold #03d01a]Enter contract_id : [/bold #03d01a]")

    @staticmethod
    def show_create_contract_success():
        """Displays message to confirm contract has been created successfully"""
        return console.print("[yellow] Contract registered successfully. [/yellow]")

    @staticmethod
    def show_update_contract_success():
        """Displays message to confirm contract has been updated successfully"""
        return console.print("[yellow]Contract updated successfully[/yellow]")

    @staticmethod
    def show_update_contract_noaccess():
        """Displays message to inform a sales thzt he is not in charge of this contract"""
        return console.print(
            "[italic red] You're not in charge of this contract. You are not allowed to update it.[/italic red]"
        )

    @staticmethod
    def display_contract_list(contract_list):
        """Displays contract's list"""
        table = Table(title="List of contracts")

        table.add_column("ID", style="cyan", justify="right")
        table.add_column("client_id", style="magenta")
        table.add_column("commercial_id", style="magenta")
        table.add_column("total_amount", style="green")
        table.add_column("remain_amount", style="green")
        table.add_column("creation_date", style="#dbe15a")
        table.add_column("is_signed", style="purple")

        for contract in contract_list:
            table.add_row(
                str(contract.contract_id),
                str(contract.client_id),
                str(contract.commercial_id),
                str(contract.total_amount),
                str(contract.remain_amount),
                str(contract.creation_date),
                str(contract.is_signed),
            )

        console.print(table)

    @staticmethod
    def contract_not_found():
        """Displays error message if contract does not exists or is not found"""
        return console.print("[italic red]Contract not found.[/italic red]")

    @staticmethod
    def display_unsold_contract_list(contract_list):
        """Displays list of unsold contracts"""
        table = Table(title="List of unsold contracts")

        table.add_column("ID", style="cyan", justify="right")
        table.add_column("client_id", style="magenta")
        table.add_column("commercial_id", style="magenta")
        table.add_column("total_amount", style="green")
        table.add_column("remain_amount", style="green")
        table.add_column("creation_date", style="#dbe15a")
        table.add_column("is_signed", style="purple")

        for contract in contract_list:
            table.add_row(
                str(contract.contract_id),
                str(contract.client_id),
                str(contract.commercial_id),
                str(contract.total_amount),
                str(contract.remain_amount),
                str(contract.creation_date),
                str(contract.is_signed),
            )

        console.print(table)

    @staticmethod
    def show_invalid_answer():
        """Displays an error message if a user input does not correspond to the expected format"""
        return console.print("[italic red]Invalid answer. Please try again[/italic red]")
