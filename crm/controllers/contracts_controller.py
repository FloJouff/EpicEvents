from crm.database import Session
from crm.models import Contract
from datetime import datetime
import uuid

from crm.controllers.permissions import requires_permission


def view_contract():
    session = Session()
    contract_list = session.query(Contract).all()
    for contract in contract_list:
        print(f"Liste des contrats : {contract}")


def view_user_contracts(user_id):
    session = Session()
    user_contract_list = (
        session.query(Contract).filter_by(commercial_id=user_id).all()
    )
    for contract in user_contract_list:
        print(f"Liste des évènements : {contract}")


####################################################
####################################################


@requires_permission("create_contract")
def create_contract(
    client_id, total_amount, is_signed=False, contract_id=uuid
):
    session = Session()
    try:
        existing_contract = (
            session.query(Contract).filter_by(contract_id=contract_id).first()
        )
        if existing_contract:
            print("This contract already exists.")
            return False

        new_contract = Contract(
            client_id=client_id,
            creation_date=datetime.now(),
            total_amount=total_amount,
            is_signed=is_signed,
            remain_amount=total_amount,
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
