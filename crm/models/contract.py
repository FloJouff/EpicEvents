import uuid
from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    DateTime,
    Boolean,
    String,
)
from crm.models import Base
from sqlalchemy.orm import relationship
from crm.models.client import Client


def generate_uuid():
    return str(uuid.uuid4())


class Contract(Base):
    __tablename__ = "contracts"

    contract_id = Column(
        "contract_id", String(65), primary_key=True, default=generate_uuid
    )
    client_id = Column(
        "client_id",
        Integer,
        ForeignKey("clients.client_id", ondelete="SET NULL"),
    )
    commercial_id = Column(
        "commercial_id",
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL"),
    )
    total_amount = Column("total_amount", Integer)
    remain_amount = Column("remain_amount", Integer)
    creation_date = Column("creation_date", DateTime)
    is_signed = Column("is_signed", Boolean)

    client = relationship("Client", back_populates="contracts")
    events = relationship("Event", back_populates="contract")

    def __init__(
        self,
        client_id,
        commercial_id,
        total_amount,
        remain_amount,
        creation_date,
        contract_status,
        # contract_id=uuid,
    ):
        """Contract constructor

        Args:
            client_id (int): client.id
            commercial_id (int): user in charge of this client
            first_name (str): client's first_name
            email (str): client's email
            phone (int): client's date_of_birth
            company (str): client's company
            creation_date (date): first contact_date with client
            last_contact_date (date): date of last update
            contact_name (str): name of teamuser in charge of this client

        """
        # self.contract_id = contract_id
        self.client_id = client_id
        self.commercial_id = commercial_id
        self.total_amount = total_amount
        self.remain_amount = remain_amount
        self.creation_date = creation_date
        self.contract_status = contract_status

    def __repr__(self):
        return f"Contract: {self.id} from {self.client_id}. User in charge: {self.commercial_id}"


# Client.contracts = relationship(
#     "Contract", order_by=Contract.contract_id, back_populates="client"
# )
