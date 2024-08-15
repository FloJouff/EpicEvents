import pytest
from pytest_mock import mocker
from crm.controllers.auth_controller import authenticate
from crm.controllers.permissions import requires_permission
from crm.models.user import User
from argon2 import PasswordHasher


# Mock pour la session de base de données
@pytest.fixture
def mock_session(mocker):
    return mocker.Mock()


# Mock pour l'utilisateur
@pytest.fixture
def mock_user():
    user = User(
        name="test",
        firstname="test",
        email="test@example.com",
        password=PasswordHasher().hash("password123"),
        role_id=2,
    )
    return user


def test_authenticate_success(mocker, mock_session, mock_user):
    mocker.patch(
        "crm.controllers.auth_controller.Session", return_value=mock_session
    )
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_user
    )

    token, role_id = authenticate("test@example.com", "password123")

    assert token is not None
    assert role_id == 2


def test_authenticate_failure(mocker, mock_session):
    mocker.patch(
        "crm.controllers.auth_controller.Session", return_value=mock_session
    )
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    token, role_id = authenticate("wrong@example.com", "wrongpassword")

    assert token is None
    assert role_id is None


def test_requires_permission_allowed(mocker):
    @requires_permission("create_user")
    def dummy_function(current_user_role_id):
        return "Function executed"

    mocker.patch(
        "crm.controllers.permissions.PERMISSIONS", {"create_user": ["2", "4"]}
    )

    result = dummy_function(current_user_role_id=2)
    assert result == "Function executed"


def test_requires_permission_denied(mocker):
    @requires_permission("create_user")
    def dummy_function(current_user_role_id):
        return "Function executed"

    mocker.patch(
        "crm.controllers.permissions.PERMISSIONS", {"create_user": ["2", "4"]}
    )

    result = dummy_function(current_user_role_id=1)
    assert result is None


def test_requires_permission_no_role_id():
    @requires_permission("create_user")
    def dummy_function():
        return "Function executed"

    result = dummy_function()
    assert result is None
