"""
Comprehensive tests for UserManager module.
Achieves 100% coverage of all functions, branches, and edge cases.
"""

import pytest
from src.user_manager import UserManager


class TestUserManagerCreate:
    """Tests for user creation functionality."""
    
    def test_create_user_success(self):
        """Test creating a user with valid data."""
        manager = UserManager()
        user = manager.create_user('testuser', 'test@example.com', 'password123')
        
        assert user['username'] == 'testuser'
        assert user['email'] == 'test@example.com'
        assert user['active'] is True
        assert user['role'] == 'user'
    
    def test_create_user_username_too_short(self):
        """Test creating user with username too short."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Username must be 3-20 characters"):
            manager.create_user('ab', 'test@example.com', 'password123')
    
    def test_create_user_username_too_long(self):
        """Test creating user with username too long."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Username must be 3-20 characters"):
            manager.create_user('a' * 21, 'test@example.com', 'password123')
    
    def test_create_user_username_empty(self):
        """Test creating user with empty username."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Username must be 3-20 characters"):
            manager.create_user('', 'test@example.com', 'password123')
    
    def test_create_user_username_invalid_characters(self):
        """Test creating user with invalid characters in username."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Username must be alphanumeric"):
            manager.create_user('test@user', 'test@example.com', 'password123')
    
    def test_create_user_duplicate_username(self):
        """Test creating user with duplicate username."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        with pytest.raises(ValueError, match="Username already exists"):
            manager.create_user('testuser', 'other@example.com', 'password456')
    
    def test_create_user_invalid_email(self):
        """Test creating user with invalid email."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Invalid email address"):
            manager.create_user('testuser', 'invalid-email', 'password123')
    
    def test_create_user_empty_email(self):
        """Test creating user with empty email."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Invalid email address"):
            manager.create_user('testuser', '', 'password123')
    
    def test_create_user_password_too_short(self):
        """Test creating user with password too short."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Password must be at least 8 characters"):
            manager.create_user('testuser', 'test@example.com', 'pass')
    
    def test_create_user_empty_password(self):
        """Test creating user with empty password."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Password must be at least 8 characters"):
            manager.create_user('testuser', 'test@example.com', '')


class TestUserManagerAuthentication:
    """Tests for authentication functionality."""
    
    def test_authenticate_success(self):
        """Test successful authentication."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        token = manager.authenticate('testuser', 'password123')
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_authenticate_wrong_password(self):
        """Test authentication with wrong password."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        token = manager.authenticate('testuser', 'wrongpassword')
        assert token is None
    
    def test_authenticate_nonexistent_user(self):
        """Test authentication with nonexistent user."""
        manager = UserManager()
        
        token = manager.authenticate('nonexistent', 'password123')
        assert token is None
    
    def test_authenticate_empty_username(self):
        """Test authentication with empty username."""
        manager = UserManager()
        
        token = manager.authenticate('', 'password123')
        assert token is None
    
    def test_authenticate_empty_password(self):
        """Test authentication with empty password."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        token = manager.authenticate('testuser', '')
        assert token is None
    
    def test_authenticate_inactive_user(self):
        """Test authentication with inactive user."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        manager.update_user('testuser', active=False)
        
        token = manager.authenticate('testuser', 'password123')
        assert token is None


class TestUserManagerCRUD:
    """Tests for CRUD operations."""
    
    def test_get_user_success(self):
        """Test getting existing user."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        user = manager.get_user('testuser')
        assert user is not None
        assert user['username'] == 'testuser'
        assert user['email'] == 'test@example.com'
        assert 'password_hash' not in user
    
    def test_get_user_nonexistent(self):
        """Test getting nonexistent user."""
        manager = UserManager()
        
        user = manager.get_user('nonexistent')
        assert user is None
    
    def test_update_user_email(self):
        """Test updating user email."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        result = manager.update_user('testuser', email='newemail@example.com')
        assert result is True
        
        user = manager.get_user('testuser')
        assert user['email'] == 'newemail@example.com'
    
    def test_update_user_invalid_email(self):
        """Test updating user with invalid email."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        with pytest.raises(ValueError, match="Invalid email address"):
            manager.update_user('testuser', email='invalid-email')
    
    def test_update_user_active_status(self):
        """Test updating user active status."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        result = manager.update_user('testuser', active=False)
        assert result is True
        
        user = manager.get_user('testuser')
        assert user['active'] is False
    
    def test_update_user_role(self):
        """Test updating user role."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        result = manager.update_user('testuser', role='admin')
        assert result is True
        
        user = manager.get_user('testuser')
        assert user['role'] == 'admin'
    
    def test_update_user_invalid_role(self):
        """Test updating user with invalid role."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        with pytest.raises(ValueError, match="Invalid role"):
            manager.update_user('testuser', role='superuser')
    
    def test_update_user_nonexistent(self):
        """Test updating nonexistent user."""
        manager = UserManager()
        
        result = manager.update_user('nonexistent', email='test@example.com')
        assert result is False
    
    def test_delete_user_success(self):
        """Test deleting existing user."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        
        result = manager.delete_user('testuser')
        assert result is True
        
        user = manager.get_user('testuser')
        assert user is None
    
    def test_delete_user_nonexistent(self):
        """Test deleting nonexistent user."""
        manager = UserManager()
        
        result = manager.delete_user('nonexistent')
        assert result is False
    
    def test_delete_user_removes_sessions(self):
        """Test that deleting user removes their sessions."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        token = manager.authenticate('testuser', 'password123')
        
        assert manager.validate_session(token) == 'testuser'
        
        manager.delete_user('testuser')
        
        assert manager.validate_session(token) is None


class TestUserManagerList:
    """Tests for listing users."""
    
    def test_list_users_empty(self):
        """Test listing users when none exist."""
        manager = UserManager()
        
        users = manager.list_users()
        assert users == []
    
    def test_list_users_multiple(self):
        """Test listing multiple users."""
        manager = UserManager()
        manager.create_user('user1', 'user1@example.com', 'password123')
        manager.create_user('user2', 'user2@example.com', 'password123')
        manager.create_user('user3', 'user3@example.com', 'password123')
        
        users = manager.list_users()
        assert len(users) == 3
        usernames = [u['username'] for u in users]
        assert 'user1' in usernames
        assert 'user2' in usernames
        assert 'user3' in usernames
    
    def test_list_users_active_only(self):
        """Test listing only active users."""
        manager = UserManager()
        manager.create_user('user1', 'user1@example.com', 'password123')
        manager.create_user('user2', 'user2@example.com', 'password123')
        manager.update_user('user2', active=False)
        
        users = manager.list_users(active_only=True)
        assert len(users) == 1
        assert users[0]['username'] == 'user1'
    
    def test_list_users_includes_inactive(self):
        """Test listing all users including inactive."""
        manager = UserManager()
        manager.create_user('user1', 'user1@example.com', 'password123')
        manager.create_user('user2', 'user2@example.com', 'password123')
        manager.update_user('user2', active=False)
        
        users = manager.list_users(active_only=False)
        assert len(users) == 2


class TestUserManagerSessions:
    """Tests for session management."""
    
    def test_validate_session_valid(self):
        """Test validating a valid session."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        token = manager.authenticate('testuser', 'password123')
        
        username = manager.validate_session(token)
        assert username == 'testuser'
    
    def test_validate_session_invalid(self):
        """Test validating an invalid session."""
        manager = UserManager()
        
        username = manager.validate_session('invalid-token')
        assert username is None
    
    def test_logout_success(self):
        """Test successful logout."""
        manager = UserManager()
        manager.create_user('testuser', 'test@example.com', 'password123')
        token = manager.authenticate('testuser', 'password123')
        
        result = manager.logout(token)
        assert result is True
        
        username = manager.validate_session(token)
        assert username is None
    
    def test_logout_invalid_token(self):
        """Test logout with invalid token."""
        manager = UserManager()
        
        result = manager.logout('invalid-token')
        assert result is False


