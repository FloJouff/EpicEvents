from crm.controllers.auth_controller import authenticate, authorize


class UserController:
    def login(self, email, password):
        token = authenticate(email, password)
        if token:
            # Retourner le token ou l'envoyer à la vue
            return token
        else:
            raise Exception("Authentication failed")

    def secure_action(self, token):
        if authorize(token, required_role="gestion"):
            # Effectue l'action sécurisée
            pass
        else:
            raise Exception("This user is not authorized to see this")
