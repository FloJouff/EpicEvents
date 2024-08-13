from crm.database import init_db
import getpass
from crm.controllers.auth_controller import (
    authenticate,
    authorize,
    register_user,
)


def main_menu():
    while True:
        print("\n--- CRM Authentication System ---")
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            username = input("Entrez un nom d'utilisateur : ")
            password = getpass.getpass("Entrez un mot de passe : ")
            register_user(username, password)
        elif choice == "2":
            email = input("Email de l'utilisateur : ")
            password = getpass.getpass("Mot de passe : ")
            if authenticate(email, password):
                print("Connexion réussie. Accès au CRM...")
                # Ici, vous pouvez ajouter la logique pour accéder au CRM
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    main_menu()
