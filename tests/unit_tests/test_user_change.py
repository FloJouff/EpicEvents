import pytest
from unittest.mock import MagicMock
from crm.controllers import user_controller
from crm.models import User
from crm.database import Session


@pytest.fixture
def mock_session(mocker):
    # Mock the Session object
    mock_session = mocker.patch("crm.controllers.user_controller.Session", autospec=True)
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )
    return mock_session


@pytest.fixture
def mock_password_hasher(mocker):
    # Mock the PasswordHasher object
    return mocker.patch("crm.controllers.user_controller.ph")


@pytest.fixture
def mock_user_model(mocker):
    # Mock the User model
    return mocker.patch("crm.models.User")


def test_create_user_success(mock_session, mock_password_hasher, mock_user_model):
    # Arrange
    mock_user_instance = mock_user_model.return_value
    mock_session_instance = mock_session.return_value

    # Act
    result = user_controller.create_user(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        password="password123",
        role_id=1,
        current_user_role_id=1,
    )

    # Assert
    assert result is True
    mock_session_instance.add.assert_called_once_with(mock_user_instance)
    mock_session_instance.commit.assert_called_once()


def test_create_user_existing_user(mock_session, mock_user_model):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_user_model
    )

    # Act
    result = user_controller.create_user(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        password="password123",
        role_id=1,
        current_user_role_id=1,
    )

    # Assert
    assert result is False


def test_view_users(mock_session, mock_user_model, capsys):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.all.return_value = [mock_user_model]

    # Act
    user_controller.view_users()

    # Assert
    captured = capsys.readouterr()
    assert "Users list" in captured.out


def test_update_user_success(mock_session, mock_password_hasher):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_user = (
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value
    )

    # Act
    result = user_controller.update_user(
        user_id=1, name="Jane", email="jane.doe@example.com"
    )

    # Assert
    assert result is True
    mock_session_instance.commit.assert_called_once()


def test_update_user_not_found(mock_session):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    # Act
    result = user_controller.update_user(user_id=1, name="Jane")

    # Assert
    assert result is False


def test_change_password_success(mock_session, mock_password_hasher, mocker):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_user = (
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value
    )
    mock_user.check_password.return_value = True

    # Act
    result = user_controller.change_password(
        user_id=1, old_password="oldpass", new_password="newpass"
    )

    # Assert
    assert result is True
    mock_session_instance.commit.assert_called_once()


def test_delete_user_success(mock_session):
    # Arrange
    mock_session_instance = mock_session.return_value
    mock_user = (
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value
    )

    # Act
    result = user_controller.delete_user(user_id=1)

    # Assert
    assert result is True
    mock_session_instance.delete.assert_called_once_with(mock_user)
    mock_session_instance.commit.assert_called_once()
