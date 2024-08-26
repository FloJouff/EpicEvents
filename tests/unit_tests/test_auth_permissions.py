# import pytest
# from pytest_mock import mocker
# from crm.controllers.auth_controller import authenticate
# from crm.controllers.permissions import requires_permission
# from crm.models.user import User
# from argon2 import PasswordHasher


# # Mock for database
# @pytest.fixture
# def mock_session(mocker):
#     return mocker.Mock()


# # Mock for user
# @pytest.fixture
# def mock_user():
#     user = User(
#         name="test",
#         firstname="test",
#         email="test@example.com",
#         password=PasswordHasher().hash("password123"),
#         role_id=2,
#     )
#     return user


# def test_authenticate_success(mocker, mock_session, mock_user):
#     mocker.patch(
#         "crm.controllers.auth_controller.Session", return_value=mock_session
#     )
#     mock_session.query.return_value.filter_by.return_value.first.return_value = (
#         mock_user
#     )

#     token, role_id = authenticate("test@example.com", "password123")

#     assert token is not None
#     assert role_id == 2


# def test_authenticate_failure(mocker, mock_session):
#     mocker.patch(
#         "crm.controllers.auth_controller.Session", return_value=mock_session
#     )
#     mock_session.query.return_value.filter_by.return_value.first.return_value = (
#         None
#     )

#     token, role_id = authenticate("wrong@example.com", "wrongpassword")

#     assert token is None
#     assert role_id is None


# def test_requires_permission_allowed(mocker):
#     @requires_permission("create_user")
#     def dummy_function(current_user_role_id):
#         return "Function executed"

#     mocker.patch(
#         "crm.controllers.permissions.PERMISSIONS", {"create_user": ["2", "4"]}
#     )

#     result = dummy_function(current_user_role_id=2)
#     assert result == "Function executed"


# def test_requires_permission_denied(mocker):
#     @requires_permission("create_user")
#     def dummy_function(current_user_role_id):
#         return "Function executed"

#     mocker.patch(
#         "crm.controllers.permissions.PERMISSIONS", {"create_user": ["2", "4"]}
#     )

#     result = dummy_function(current_user_role_id=1)
#     assert result is None


# def test_requires_permission_no_role_id():
#     @requires_permission("create_user")
#     def dummy_function():
#         return "Function executed"

#     result = dummy_function()
#     assert result is None


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


# def test_main_menu_logout(controller, mocker):
#     mocker.patch.object(controller, "handle_disconnection")
#     controller.token = "fake_token"
#     controller.token_expiry = datetime.now() + timedelta(
#         hours=1
#     )  # Set token expiry to 1 hour from now
#     controller.view.show_main_menu.return_value = (
#         "2"  # Assuming 2 is DISCONNECT constant
#     )

#     controller.main_menu()

#     controller.handle_disconnection.assert_called_once()


# def test_main_menu_login(controller, mocker):
#     mocker.patch.object(controller, "handle_authentication")
#     controller.token = None
#     controller.view.show_main_menu.return_value = "1"  # Assuming 1 is LOGIN constant

#     controller.main_menu()

#     controller.handle_authentication.assert_called_once()


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
