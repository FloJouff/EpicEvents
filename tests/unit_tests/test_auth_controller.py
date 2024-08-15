import pytest
import jwt
import datetime
from crm.controllers.auth_controller import refresh_token

JWT_SECRET = "testsecret"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # 1 hour


@pytest.fixture
def mock_jwt_secret(monkeypatch):
    monkeypatch.setattr(
        "crm.controllers.auth_controller.JWT_SECRET", JWT_SECRET
    )
    monkeypatch.setattr(
        "crm.controllers.auth_controller.JWT_ALGORITHM", JWT_ALGORITHM
    )


def generate_token(exp_delta):
    """Helper function to generate a JWT token with custom expiration delta"""
    payload = {
        "user_id": 1,
        "role": "admin",
        "exp": datetime.datetime.now() + datetime.timedelta(seconds=exp_delta),
    }
    return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)


def test_refresh_token_valid(mock_jwt_secret):
    # Arrange
    token = generate_token(3600)  # Token valid for 1 hour

    # Act
    new_token = refresh_token(token)

    # Assert
    assert new_token is not None
    decoded_payload = jwt.decode(
        new_token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
    )
    assert decoded_payload["user_id"] == 1
    assert decoded_payload["role"] == "admin"
    assert datetime.datetime.now() < datetime.datetime.fromtimestamp(
        decoded_payload["exp"]
    )


# def test_refresh_token_expired(mock_jwt_secret):
#     # Arrange
#     token = generate_token(-3600)  # Token expired 1 hour ago

#     # Act
#     new_token = refresh_token(token)

#     # Assert
#     assert new_token is None


def test_refresh_token_invalid_token(mock_jwt_secret):
    # Arrange
    token = "this.is.an.invalid.token"

    # Act
    new_token = refresh_token(token)

    # Assert
    assert new_token is None
