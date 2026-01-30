"""
Basic tests for user_manager module (intentionally incomplete for initial coverage).
"""
import pytest
from src.user_manager import UserManager


def test_create_user_success():
    """Test creating a user with valid data."""
    manager = UserManager()
    user = manager.create_user("john_doe", "john@example.com", "Password123")
    
    assert user["username"] == "john_doe"
    assert user["email"] == "john@example.com"
    assert user["active"] is True


def test_authenticate_success():
    """Test successful authentication."""
    manager = UserManager()
    manager.create_user("john_doe", "john@example.com", "Password123")
    
    token = manager.authenticate("john_doe", "Password123")
    assert token is not None
    assert token.startswith("session_")


def test_get_user():
    """Test getting user information."""
    manager = UserManager()
    manager.create_user("john_doe", "john@example.com", "Password123")
    
    user = manager.get_user("john_doe")
    assert user is not None
    assert user["username"] == "john_doe"
    assert "password" not in user
