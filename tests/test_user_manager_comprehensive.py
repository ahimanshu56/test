"""
Comprehensive tests for user_manager module to achieve high coverage.
"""
import pytest
from src.user_manager import UserManager


class TestUserManagerValidation:
    """Test validation methods."""
    
    def test_validate_email_valid(self):
        """Test email validation with valid emails."""
        manager = UserManager()
        assert manager.validate_email("user@example.com") is True
        assert manager.validate_email("test.user+tag@domain.co.uk") is True
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid emails."""
        manager = UserManager()
        assert manager.validate_email("") is False
        assert manager.validate_email("invalid") is False
        assert manager.validate_email("@example.com") is False
        assert manager.validate_email("user@") is False
        assert manager.validate_email(None) is False
        assert manager.validate_email(123) is False
    
    def test_validate_password_valid(self):
        """Test password validation with valid passwords."""
        manager = UserManager()
        is_valid, error = manager.validate_password("Password123")
        assert is_valid is True
        assert error is None
    
    def test_validate_password_too_short(self):
        """Test password validation with short password."""
        manager = UserManager()
        is_valid, error = manager.validate_password("Pass1")
        assert is_valid is False
        assert "at least 8 characters" in error
    
    def test_validate_password_no_uppercase(self):
        """Test password validation without uppercase."""
        manager = UserManager()
        is_valid, error = manager.validate_password("password123")
        assert is_valid is False
        assert "uppercase" in error
    
    def test_validate_password_no_lowercase(self):
        """Test password validation without lowercase."""
        manager = UserManager()
        is_valid, error = manager.validate_password("PASSWORD123")
        assert is_valid is False
        assert "lowercase" in error
    
    def test_validate_password_no_digit(self):
        """Test password validation without digit."""
        manager = UserManager()
        is_valid, error = manager.validate_password("Password")
        assert is_valid is False
        assert "digit" in error
    
    def test_validate_password_empty(self):
        """Test password validation with empty password."""
        manager = UserManager()
        is_valid, error = manager.validate_password("")
        assert is_valid is False
        assert "cannot be empty" in error
    
    def test_validate_password_none(self):
        """Test password validation with None."""
        manager = UserManager()
        is_valid, error = manager.validate_password(None)
        assert is_valid is False
        assert "cannot be empty" in error


class TestUserManagerCreateUser:
    """Test user creation."""
    
    def test_create_user_success(self):
        """Test creating user with valid data."""
        manager = UserManager()
        user = manager.create_user("john_doe", "john@example.com", "Password123")
        
        assert user["username"] == "john_doe"
        assert user["email"] == "john@example.com"
        assert user["active"] is True
        assert "password" not in user
    
    def test_create_user_duplicate(self):
        """Test creating duplicate user."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        with pytest.raises(ValueError, match="already exists"):
            manager.create_user("john_doe", "another@example.com", "Password123")
    
    def test_create_user_invalid_username(self):
        """Test creating user with invalid username."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Username is required"):
            manager.create_user("", "john@example.com", "Password123")
        
        with pytest.raises(ValueError, match="Username is required"):
            manager.create_user(None, "john@example.com", "Password123")
    
    def test_create_user_invalid_email(self):
        """Test creating user with invalid email."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="Invalid email"):
            manager.create_user("john_doe", "invalid-email", "Password123")
    
    def test_create_user_invalid_password(self):
        """Test creating user with invalid password."""
        manager = UserManager()
        
        with pytest.raises(ValueError, match="at least 8 characters"):
            manager.create_user("john_doe", "john@example.com", "Pass1")


