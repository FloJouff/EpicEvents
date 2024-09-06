import pytest
from unittest.mock import MagicMock, patch
from crm.controllers.client_controller import create_client, delete_client


@pytest.fixture
def mock_session(mocker):
    return mocker.patch("crm.controllers.client_controller.Session", autospec=True)


@pytest.fixture
def mock_permission(mocker):
    mocker.patch(
        "crm.controllers.client_controller.requires_permission",
        lambda x: lambda *args, **kwargs: x(*args, **kwargs),
    )


def test_create_client_success(mock_session, mock_permission):
    mock_session_instance = mock_session.return_value
    mock_client = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    result = create_client(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        phone="1234567890",
        company="Doe Inc.",
        contact_id=1,
        current_user_role_id=2,
    )

    assert result is True
    mock_session_instance.add.assert_called_once()
    mock_session_instance.commit.assert_called_once()


def test_create_client_already_exists(mock_session, mock_permission):
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        MagicMock()
    )

    result = create_client(
        name="John",
        firstname="Doe",
        email="john.doe@example.com",
        phone="1234567890",
        company="Doe Inc.",
        contact_id=1,
        current_user_role_id=2,
    )

    assert result is False
    mock_session_instance.add.assert_not_called()
    mock_session_instance.commit.assert_not_called()


def test_delete_client_success(mock_session, mock_permission):
    mock_session_instance = mock_session.return_value
    mock_client = MagicMock()
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        mock_client
    )

    result = delete_client(client_id=1, current_user_role_id=4)

    assert result is True
    mock_session_instance.delete.assert_called_once_with(mock_client)
    mock_session_instance.commit.assert_called_once()


def test_delete_client_not_found(mock_session, mock_permission):
    mock_session_instance = mock_session.return_value
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )

    result = delete_client(client_id=1, current_user_role_id=4)

    assert result is False
    mock_session_instance.delete.assert_not_called()
    mock_session_instance.commit.assert_not_called()
