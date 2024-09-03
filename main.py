from crm.database import init_db
from crm.controllers.main_controller import run_main_menu
from sentry import init_sentry

init_sentry()


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    run_main_menu()
