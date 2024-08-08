from sqlalchemy import Column, String, Integer
from crm.database import Base


class Role(Base):
    MANAGER = "MANAGER"
    SUPPORT = "SUPPORT"
    SALES = "SALES"

    ROLE_CHOICES = (
        (MANAGER, "gestion"),
        (SUPPORT, "support"),
        (SALES, "commercial"),
    )

    __tablename__ = "roles"

    role_id = Column("role_id", Integer, primary_key=True, autoincrement=True)
    role_choice = Column("role_choice", String(65), unique=True)

    def __init__(
        self,
        role_id,
        role_choice,
    ):
        """Role constructor

        Args:
            role_id (int): event.id
            role_choice (int): event's contract's id


        """

        self.role_id = role_id
        self.role_choice = role_choice
