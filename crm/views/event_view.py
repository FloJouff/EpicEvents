import Constantes.constantes as constante
from validators import validate_date, validate_id
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


class AdminEventView:
    @staticmethod
    def show_admin_event_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline] Admin Event Menu [/bold white underline]---",
                    (1, 2),
                )
            )
        )
        console.print(Padding(f"{constante.ADMIN_VIEW_EVENT}. View events list", (0, 4)))
        console.print(
            Padding(f"{constante.ADMIN_CREATE_EVENT}. Create an event", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_UPDATE_EVENT}. Update an event ", (0, 4))
        )
        console.print(
            Padding(f"{constante.ADMIN_DELETE_EVENT}. Delete an event ", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class ManagementEventView:
    @staticmethod
    def show_management_event_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline]Manager Event Menu [/bold white underline]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.MANAGEMENT_VIEW_EVENT}. View events list", (0, 4))
        )
        console.print(
            Padding(
                f"{constante.MANAGEMENT_VIEW_NO_SUPPORT}. View events with no support",
                (0, 4),
            )
        )
        console.print(
            Padding(
                f"{constante.MANAGEMENT_UPDATE_NO_SUPPORT}. Update an event with no support",
                (0, 4),
            )
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SalesEventView:
    @staticmethod
    def show_sales_event_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline]Sales Event Menu [/bold white underline]---",
                    (1, 2),
                )
            )
        )
        console.print(Padding(f"{constante.SALES_VIEW_EVENT}. View events list", (0, 4)))
        console.print(
            Padding(f"{constante.SALES_CREATE_EVENT}. Create new event", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class SupportEventView:
    @staticmethod
    def show_support_event_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline]Support Event Menu [/bold white underline]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(f"{constante.SUPPORT_VIEW_EVENT}. View events list", (0, 4))
        )
        console.print(
            Padding(f"{constante.SUPPORT_VIEW_OWN_EVENT}. View my events list", (0, 4))
        )
        console.print(
            Padding(f"{constante.SUPPORT_UPDATE_EVENT}. Update an event", (0, 4))
        )
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")


