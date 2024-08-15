import pytest
from crm.models.user import User
from crm.models.role import Role
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


@pytest.fixture
def role_manager():
    return Role(role_id=1, role="gestion")


@pytest.fixture
def role_sales():
    return Role(role_id=2, role="commercial")


@pytest.fixture
def role_support():
    return Role(role_id=3, role="support")


@pytest.fixture
def user_manager(role_manager):
    hashed_password = ph.hash("manager_pass")
    return User(
        name="Doe",
        firstname="John",
        email="john.doe@example.com",
        password=hashed_password,
        role=role_manager,
    )


@pytest.fixture
def user_sales(role_sales):
    hashed_password = ph.hash("sales_pass")
    return User(
        name="Smith",
        firstname="Jane",
        email="jane.smith@example.com",
        password=hashed_password,
        role_id=role_sales,
    )


@pytest.fixture
def user_support(role_support):
    hashed_password = ph.hash("support_pass")
    return User(
        name="Brown",
        firstname="Bob",
        email="bob.brown@example.com",
        password=hashed_password,
        role_id=role_support,
    )


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
    )  # On retourne l'utilisateur et le mot de passe en clair pour les tests


# Tests pour le hachage et la vérification des mots de passe
def test_password_hashing(user_test):
    user, password = user_test

    # Test de vérification avec le bon mot de passe
    assert user.check_password(password) is True

    # Test de vérification avec un mauvais mot de passe
    assert user.check_password("wrongpassword") is False


def test_password_hashing_invalid():
    user = User(
        name="Test",
        firstname="User",
        email="test@example.com",
        password="securepassword",
        role_id=None,
    )

    # Simulation d'un mot de passe incorrect
    assert not user.check_password("incorrectpassword")