class TestUserManagerAuthentication:
    """Test authentication functionality."""
    
    def test_authenticate_success(self):
        """Test successful authentication."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        token = manager.authenticate("john_doe", "Password123")
        assert token is not None
        assert token.startswith("session_john_doe")
        assert token in manager.active_sessions
    
    def test_authenticate_wrong_password(self):
        """Test authentication with wrong password."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        token = manager.authenticate("john_doe", "WrongPassword")
        assert token is None
        assert manager.users["john_doe"]["login_attempts"] == 1
    
    def test_authenticate_nonexistent_user(self):
        """Test authentication with nonexistent user."""
        manager = UserManager()
        token = manager.authenticate("nonexistent", "Password123")
        assert token is None
    
    def test_authenticate_empty_username(self):
        """Test authentication with empty username."""
        manager = UserManager()
        token = manager.authenticate("", "Password123")
        assert token is None
    
    def test_authenticate_inactive_user(self):
        """Test authentication with inactive user."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        manager.deactivate_user("john_doe")
        
        token = manager.authenticate("john_doe", "Password123")
        assert token is None
    
    def test_authenticate_max_attempts(self):
        """Test account lockout after max failed attempts."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        # Fail 3 times
        for _ in range(3):
            token = manager.authenticate("john_doe", "WrongPassword")
            assert token is None
        
        # Account should be locked
        assert manager.users["john_doe"]["active"] is False
        
        # Even correct password should fail
        token = manager.authenticate("john_doe", "Password123")
        assert token is None
    
    def test_authenticate_resets_attempts_on_success(self):
        """Test that successful login resets failed attempts."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        # Fail once
        manager.authenticate("john_doe", "WrongPassword")
        assert manager.users["john_doe"]["login_attempts"] == 1
        
        # Succeed
        token = manager.authenticate("john_doe", "Password123")
        assert token is not None
        assert manager.users["john_doe"]["login_attempts"] == 0


class TestUserManagerLogout:
    """Test logout functionality."""
    
    def test_logout_success(self):
        """Test successful logout."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        token = manager.authenticate("john_doe", "Password123")
        
        result = manager.logout(token)
        assert result is True
        assert token not in manager.active_sessions
    
    def test_logout_invalid_token(self):
        """Test logout with invalid token."""
        manager = UserManager()
        result = manager.logout("invalid_token")
        assert result is False


class TestUserManagerGetUser:
    """Test getting user information."""
    
    def test_get_user_exists(self):
        """Test getting existing user."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        user = manager.get_user("john_doe")
        assert user is not None
        assert user["username"] == "john_doe"
        assert user["email"] == "john@example.com"
        assert "password" not in user
    
    def test_get_user_not_exists(self):
        """Test getting nonexistent user."""
        manager = UserManager()
        user = manager.get_user("nonexistent")
        assert user is None


class TestUserManagerListUsers:
    """Test listing users."""
    
    def test_list_users_empty(self):
        """Test listing users when none exist."""
        manager = UserManager()
        users = manager.list_users()
        assert users == []
    
    def test_list_users_all(self):
        """Test listing all users."""
        manager = UserManager()
        manager.create_user("user1", "user1@example.com", "Password123")
        manager.create_user("user2", "user2@example.com", "Password123")
        
        users = manager.list_users()
        assert len(users) == 2
        assert all("password" not in u for u in users)
    
    def test_list_users_active_only(self):
        """Test listing only active users."""
        manager = UserManager()
        manager.create_user("user1", "user1@example.com", "Password123")
        manager.create_user("user2", "user2@example.com", "Password123")
        manager.deactivate_user("user2")
        
        users = manager.list_users(active_only=True)
        assert len(users) == 1
        assert users[0]["username"] == "user1"


class TestUserManagerDeactivateUser:
    """Test user deactivation."""
    
    def test_deactivate_user_success(self):
        """Test deactivating existing user."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        
        result = manager.deactivate_user("john_doe")
        assert result is True
        assert manager.users["john_doe"]["active"] is False
    
    def test_deactivate_user_not_exists(self):
        """Test deactivating nonexistent user."""
        manager = UserManager()
        result = manager.deactivate_user("nonexistent")
        assert result is False
    
    def test_deactivate_user_removes_sessions(self):
        """Test that deactivation removes active sessions."""
        manager = UserManager()
        manager.create_user("john_doe", "john@example.com", "Password123")
        token = manager.authenticate("john_doe", "Password123")
        
        assert token in manager.active_sessions
        
        manager.deactivate_user("john_doe")
        assert token not in manager.active_sessions
