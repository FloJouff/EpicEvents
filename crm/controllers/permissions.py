from functools import wraps
from Constantes.permissions import PERMISSIONS


def requires_permission(task):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "current_user_role_id" in kwargs:
                current_user_role_id = kwargs["current_user_role_id"]
            elif args:
                current_user_role_id = args[0]
            else:
                print("Role ID not provided. Permission denied.")
                return None

            allowed_roles = PERMISSIONS.get(task, [])

            if str(current_user_role_id) in allowed_roles:
                return func(*args, **kwargs)
            else:
                print(
                    f"Permission denied: Role {current_user_role_id} does not have permission for {task}"
                )
                return None

        return wrapper

    return decorator
