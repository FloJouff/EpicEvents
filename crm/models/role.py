from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from crm.models import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column("role_id", Integer, primary_key=True)
    role = Column(
        "role", Enum("gestion", "commercial", "support", "admin"), unique=True
    )
    users = relationship("User", back_populates="role")

    def __init__(self, role_id, role):
        """Role constructor

        Args:
            role_id(int):
            role (Enum): event's contract's id


        """
        self.role_id = role_id
        self.role = role

    def __repr__(self):
        return f"Role: {self.role}"
