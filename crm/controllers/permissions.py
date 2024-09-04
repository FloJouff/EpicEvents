from functools import wraps
from Constantes.permissions import PERMISSIONS, Role


def requires_permission(task):
    """Decorator to give permissions to user

    Args:
        task (str): task needed permission
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "current_user_role_id" in kwargs:
                current_user_role_id = kwargs["current_user_role_id"]
            elif args:
                current_user_role_id = args[0]
            else:
                print("Role ID not provided. Permission denied")
                return None

            if not current_user_role_id:
                print("Role ID not provided or invalid. Permission denied.")
                return None

            try:
                current_user_role = Role(str(current_user_role_id))
            except ValueError:
                print(f"Invalide role ID: {current_user_role_id}. Permission denied")
                return None

            allowed_roles = PERMISSIONS.get(task, [])

            if current_user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                print(
                    f"Permission denied: Role {current_user_role_id} does not have permission for {task}"
                )
                return None

        return wrapper

    return decorator
