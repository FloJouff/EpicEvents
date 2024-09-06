import pytest
from unittest.mock import MagicMock
from crm.controllers import user_controller
from crm.models import User
from crm.database import Session


@pytest.fixture
def mock_session(mocker):
    mock_session = mocker.patch("crm.controllers.user_controller.Session", autospec=True)
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )
    return mock_session


@pytest.fixture
def mock_password_hasher(mocker):
    return mocker.patch("crm.controllers.user_controller.ph")


@pytest.fixture
def mock_user_model(mocker):
    return mocker.patch("crm.models.User")


def test_create_user_success(mock_session, mock_password_hasher, mock_user_model):
    """Test successfully creating new user"""
    mock_user_instance = mock_user_model.return_value
    mock_session_instance = mock_session.return_value

    result = user_controller.create_user(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        password="password123",
        role_id=1,
        current_user_role_id=1,
    )

    assert result is True
    mock_session_instance.commit.assert_called_once()


def test_create_user_existing_user(mock_session, mock_user_model):
    """Test to create an already existing user"""
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user_model
    )

    result = user_controller.create_user(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        password="password123",
        role_id=1,
        current_user_role_id=1,
    )

    assert result is False


def test_view_users(mock_session, mock_user_model, capsys):
    """Test to display users list"""

    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.all.return_value = mock_user_model

    user_controller.view_users()

    captured = capsys.readouterr()
    assert "List of Users" in captured.out


def test_update_user_success(mock_session, mock_password_hasher, mock_user_model):
    """Test when a user is updated successfully"""

    mock_session_instance = mock_session.return_value
    mock_user = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user
    )
    mock_password_hasher.hash.return_value = "new_hashed_password"

    result = user_controller.update_user(
        1,
        name="Doe",
        email="john.doe@example.com",
        password="NewPassword123",
        current_user_role_id=1,
    )

    assert result is True
    assert mock_user.name == "Doe"
    assert mock_user.email == "john.doe@example.com"
    assert mock_user.password == "new_hashed_password"
    mock_session_instance.commit.assert_called_once()


def test_update_user_not_found(mock_session, mock_user_model):
    """Test when trying to update unknown user"""

    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    result = user_controller.update_user(
        1,
        name="Doe",
        current_user_role_id=1,
    )

    assert result is False
    mock_session_instance.commit.assert_not_called()


def test_change_password_success(mock_session, mock_password_hasher):
    """Test when a user change password"""
    mock_session_instance = mock_session.return_value
    mock_user = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user
    )
    mock_user.check_password.return_value = True
    mock_password_hasher.hash.return_value = "new_hashed_password"

    result = user_controller.change_password(1, "OldPassword123", "NewPassword123")

    assert result is True
    assert mock_user.password == "new_hashed_password"
    mock_session_instance.commit.assert_called_once()


def test_change_password_incorrect_old_password(mock_session):
    """Test when a user tries to change password with incorrect old password"""
    mock_session_instance = mock_session.return_value
    mock_user = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user
    )
    mock_user.check_password.return_value = False

    result = user_controller.change_password(1, "OldPassword123", "NewPassword123")

    assert result is False
    mock_session_instance.commit.assert_not_called()


def test_delete_user_success(mock_session):
    """Test when a user is deleted successfully"""

    mock_session_instance = mock_session.return_value
    mock_user = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user
    )
    result = user_controller.delete_user(
        1,
        current_user_role_id=1,
    )

    assert result is True
    mock_session_instance.delete.assert_called_once_with(mock_user)
    mock_session_instance.commit.assert_called_once()


def test_delete_user_not_found(mock_session):
    """Test trying to delet an unknown user"""
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    result = user_controller.delete_user(
        1,
        current_user_role_id=1,
    )

    assert result is False
    mock_session_instance.commit.assert_not_called()
