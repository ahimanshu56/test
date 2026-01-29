"""
Initial minimal tests for UserManager (intentionally incomplete for baseline).
"""

import pytest
from src.user_manager import UserManager


class TestUserManager:
    """Basic tests for UserManager."""
    
    def test_create_user_success(self):
        """Test creating a user with valid data."""
        manager = UserManager()
        user = manager.create_user('testuser', 'test@example.com', 'password123')
        
        assert user['username'] == 'testuser'
        assert user['email'] == 'test@example.com'
        assert user['active'] is True
    
    def test_authenticate_success(self):
        """Test successful authentication."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        token = manager.authenticate('testuser', 'password123')
        assert token is not None
