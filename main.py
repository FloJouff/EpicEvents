from crm.database import init_db
# from crm.views.main_view import main_menu
from crm.controllers.main_controller import run_main_menu


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    run_main_menu()
