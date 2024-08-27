import pytest
from unittest.mock import Mock, patch
from crm.models import Event
from crm.controllers.event_controller import (
    view_event,
    view_user_own_event,
    create_event,
    update_event,
    delete_event,
    view_no_support_event,
    update_no_support_event,
)
from Constantes.permissions import Role

# Mock pour PERMISSIONS
MOCK_PERMISSIONS = {
    "create_event": [Role("1"), Role("2")],
    "update_event": [Role("1"), Role("2")],
    "delete_event": [Role("1")],
}


@pytest.fixture(autouse=True)
def mock_permissions():
    with patch("crm.controllers.permissions.PERMISSIONS", MOCK_PERMISSIONS):
        yield


@pytest.fixture
def mock_session():
    with patch("crm.controllers.event_controller.Session") as mock:
        yield mock()


def test_view_event(mock_session):
    mock_events = [Mock(spec=Event), Mock(spec=Event)]
    mock_session.query.return_value.all.return_value = mock_events

    with patch("builtins.print") as mock_print:
        view_event()

    assert mock_print.call_count == len(mock_events)


def test_view_user_own_event(mock_session):
    user_id = 1
    mock_events = [Mock(spec=Event), Mock(spec=Event)]
    mock_session.query.return_value.filter_by.return_value.all.return_value = mock_events

    with patch("builtins.print") as mock_print:
        view_user_own_event(user_id)

    mock_session.query.return_value.filter_by.assert_called_once_with(support_id=user_id)
    assert mock_print.call_count == len(mock_events)


@patch("crm.controllers.permissions.Role")
def test_create_event(mock_role, mock_session):
    mock_role.return_value = Role("1")

    result = create_event(
        client_id=1,
        contract_id=1,
        start_date="2023-01-01",
        end_date="2023-01-02",
        location="Test Location",
        attendees="Test Attendees",
        current_user_role_id="1",
    )

    assert result is True
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()


@patch("crm.controllers.permissions.Role")
def test_update_event(mock_role, mock_session):
    mock_role.return_value = Role("1")
    mock_event = Mock(spec=Event)
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_event
    )

    result = update_event(
        user_id=1,
        event_id=1,
        current_user_role_id="1",
        start_date="2023-01-01",
        end_date="2023-01-02",
        location="New Location",
        attendees="New Attendees",
        notes="New Notes",
    )

    assert result is True
    assert mock_event.start_date == "2023-01-01"
    assert mock_event.end_date == "2023-01-02"
    assert mock_event.location == "New Location"
    assert mock_event.attendees == "New Attendees"
    assert mock_event.notes == "New Notes"
    mock_session.commit.assert_called_once()


@patch("crm.controllers.permissions.Role")
def test_delete_event(mock_role, mock_session):
    mock_role.return_value = Role("1")
    mock_event = Mock(spec=Event)
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_event
    )

    result = delete_event(event_id=1, current_user_role_id="1")

    assert result is True
    mock_session.delete.assert_called_once_with(mock_event)
    mock_session.commit.assert_called_once()


def test_view_no_support_event(mock_session):
    mock_events = [Mock(spec=Event), Mock(spec=Event)]
    mock_session.query.return_value.filter_by.return_value.all.return_value = mock_events

    with patch("builtins.print") as mock_print:
        view_no_support_event()

    mock_session.query.return_value.filter_by.assert_called_once_with(support_id=None)
    assert mock_print.call_count == len(mock_events)


def test_update_no_support_event(mock_session):
    mock_event = Mock(spec=Event)
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_event
    )

    result = update_no_support_event(user_id=1, event_id=1, support_id=2)

    assert result is True
    assert mock_event.support_id == 2
    mock_session.commit.assert_called_once()