class EventView:
    @staticmethod
    def show_update_event_menu():
        console.print(
            Panel.fit(
                Padding(
                    "---[bold white underline]Update Event Menu [/bold white underline]---",
                    (1, 2),
                )
            )
        )
        console.print(
            Padding(
                f"{constante.EVENT_UPDATE_START_DATE}. Update start date (YYYY-MM-DD)",
                (0, 4),
            )
        )
        console.print(
            Padding(
                f"{constante.EVENT_UPDATE_END_DATE}. Update end date (YYYY-MM-DD)",
                (0, 4),
            )
        )
        console.print(
            Padding(f"{constante.EVENT_UPDATE_LOCATION}. Update location", (0, 4))
        )
        console.print(
            Padding(f"{constante.EVENT_UPDATE_ATTENDEES}. Update attendees", (0, 4))
        )
        console.print(Padding(f"{constante.EVENT_UPDATE_NOTES}. Update Notes", (0, 4)))
        console.print(Padding("0. Back", (0, 4)))
        return console.input("[bold #a575ef]Select an option : [/bold #a575ef]")

    @staticmethod
    def get_new_event_info():
        while True:
            client_id = console.input("[bold #03d01a]Client's id :  [/bold #03d01a]")
            if validate_id(client_id):
                break
        while True:
            contract_id = console.input("[bold #03d01a]Contract's id :  [/bold #03d01a]")
            if validate_id(contract_id):
                break
        while True:
            start_date = console.input(
                "[bold #03d01a]Starting date (YYYY-MM-DD): [/bold #03d01a]"
            )
            if validate_date(start_date):
                break
        while True:
            end_date = console.input(
                "[bold #03d01a]Ending date (YYYY-MM-DD): [/bold #03d01a]"
            )
            if validate_date(end_date):
                break
        location = console.input("[bold #03d01a]Location : [/bold #03d01a]")
        attendees = console.input("[bold #03d01a]Attendees : [/bold #03d01a]")
        return client_id, contract_id, start_date, end_date, location, attendees

    @staticmethod
    def get_new_event_start_date():
        while True:
            start_date = console.input(
                "[bold #03d01a]Enter New starting date (YYYY-MM-DD): [/bold #03d01a]"
            )
            if validate_date(start_date):
                return start_date

    @staticmethod
    def get_new_event_end_date():
        while True:
            end_date = console.input(
                "[bold #03d01a]Enter New ending date (YYYY-MM-DD): [/bold #03d01a]"
            )
            if validate_date(end_date):
                return end_date

    @staticmethod
    def get_new_location():
        return console.input("[bold #03d01a]Enter new location: [/bold #03d01a]")

    @staticmethod
    def get_new_attenddes():
        return console.input("[bold #03d01a]Enter new attendees: [/bold #03d01a]")

    @staticmethod
    def get_new_event_notes():
        return console.input("[bold #03d01a]Enter your notes: [/bold #03d01a]")

    @staticmethod
    def get_new_support_id():
        while True:
            support_id = console.input(
                "[bold #03d01a]Enter the Support ID for this event: [/bold #03d01a]"
            )
            if validate_id(support_id):
                break
        return int(support_id)

    @staticmethod
    def get_event_id_for_deletion():
        while True:
            event_id = console.input(
                "[bold #03d01a]Enter the event ID to delete:  [/bold #03d01a]"
            )
            if validate_id(event_id):
                break
        return int(event_id)

    @staticmethod
    def get_no_support_event_info():
        while True:
            event_id = console.input("[bold #03d01a]Event's id : [/bold #03d01a]")
            if validate_id(event_id):
                break
        while True:
            support_id = console.input(
                "[bold #03d01a]Enter the Support ID for this event: [/bold #03d01a]"
            )
            if validate_id(support_id):
                break
        return event_id, support_id

    @staticmethod
    def get_event_id():
        while True:
            event_id = console.input("[bold #03d01a]Event's id : [/bold #03d01a]")
            if validate_id(event_id):
                break
        return int(event_id)

    @staticmethod
    def show_delete_event_success(event_id):
        return console.print(
            f"[yellow]Event with ID [bold]{event_id}[/bold] has been deleted successfully [/yellow]"
        )

    @staticmethod
    def show_delete_event_error():
        return console.print(
            "[italic red]Failed to delete Event. Please try again.[/italic red]"
        )

    @staticmethod
    def show_update_event_error():
        return console.print(
            "[italic red]Failed to update Event. Please try again.[/italic red]"
        )

    @staticmethod
    def show_update_event_success():
        return console.print("[yellow] Event updated successfully [/yellow]")

    @staticmethod
    def show_acces_event_denied():
        return console.print(
            "[italic red]Acces denied : you're not assigned to this event.[/italic red]"
        )

    @staticmethod
    def show_new_support_affected():
        return console.print(
            "[yellow] New support affected successfully to this event. [/yellow]"
        )

    @staticmethod
    def show_no_support_list(event_list):
        table = Table(title="List of Events with no support")

        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Client ID", style="magenta")
        table.add_column("Contract ID", style="magenta")
        table.add_column("Support ID", style="magenta")
        table.add_column("Start Date", style="green")
        table.add_column("End Date", style="green")
        table.add_column("Location", style="yellow")
        table.add_column("Attendees", style="yellow")
        table.add_column("Notes", style="grey")

        for event in event_list:
            table.add_row(
                str(event.event_id),
                str(event.client_id),
                str(event.contract_id),
                str(event.support_id),
                str(event.start_date),
                str(event.end_date),
                event.location,
                str(event.attendees),
                event.notes,
            )

        console.print(table)

    @staticmethod
    def display_event_list(event_list):
        table = Table(title="List of Events")

        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Client ID", style="magenta")
        table.add_column("Contract ID", style="magenta")
        table.add_column("Support ID", style="magenta")
        table.add_column("Start Date", style="green")
        table.add_column("End Date", style="green")
        table.add_column("Location", style="yellow")
        table.add_column("Attendees", style="yellow")
        table.add_column("Notes", style="white")

        for event in event_list:
            table.add_row(
                str(event.event_id),
                str(event.client_id),
                str(event.contract_id),
                str(event.support_id),
                str(event.start_date),
                str(event.end_date),
                event.location,
                str(event.attendees),
                event.notes,
            )

        console.print(table)

    @staticmethod
    def event_not_found():
        return console.print("[italic red]Event not found.[/italic red]")
