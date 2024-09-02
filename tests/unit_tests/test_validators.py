import pytest

from validators import (
    validate_email,
    validate_date,
    validate_phone_number,
    validate_password,
    validate_name,
    validate_id,
)


def test_validate_email_valid():
    assert validate_email("test@example.com") is True


def test_validate_email_invalid(mocker):
    assert validate_email("invalid-email") is None


def test_validate_date_valid():
    assert validate_date("2023-09-02") is True


def test_validate_date_invalid(mocker):
    assert validate_date("02-09-2023") is False


def test_validate_phone_number_valid():
    assert validate_phone_number("0123456789") is True


def test_validate_phone_number_invalid(mocker):
    assert validate_phone_number("12345") is None


def test_validate_password_valid():
    assert validate_password("password123") is True


def test_validate_password_invalid():
    assert validate_password("short") is None


def test_validate_name_valid():
    assert validate_name("John Doe") is True


def test_validate_name_invalid(mocker):

    assert validate_name("J") is False


def test_validate_id_valid():
    assert validate_id("12345") is True


def test_validate_id_invalid(mocker):
    assert validate_id("abc") is False
