from crm.database import Session
from crm.models import Contract

# from crm.controllers.permissions import requires_permission


def view_contract():
    session = Session()
    contract_list = session.query(Contract).all()
    for contract in contract_list:
        print(f"Liste des contrats : {contract}")
