import Constantes.constantes as constante


class AdminContractView:
    @staticmethod
    def show_admin_contract_menu():
        print("\n--- Manager Contract Menu ---")
        print(f"{constante.ADMIN_VIEW_CONTRACT}. View contracts list")
        print(f"{constante.ADMIN_CREATE_CONTRACT}. Create new contract")
        print(f"{constante.ADMIN_UPDATE_CONTRACT}. Update a contrat")
        print(f"{constante.ADMIN_DELETE_CONTRACT}. Delete a contract")
        print("0. Back")
        return input("Select an option : ")


class ManagementContractView:
    @staticmethod
    def show_management_contract_menu():
        print("\n--- Manager Contract Menu ---")
        print(f"{constante.MANAGEMENT_VIEW_CONTRACT}. View contracts list")
        print(f"{constante.MANAGEMENT_CREATE_CONTRACT}. Create new contract")
        print(f"{constante.MANAGEMENT_UPDATE_CONTRACT}. Update a contrat")
        print("0. Back")
        return input("Select an option : ")


class SalesContractView:
    @staticmethod
    def show_sales_contract_menu():
        print("\n--- Sales Contrat Menu---")
        print(f"{constante.SALES_VIEW_CONTRACT}. View contracts list")
        print(f"{constante.SALES_CREATE_CONTRACT}. Create new contract")
        print(f"{constante.SALES_UPDATE_CONTRACT}. Update a contrat")
        print(f"{constante.SALES_UNSIGNED_CONTRACT}. View unsigned contracts")
        print(f"{constante.SALES_UNPAID_CONTRACT}. View contracts with remaining amount")
        print("0. Back")
        return input("Select an option : ")


class SupportContractView:
    @staticmethod
    def show_support_contract_menu():
        print("\n--- Support contract Menu ---")
        print(f"{constante.SUPPORT_VIEW_CONTRACT}. View contracts list")
        print("0. Back")
        return input("Select an option : ")


class ContractView:
    @staticmethod
    def update_contract_menu():
        print("\n--- Update contract ---")
        print(f"{constante.CONTRACT_UPDATE_CLIENT}. Update client")
        print(f"{constante.CONTRACT_UPDATE_SALES}. Update contract's sale")
        print(f"{constante.CONTRACT_UPDATE_STATUS}. Update contract's status")
        print(f"{constante.CONTRACT_UPDATE_REMAIN}. Update remaining amount")
        print("0. Back")
        return input("Select an option : ")

    @staticmethod
    def get_new_contract_info():
        client_id = input("Client's id : ")
        sales_id = input("Sales's id : ")
        total_amount = input("total cost : ")
        return client_id, sales_id, total_amount
