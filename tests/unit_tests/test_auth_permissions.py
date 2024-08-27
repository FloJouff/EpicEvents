import pytest
from pytest_mock import mocker
from crm.controllers.auth_controller import authenticate
from crm.controllers.permissions import requires_permission
from crm.models.user import User
from argon2 import PasswordHasher
import Constantes.constantes as constante
import pytest
from datetime import datetime, timedelta
import jwt
from crm.controllers.main_controller import MainController
from crm.views.main_view import MainView


@pytest.fixture
def mock_view(mocker):
    return mocker.Mock(spec=MainView)


@pytest.fixture
def mock_jwt_decode(mocker):
    return mocker.patch("jwt.decode")


@pytest.fixture
def controller(mock_view):
    controller = MainController()
    controller.view = mock_view
    return controller


def test_main_menu_logout(controller, mocker):
    # Simuler un utilisateur déjà connecté
    controller.token = "fake_token"
    controller.role_id = 1
    controller.user_id = "fake_user_id"
    controller.token_expiry = datetime.now() + timedelta(hours=1)

    # Simuler une séquence de choix : d'abord déconnexion, puis quitter
    controller.view.show_main_menu.side_effect = [constante.DISCONNECT, "0"]

    # Patcher handle_disconnection pour simuler la déconnexion
    def mock_disconnect():
        controller.token = None
        controller.role_id = None
        controller.user_id = None
        controller.token_expiry = None

    mock_handle_disconnection = mocker.patch.object(
        controller, "handle_disconnection", side_effect=mock_disconnect
    )

    # Exécuter main_menu
    controller.main_menu()

    # Vérifications
    assert controller.view.show_main_menu.call_count == 2
    controller.view.show_main_menu.assert_any_call(
        True
    )  # Premier appel avec utilisateur connecté
    controller.view.show_main_menu.assert_any_call(
        False
    )  # Deuxième appel après déconnexion
    mock_handle_disconnection.assert_called_once()
    controller.view.show_exit_message.assert_called_once()

    # Vérifier que l'utilisateur est bien déconnecté
    assert controller.token is None
    assert controller.role_id is None
    assert controller.user_id is None
    assert controller.token_expiry is None


def test_main_menu_login(controller, mocker):
    # Simuler un utilisateur non connecté initialement
    controller.token = None
    controller.role_id = None
    controller.user_id = None
    controller.token_expiry = None

    # Simuler une séquence de choix : d'abord connexion, puis quitter
    controller.view.show_main_menu.side_effect = [constante.LOGIN, "0"]

    # Mock les informations de connexion
    mock_email = "test@example.com"
    mock_password = "password123"
    controller.view.get_login_credentials.return_value = (mock_email, mock_password)

    # Mock la fonction d'authentification
    mock_token = "fake_token"
    mock_role_id = 2
    mocker.patch(
        "crm.controllers.main_controller.authenticate",
        return_value=(mock_token, mock_role_id),
    )

    # Mock le décodage JWT
    mock_user_id = "fake_user_id"
    mock_exp = datetime.now() + timedelta(hours=1)
    mocker.patch(
        "jwt.decode", return_value={"user_id": mock_user_id, "exp": mock_exp.timestamp()}
    )

    # Mock handle_role_specific_actions pour éviter les effets secondaires
    mock_handle_role = mocker.patch.object(controller, "handle_role_specific_actions")

    # Exécuter main_menu
    controller.main_menu()

    # Vérifications
    assert controller.view.show_main_menu.call_count == 2
    controller.view.show_main_menu.assert_any_call(
        False
    )  # Premier appel avec utilisateur non connecté
    controller.view.show_main_menu.assert_any_call(
        True
    )  # Deuxième appel après connexion

    controller.view.get_login_credentials.assert_called_once()
    controller.view.show_login_success.assert_called_once()
    mock_handle_role.assert_called_once()

    # Vérifier que l'utilisateur est bien connecté
    assert controller.token == mock_token
    assert controller.role_id == mock_role_id
    assert controller.user_id == mock_user_id
    assert isinstance(controller.token_expiry, datetime)

    controller.view.show_exit_message.assert_called_once()


