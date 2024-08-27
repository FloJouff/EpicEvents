import pytest
from unittest.mock import Mock, patch
from Constantes.permissions import Role


from crm.controllers.contracts_controller import (
    view_contract,
    view_user_own_contracts,
    create_contract,
    update_contract,
    view_unsigned_contract,
    view_unpaid_contract,
)


MOCK_PERMISSIONS = {
    "update_contract": [Role("1"), Role("4"), Role("3")],
    "delete_contract": [Role("1"), Role("4")],
}


@pytest.fixture(autouse=True)
def mock_permissions():
    with patch("Constantes.permissions.PERMISSIONS", MOCK_PERMISSIONS):
        yield


@pytest.fixture
def mock_session():
    with patch("crm.controllers.contracts_controller.Session") as mock:
        yield mock.return_value


def test_view_contract(mock_session, capsys):
    mock_contracts = [Mock(id=1), Mock(id=2)]
    mock_session.query.return_value.all.return_value = mock_contracts

    view_contract()

    captured = capsys.readouterr()
    assert "Liste des contrats : " in captured.out
    assert len(captured.out.strip().split("\n")) == 2


def test_view_user_own_contracts(mock_session, capsys):
    user_id = 1
    mock_contracts = [Mock(id=1), Mock(id=2)]
    mock_session.query.return_value.filter_by.return_value.all.return_value = (
        mock_contracts
    )

    view_user_own_contracts(user_id)

    captured = capsys.readouterr()
    assert "Liste des évènements : " in captured.out
    assert len(captured.out.strip().split("\n")) == 2


@patch("crm.controllers.contracts_controller.uuid.uuid4")
def test_create_contract(mock_uuid, mock_session):
    mock_uuid.return_value = "mocked-uuid"

    result = create_contract(
        client_id=1, commercial_id=2, total_amount=1000, current_user_role_id=1
    )
    print("test create:", result)

    assert result is True
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()


@patch("Constantes.permissions.Role")
def test_update_contract(mock_role, mock_session):
    contract_id = "test-id"
    mock_contract = Mock()
    mock_session.query.return_value.filter_by.return_value.first.return_value = (
        mock_contract
    )

    mock_role.return_value = Role("1")

    result = update_contract(
        user_id=1,
        contract_id=contract_id,
        client_id=2,
        commercial_id=3,
        remain_amount=500,
        is_signed=True,
        current_user_role_id=1,
    )

    assert result is True
    assert mock_contract.client_id == 2
    assert mock_contract.commercial_id == 3
    assert mock_contract.remain_amount == 500
    assert mock_contract.is_signed is True
    mock_session.commit.assert_called_once()


# @patch("Constantes.permissions.Role")
# def test_delete_contract(mock_role, mock_session):
#     contract_id = "test-id"
#     mock_contract = Mock()
#     mock_session.query.return_value.filter_by.return_value.first.return_value = (
#         mock_contract
#     )

#     mock_role.return_value = Role("4")

#     result = delete_contract(
#         user_id=1, contract_id=contract_id, current_user_role_id="1"
#     )

#     assert result is True
#     mock_session.delete.assert_called_once_with(mock_contract)
#     mock_session.commit.assert_called_once()


@patch("Constantes.permissions.Role")
def test_update_contract_permission_denied(mock_role, mock_session):
    mock_role.return_value = Role("3")

    result = update_contract(user_id=1, contract_id="test-id", client_id=2)

    assert result is None


# @patch("Constantes.permissions.Role")
# def test_delete_contract_permission_denied(mock_role, mock_session):
#     mock_role.return_value = Role("3")

#     result = delete_contract(user_id=1, contract_id="test-id")

#     assert result is None


def test_view_unsigned_contract(mock_session, capsys):
    mock_contracts = [Mock(id=1), Mock(id=2)]
    mock_session.query.return_value.filter_by.return_value.all.return_value = (
        mock_contracts
    )

    view_unsigned_contract()

    captured = capsys.readouterr()
    assert "List of unsigned contracts : " in captured.out
    assert len(captured.out.strip().split("\n")) == 2


def test_view_unpaid_contract(mock_session, capsys):
    mock_contracts = [Mock(id=1), Mock(id=2)]
    mock_session.query.return_value.filter.return_value.all.return_value = mock_contracts

    view_unpaid_contract()

    captured = capsys.readouterr()
    assert "List of unsolded contracts : " in captured.out
    assert len(captured.out.strip().split("\n")) == 2
