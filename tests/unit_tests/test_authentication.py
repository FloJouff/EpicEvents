import pytest
from crm.models.user import User
from argon2 import PasswordHasher
from crm.controllers.permissions import requires_permission

ph = PasswordHasher()


@pytest.fixture
def user_test():
    password = "securepassword"
    hashed_password = ph.hash(password)
    user = User(
        name="Test",
        firstname="User",
        email="test@example.com",
        password=hashed_password,
        role_id=None,
    )
    return (
        user,
        password,
    )


def test_password_hashing(user_test):
    user, password = user_test

    assert user.check_password(password) is True

    assert user.check_password("wrongpassword") is False


def test_password_hashing_invalid():
    user = User(
        name="Test",
        firstname="User",
        email="test@example.com",
        password="securepassword",
        role_id=None,
    )

    assert not user.check_password("incorrectpassword")


@pytest.fixture
def mock_session(mocker):
    return mocker.Mock()


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
    mocker.patch("crm.database.Session", return_value=mock_session)
    mock_session.query.return_value.filter_by.return_value.first.return_value = mock_user

    mock_ph = mocker.Mock(spec=PasswordHasher)
    mock_ph.verify.return_value = True
    mocker.patch("crm.models.user.ph", mock_ph)

    mocker.patch("crm.models.user.jwt.encode", return_value="mocked_token")

    token, role_id = User.authenticate("test@example.com", "password123")

    assert token == "mocked_token"
    assert role_id == mock_user.role_id

    mock_ph.verify.assert_called_once_with(mock_user.password, "password123")


def test_authenticate_failure(mocker, mock_session):
    mocker.patch("crm.database.Session", return_value=mock_session)
    mock_session.query.return_value.filter_by.return_value.first.return_value = None

    token, role_id = User.authenticate("wrong@example.com", "wrongpassword")

    assert token is None
    assert role_id is None


def test_requires_permission_denied(mocker):
    @requires_permission("create_user")
    def dummy_function(current_user_role_id):
        return "Function executed"

    mocker.patch("crm.controllers.permissions.PERMISSIONS", {"create_user": ["2", "4"]})

    result = dummy_function(current_user_role_id=1)
    assert result is None


def test_requires_permission_no_role_id():
    @requires_permission("create_user")
    def dummy_function():
        return "Function executed"

    result = dummy_function()
    assert result is None