def test_handle_authentication_with_no_token(controller, mocker):
    mocker.patch.object(controller, "login")
    controller.token = None

    controller.handle_authentication()

    controller.login.assert_called_once()


def test_login_success(controller, mocker, mock_jwt_decode):
    mock_authenticate = mocker.patch("crm.controllers.main_controller.authenticate")
    mock_authenticate.return_value = ("fake_token", 1)

    mock_jwt_decode.return_value = {
        "user_id": 123,
        "exp": (datetime.now() + timedelta(hours=1)).timestamp(),
    }

    controller.view.get_login_credentials.return_value = ("test@example.com", "password")

    mocker.patch.object(controller, "handle_role_specific_actions")
    controller.login()

    assert controller.token == "fake_token"
    assert controller.role_id == 1
    assert controller.user_id == 123
    controller.view.show_login_success.assert_called_once()
    controller.handle_role_specific_actions.assert_called_once()


def test_login_failure(controller, mocker):
    mock_authenticate = mocker.patch("crm.controllers.main_controller.authenticate")
    mock_authenticate.return_value = (None, None)

    controller.view.get_login_credentials.return_value = (
        "test@example.com",
        "wrong_password",
    )

    controller.login()

    assert controller.token is None
    assert controller.role_id is None
    assert controller.user_id is None
    controller.view.show_login_failure.assert_called_once()


def test_handle_disconnection(controller):
    controller.token = "fake_token"
    controller.role_id = 1
    controller.user_id = 123

    controller.handle_disconnection()

    assert controller.token is None
    assert controller.role_id is None
    assert controller.user_id is None
    controller.view.show_disconnection_success.assert_called_once()


def test_session_expiring(controller, mocker):
    controller.token = "fake_token"
    controller.token_expiry = datetime.now() + timedelta(
        minutes=4
    )  # Token about to expire

    mocker.patch.object(controller, "handle_disconnection")
    controller.view.show_main_menu.side_effect = [
        "1",
        "0",
    ]  # First try to login, then exit

    controller.main_menu()

    controller.view.show_session_expiring_message.assert_called()
    controller.handle_disconnection.assert_called()


# def test_token_expiration(controller, mocker):
#     # Simuler un utilisateur connecté avec un token expiré
#     expired_time = datetime.now() - timedelta(minutes=5)
#     controller.token = "expired_token"
#     controller.role_id = 1
#     controller.user_id = "fake_user_id"
#     controller.token_expiry = expired_time

#     # Mock jwt.decode pour simuler un token expiré
#     mock_jwt_decode = mocker.patch("jwt.decode")
#     mock_jwt_decode.side_effect = jwt.ExpiredSignatureError

#     # Simuler une séquence de choix : d'abord une action quelconque, puis quitter
#     controller.view.show_main_menu.side_effect = ["1", "0"]

#     # Mock handle_role_specific_actions pour éviter les effets secondaires
#     mock_handle_role = mocker.patch.object(controller, "handle_role_specific_actions")

#     # Mock handle_disconnection pour vérifier qu'il est appelé
#     mock_handle_disconnection = mocker.patch.object(controller, "handle_disconnection")

#     # Exécuter main_menu
#     controller.main_menu()

#     # Vérifications
#     assert controller.view.show_main_menu.call_count == 2
#     controller.view.show_main_menu.assert_any_call(
#         True
#     )  # Premier appel, l'utilisateur pense être connecté
#     controller.view.show_main_menu.assert_any_call(
#         False
#     )  # Deuxième appel, après détection de l'expiration

#     mock_jwt_decode.assert_called_once()
#     controller.view.show_session_expired.assert_called_once()
#     mock_handle_disconnection.assert_called_once()

#     # Vérifier que l'utilisateur a été déconnecté
#     assert controller.token is None
#     assert controller.role_id is None
#     assert controller.user_id is None
#     assert controller.token_expiry is None

#     controller.view.show_exit_message.assert_called_once()
