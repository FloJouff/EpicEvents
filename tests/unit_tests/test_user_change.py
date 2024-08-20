# import pytest
# from crm.controllers.user_controller import (
#     create_user,
#     update_user,
#     delete_user,
# )
# from crm.models import User
# from crm.database import Session


# @pytest.fixture
# def mock_session(mocker):
#     return mocker.patch("crm.database.Session", autospec=True)


# @pytest.fixture
# def mock_user(mocker):
#     return mocker.patch("crm.models.User", autospec=True)


# def test_create_user(mock_session, mock_user):
#     # Arrange
#     mock_session_instance = mock_session.return_value
#     mock_user_instance = mock_user.return_value

#     name = "John"
#     firstname = "Doe"
#     email = "john.doe@example.com"
#     password = "password123"
#     role_id = 4  # Admin role
#     current_user_role_id = 4  # Simulate that current user is admin

#     # Act
#     success = create_user(
#         name, firstname, email, password, role_id, current_user_role_id
#     )

#     # Assert
#     assert success is True
#     mock_session_instance.add.assert_called_once_with(mock_user_instance)
#     mock_session_instance.commit.assert_called_once()
#     mock_user.assert_called_once_with(
#         name=name,
#         firstname=firstname,
#         email=email,
#         password=mock_user_instance.password,
#         role_id=role_id,
#     )


# def test_update_user(mock_session):
#     # Arrange
#     mock_session_instance = mock_session.return_value
#     mock_user_instance = (
#         mock_session_instance.query.return_value.filter_by.return_value.first.return_value
#     )

#     user_id = 1
#     updated_name = "Jane"
#     updated_firstname = "Smith"
#     updated_email = "jane.smith@example.com"

#     # Act
#     success = update_user(
#         user_id, updated_name, updated_firstname, updated_email
#     )

#     # Assert
#     assert success is True
#     assert mock_user_instance.name == updated_name
#     assert mock_user_instance.firstname == updated_firstname
#     assert mock_user_instance.email == updated_email
#     mock_session_instance.commit.assert_called_once()


# def test_delete_user(mock_session):
#     # Arrange
#     mock_session_instance = mock_session.return_value
#     mock_user_instance = (
#         mock_session_instance.query.return_value.filter_by.return_value.first.return_value
#     )

#     user_id = 1

#     # Act
#     success = delete_user(user_id)

#     # Assert
#     assert success is True
#     mock_session_instance.query.assert_called_once_with(User)
#     mock_session_instance.query.return_value.filter_by.assert_called_once_with(
#         user_id=user_id
#     )
#     mock_session_instance.delete.assert_called_once_with(mock_user_instance)
#     mock_session_instance.commit.assert_called_once()
#     mock_session_instance.close.assert_called_once()
