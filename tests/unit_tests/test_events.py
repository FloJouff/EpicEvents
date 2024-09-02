import pytest
from unittest.mock import Mock, patch
from rich.table import Table
from crm.models import Event
from crm.views.event_view import EventView
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
        yield mock.return_value


@pytest.fixture
def event_view():
    return EventView()


def test_view_event(event_view, mocker):
    mock_event = Event(
        contract_id="1",
        client_id="2",
        start_date="2023-01-01",
        end_date="2023-01-02",
        location="User Location",
        attendees="75",
    )
    mock_list = [mock_event]
    mock_table = Table()
    mock_table.add_column("Contract ID")
    mock_table.add_column("Client ID")
    mock_table.add_column("Start Date")
    mock_table.add_column("End Date")
    mock_table.add_column("Location")
    mock_table.add_column("Attendees")
    mock_table.add_row(
        mock_event.contract_id,
        mock_event.client_id,
        str(mock_event.start_date),
        str(mock_event.end_date),
        mock_event.location,
        mock_event.attendees,
    )

    mocker.patch.object(EventView, "display_event_list", return_value=mock_table)

    result = EventView.display_event_list(mock_list)
    assert isinstance(result, Table)


def test_view_user_own_event(event_view, mocker):
    mock_event = Event(
        contract_id="1",
        client_id="2",
        start_date="2023-01-01",
        end_date="2023-01-02",
        location="User Location",
        attendees="75",
    )
    mock_list = [mock_event]
    mock_table = Table()
    mock_table.add_column("Contract ID")
    mock_table.add_column("Client ID")
    mock_table.add_column("Start Date")
    mock_table.add_column("End Date")
    mock_table.add_column("Location")
    mock_table.add_column("Attendees")
    mock_table.add_row(
        mock_event.contract_id,
        mock_event.client_id,
        str(mock_event.start_date),
        str(mock_event.end_date),
        mock_event.location,
        mock_event.attendees,
    )

    mocker.patch.object(EventView, "display_event_list", return_value=mock_table)

    result = EventView.display_event_list(mock_list)
    assert isinstance(result, Table)


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


def test_view_no_support_event(event_view, mocker):
    mock_event = Event(
        contract_id="1",
        client_id="2",
        start_date="2023-01-01",
        end_date="2023-01-02",
        location="User Location",
        attendees="75",
        support_id="",
    )
    mock_list = [mock_event]
    mock_table = Table()
    mock_table.add_column("Contract ID")
    mock_table.add_column("Client ID")
    mock_table.add_column("Start Date")
    mock_table.add_column("End Date")
    mock_table.add_column("Location")
    mock_table.add_column("Attendees")
    mock_table.add_column("Support ID")
    mock_table.add_row(
        mock_event.contract_id,
        mock_event.client_id,
        str(mock_event.start_date),
        str(mock_event.end_date),
        mock_event.location,
        mock_event.attendees,
        mock_event.support_id,
    )

    mocker.patch.object(EventView, "show_no_support_list", return_value=mock_table)

    result = EventView.show_no_support_list(mock_list)
    assert isinstance(result, Table)


def test_update_no_support_event(mock_session):
    mock_event = Mock(spec=Event)
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_event
    )

    result = update_no_support_event(user_id=1, event_id=1, support_id=2)

    assert result is True
    assert mock_event.support_id == 2
    mock_session.commit.assert_called_once()
