from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    Date,
)
from crm.database import Base
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(
        "client_id", Integer, primary_key=True, autoincrement=True
    )
    name = Column("name", String(65))
    firstname = Column("fisrtname", String(65))
    email = Column("email", String(255), unique=True)
    phone = Column("phone", String(255))
    company = Column("company", String(65))
    creation_date = Column("creation_date", Date)
    last_contact_date = Column("last_contact_date", Date)
    contact_id = Column(
        "contact_id", ForeignKey("users.user_id", ondelete="SET NULL")
    )

    contracts = relationship("Contract", back_populates="client")

    def __init__(
        self,
        client_id,
        name,
        firstname,
        email,
        phone,
        company,
        creation_date,
        last_contact_date,
        contact_id,
    ):
        """Client constructor

        Args:
            client_id (int): client.id
            name (str): client's name
            first_name (str): client's first_name
            email (str): client's email
            phone (int): client's date_of_birth
            company (str): client's company
            creation_date (date): first contact_date with client
            last_contact_date (date): date of last update
            contact_id (str): id of teamuser in charge of this client

        """
        self.client_id = client_id
        self.name = name
        self.firstname = firstname
        self.email = email
        self.phone = phone
        self.company = company
        self.creation_date = creation_date
        self.last_contact_date = last_contact_date
        self.contact_id = contact_id

    def __repr__(self):
        return f"Client: {self.name} {self.firstname} from {self.company}"
