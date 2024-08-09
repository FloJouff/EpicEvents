from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from crm.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column("role_id", Integer, primary_key=True)
    role = Column(
        "role", Enum("gestion", "commercial", "support"), unique=True
    )
    users = relationship("User", back_populates="role")

    def __init__(
        self,
        role_id,
        role,
    ):
        """Role constructor

        Args:
            role_id(int):
            role (Enum): event's contract's id


        """
        self.role_id = role_id
        self.role = role

    def __repr__(self):
        return f"Role: {self.role}"

    def has_permissions(self):
        if self.role == "gestion":
            return {
                "create_user": True,
                "view_user": True,
                "edit_user": True,
                "delete_user": True,
                "create_clients": False,
                "view_clients": True,
                "edit_own_clients": False,
                "create_event": True,
                "view_events": True,
                "create_contracts": True,
                "view_contracts": True,
                "edit_contracts": True,
                "edit_events": True,
                "edit_assigned_events": False,
            }
        elif self.role == "commercial":
            return {
                "create_user": False,
                "view_user": False,
                "edit_user": False,
                "delete_user": False,
                "create_clients": True,
                "view_clients": True,
                "edit_own_clients": True,
                "create_event": True,
                "view_events": True,
                "create_contracts": False,
                "view_contracts": True,
                "edit_contracts": True,
                "edit_events": False,
                "edit_assigned_events": False,
            }
        elif self.role == "support":
            return {
                "create_user": False,
                "view_user": False,
                "edit_user": False,
                "delete_user": False,
                "create_clients": True,
                "view_clients": True,
                "edit_own_clients": False,
                "create_event": False,
                "view_events": True,
                "create_contracts": False,
                "view_contracts": True,
                "edit_contracts": True,
                "edit_events": False,
                "edit_assigned_events": True,
            }
        else:
            return {}
