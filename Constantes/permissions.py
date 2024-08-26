from enum import Enum


class Role(Enum):
    GESTION = "1"
    COMMERCIAL = "2"
    SUPPORT = "3"
    ADMIN = "4"


PERMISSIONS = {
    "create_user": [Role.ADMIN, Role.GESTION],
    "view_user": [Role.ADMIN, Role.GESTION],
    "update_user": [Role.ADMIN, Role.GESTION],
    "delete_user": [Role.ADMIN, Role.GESTION],
    "create_client": [Role.COMMERCIAL],
    "view_clients": [Role.ADMIN, Role.GESTION, Role.COMMERCIAL, Role.SUPPORT],
    "update_client": [Role.ADMIN, Role.COMMERCIAL],
    "update_own_clients": [Role.ADMIN, Role.COMMERCIAL],
    "update_client_sales": [Role.ADMIN, Role.GESTION],
    "delete_client": [Role.ADMIN],
    "create_contract": [Role.ADMIN, Role.GESTION],
    "view_contracts": [Role.ADMIN, Role.GESTION, Role.COMMERCIAL, Role.SUPPORT],
    "update_contract": [Role.ADMIN, Role.GESTION],
    "update_own_contract": [Role.COMMERCIAL],
    "create_event": [Role.ADMIN, Role.GESTION, Role.COMMERCIAL],
    "view_events": [Role.ADMIN, Role.GESTION, Role.COMMERCIAL, Role.SUPPORT],
    "update_event": [Role.ADMIN, Role.GESTION],
    "update_assigned_events": [Role.ADMIN, Role.SUPPORT],
}
