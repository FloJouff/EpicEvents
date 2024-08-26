from crm.database import Session
from crm.models import Contract
from datetime import datetime
import uuid
from crm.views import contract_view
from crm.controllers.permissions import requires_permission
import Constantes.constantes as constante


def view_contract():
    session = Session()
    contract_list = session.query(Contract).all()
    for contract in contract_list:
        print(f"Liste des contrats : {contract}")


def view_user_own_contracts(user_id):
    session = Session()
    user_contract_list = (
        session.query(Contract).filter_by(commercial_id=user_id).all()
    )
    for contract in user_contract_list:
        print(f"Liste des évènements : {contract}")


@requires_permission("create_contract")
def create_contract(
    client_id,
    commercial_id,
    total_amount,
    current_user_role_id,
):
    session = Session()
    try:
        # existing_contract = (
        #     session.query(Contract).filter_by(contract_id=contract_id).first()
        # )
        # if existing_contract:
        #     print("This contract already exists.")
        #     return False

        new_contract = Contract(
            contract_id=str(uuid.uuid4()),
            client_id=client_id,
            commercial_id=commercial_id,
            total_amount=total_amount,
            remain_amount=total_amount,
            creation_date=datetime.now(),
            is_signed=False,
        )

        session.add(new_contract)
        session.commit()
        print("Contract registered successfully.")
        return True
    except Exception as e:
        print(f"Error during registration: {e}")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("update_contract")
def update_contract(
    user_id,
    contract_id,
    client_id=None,
    commercial_id=None,
    remain_amount=None,
    is_signed=None,
):
    session = Session()
    try:
        contract = session.query(Contract).filter_by(contract_id=contract_id).first()
        if not contract:
            print("Contract not found.")
            return False
        if client_id:
            contract.client_id = client_id
        if commercial_id:
            contract.commercial_id = commercial_id
        if remain_amount:
            contract.remain_amount = remain_amount
        if is_signed:
            contract.is_signed = True

        session.commit()
        print("Contract updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        session.rollback()
        return False
    finally:
        session.close()


@requires_permission("update_own_contract")
def update_own_contract(
    user_id,
    contract_id,
    client_id=None,
    commercial_id=None,
    remain_amount=None,
    is_signed=None,
):
    session = Session()

    try:
        contract = session.query(Contract).filter_by(contract_id=contract_id).first()

        if not contract:
            print("Contract not found.")
            return False
        if contract.commercial_id == user_id:
            if client_id:
                contract.client_id = client_id
            if commercial_id:
                contract.commercial_id = commercial_id
            if remain_amount:
                contract.remain_amount = remain_amount
            if is_signed:
                contract.is_signed = True

        else:
            print(
                "You're not in charge of this contract. You are not allowed to update it."
            )

        session.commit()
        print("Contract updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating contract: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def delete_contract(user_id, contract_id):
    session = Session()
    try:
        contract = session.query(Contract).filter_by(contract_id=contract_id).first()
        if not contract:
            print(f"User with id {contract_id} not found")
            return False
        session.delete(contract)
        session.commit()
        print(f"Contract with ID {contract_id} has been deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting contract: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def view_unsigned_contract():
    session = Session()
    unsigned_contract_list = session.query(Contract).filter_by(is_signed=False).all()
    for contract in unsigned_contract_list:
        print(f"List of unsigned contracts : {contract}")


def view_unpaid_contract():
    session = Session()
    unpaid_contract_list = (
        session.query(Contract).filter(Contract.remain_amount != 0).all()
    )
    for contract in unpaid_contract_list:
        print(f"List of unsolded contracts : {contract}")


def update_contract_menu(user_id, contract_id):
    while True:
        update_contract_choice = contract_view.ContractView.show_update_contract_menu()
        if update_contract_choice == constante.CONTRACT_UPDATE_CLIENT:
            new_client = contract_view.ContractView.get_new_contract_client_id()
            update_contract(user_id, contract_id, client_id=new_client)
        elif update_contract_choice == constante.CONTRACT_UPDATE_SALES:
            new_sales_id = contract_view.ContractView.get_new_contract_contact_id()
            update_contract(user_id, contract_id, commercial_id=new_sales_id)
        elif update_contract_choice == constante.CONTRACT_UPDATE_STATUS:
            new_status = contract_view.ContractView.get_new_status()
            if new_status == "Y" or "y":
                update_contract(user_id, contract_id, is_signed=True)
        elif update_contract_choice == constante.CONTRACT_UPDATE_REMAIN:
            new_total_remain = contract_view.ContractView.get_new_contract_remain_cost()
            update_contract(user_id, contract_id, remain_amount=new_total_remain)
        elif update_contract_choice == "0":
            break


def update_own_contract_menu(user_id, contract_id):
    while True:
        update_contract_choice = (
            contract_view.SalesContractView.show_sales_update_contract_menu()
        )
        if update_contract_choice == constante.CONTRACT_UPDATE_CLIENT:
            new_client = contract_view.ContractView.get_new_contract_client_id()
            update_own_contract(user_id, contract_id, client_id=new_client)
        elif update_contract_choice == constante.CONTRACT_UPDATE_STATUS:
            new_status = contract_view.ContractView.get_new_status()
            if new_status == "Y" or "y":
                update_own_contract(user_id, contract_id, is_signed=True)
        elif update_contract_choice == constante.CONTRACT_UPDATE_REMAIN:
            new_total_remain = contract_view.ContractView.get_new_contract_remain_cost()
            update_own_contract(user_id, contract_id, remain_amount=new_total_remain)
        elif update_contract_choice == "0":
            break
