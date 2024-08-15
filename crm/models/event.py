from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
)
from crm.models import Base
from sqlalchemy.orm import relationship
from crm.models.contract import Contract


class Event(Base):
    __tablename__ = "events"

    event_id = Column(
        "event_id", Integer, primary_key=True, autoincrement=True
    )
    contract_id = Column(
        "contract_id",
        String(65),
        ForeignKey("contracts.contract_id", ondelete="SET NULL"),
    )
    client_id = Column(
        "client_id",
        Integer,
        ForeignKey("clients.client_id", ondelete="SET NULL"),
    )
    support_id = Column(
        "support_id", Integer, ForeignKey("users.user_id", ondelete="SET NULL")
    )
    start_date = Column("start_date", DateTime)
    end_date = Column("end_date", DateTime)
    location = Column("location", String(1000))
    attendees = Column("attendees", Integer)
    notes = Column("notes", String(255))

    contract = relationship("Contract", back_populates="events")
    # user = relationship("User", back_populates="events")
    client = relationship("Client")

    def __init__(
        self,
        contract_id,
        client_id,
        support_id,
        start_date,
        end_date,
        location,
        attendees,
        notes,
    ):
        """Event constructor

        Args:
            contract_id (int): event's contract's id
            client_id (int): event's client's id
            support_id (int): client's contact in EpicEvents
            start_date (date): event starting date
            end_date (date): event ending date
            location (str): event's location
            attendees (int): number of attendees
            note (str): additionnal notes

        """

        self.client_id = client_id
        self.contract_id = contract_id
        self.support_id = support_id
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.attendees = attendees
        self.notes = notes

    def __repr__(self):
        return f"Event: event from {self.client_id}. User in charge: {self.support_id}"