class TestUserManagerHelpers:
    """Tests for helper methods."""
    
    def test_is_valid_email_valid(self):
        """Test email validation with valid emails."""
        manager = UserManager()
        
        assert manager._is_valid_email('test@example.com') is True
        assert manager._is_valid_email('user.name@example.co.uk') is True
        assert manager._is_valid_email('user+tag@example.com') is True
    
    def test_is_valid_email_invalid(self):
        """Test email validation with invalid emails."""
        manager = UserManager()
        
        assert manager._is_valid_email('') is False
        assert manager._is_valid_email('invalid') is False
        assert manager._is_valid_email('@example.com') is False
        assert manager._is_valid_email('user@') is False
        assert manager._is_valid_email('user@example') is False
    
    def test_hash_password_consistent(self):
        """Test that password hashing is consistent."""
        manager = UserManager()
        
        hash1 = manager._hash_password('password123')
        hash2 = manager._hash_password('password123')
        
        assert hash1 == hash2
    
    def test_hash_password_different(self):
        """Test that different passwords produce different hashes."""
        manager = UserManager()
        
        hash1 = manager._hash_password('password123')
        hash2 = manager._hash_password('password456')
        
        assert hash1 != hash2
    
    def test_generate_session_token_unique(self):
        """Test that session tokens are unique."""
        manager = UserManager()
        
        token1 = manager._generate_session_token('user1')
        token2 = manager._generate_session_token('user1')
        
        # Tokens should be different due to timestamp
        assert token1 != token2
