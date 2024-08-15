class ManagementEventView:
    @staticmethod
    def show_manager_event_menu():
        print("\n--- Manager Event Menu ---")
        print("1. View events list")
        print("2. View events with no support")
        print("3. Update an event with no support")
        print("4. Back")
        print("5. Logout")
        return input("Select an option : ")


class SalesEventView:
    @staticmethod
    def show_sales_event_menu():
        print("\n--- Sales Event Menu---")
        print("1. View events list")
        print("2. Create new event")
        print("3. Back")
        print("4. Logout")
        return input("Select an option : ")


class SupportEventtView:
    @staticmethod
    def show_support_event_menu():
        print("\n--- Support Event Menu ---")
        print("1. View events list")
        print("2. View my events list")
        print("3. Update an event")
        print("4. Back")
        print("5. Logout")
        return input("Select an option : ")


def update_event_menu():
    print("\n--- Update Event ---")
    print("1. Update start date")
    print("2. Update end date")
    print("3. Update location")
    print("4. Update attendees")
    print("5. Update Notes")
    print("6. Back")
    print("7. Logout")
    return input("Select an option : ")
