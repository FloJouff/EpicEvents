class ManagementContractView:
    @staticmethod
    def show_management_contract_menu():
        print("\n--- Manager Contract Menu ---")
        print("1. View contracts list")
        print("2. Create new contract")
        print("3. Update a contrat")
        print("4. Back")
        print("5. Logout")
        return input("Select an option : ")


class SalesContractView:
    @staticmethod
    def show_sales_contract_menu():
        print("\n--- Sales Contrat Menu---")
        print("1. View contracts list")
        print("2. Create new contract")
        print("3. Update a contrat")
        print("4. View unsigned contracts")
        print("5. View contracts with remaining amount")
        print("6. Back")
        print("7. Logout")
        return input("Select an option : ")


class SupportContractView:
    @staticmethod
    def show_support_contract_menu():
        print("\n--- Support contract Menu ---")
        print("1. View contracts list")
        print("2. Back")
        print("3. Logout")
        return input("Select an option : ")


def update_contract_menu():
    print("\n--- Update contract ---")
    print("1. Update client")
    print("2. Update contract's sale")
    print("3. Update contract's status")
    print("4. Update remaining amount")
    print("5. Back")
    print("6. Logout")
    return input("Select an option : ")
