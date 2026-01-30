"""Comprehensive tests for user_manager module."""
import pytest
from src.user_manager import User, UserManager


class TestUser:
    """Test User class."""
    
    def test_user_creation(self):
        """Test creating a user."""
        user = User("john_doe", "john@example.com", 25)
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert user.is_active is True
    
    def test_user_repr(self):
        """Test user string representation."""
        user = User("john_doe", "john@example.com", 25)
        repr_str = repr(user)
        assert "john_doe" in repr_str
        assert "john@example.com" in repr_str
        assert "25" in repr_str
    
    def test_deactivate_user(self):
        """Test deactivating a user."""
        user = User("john_doe", "john@example.com", 25)
        user.deactivate()
        assert user.is_active is False
    
    def test_activate_user(self):
        """Test activating a user."""
        user = User("john_doe", "john@example.com", 25)
        user.deactivate()
        user.activate()
        assert user.is_active is True


class TestUserManager:
    """Test UserManager class."""
    
    def test_validate_email_valid(self):
        """Test email validation with valid emails."""
        manager = UserManager()
        assert manager.validate_email("test@example.com") is True
        assert manager.validate_email("user.name@domain.co.uk") is True
        assert manager.validate_email("user+tag@example.com") is True
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid emails."""
        manager = UserManager()
        assert manager.validate_email("invalid") is False
        assert manager.validate_email("@example.com") is False
        assert manager.validate_email("user@") is False
        assert manager.validate_email("user@domain") is False
        assert manager.validate_email("") is False
    
    def test_validate_username_valid(self):
        """Test username validation with valid usernames."""
        manager = UserManager()
        assert manager.validate_username("john123") is True
        assert manager.validate_username("user") is True
        assert manager.validate_username("a" * 20) is True
    
    def test_validate_username_invalid(self):
        """Test username validation with invalid usernames."""
        manager = UserManager()
        assert manager.validate_username("ab") is False  # Too short
        assert manager.validate_username("a" * 21) is False  # Too long
        assert manager.validate_username("user_name") is False  # Contains underscore
        assert manager.validate_username("user-name") is False  # Contains hyphen
        assert manager.validate_username("") is False  # Empty
        assert manager.validate_username(None) is False  # None
    
    def test_validate_age_valid(self):
        """Test age validation with valid ages."""
        manager = UserManager()
        assert manager.validate_age(13) is True
        assert manager.validate_age(25) is True
        assert manager.validate_age(120) is True
    
    def test_validate_age_invalid(self):
        """Test age validation with invalid ages."""
        manager = UserManager()
        assert manager.validate_age(12) is False  # Too young
        assert manager.validate_age(121) is False  # Too old
        assert manager.validate_age(-5) is False  # Negative
        assert manager.validate_age(25.5) is False  # Float
    
    def test_create_user_success(self):
        """Test creating a valid user."""
        manager = UserManager()
        user = manager.create_user("john123", "john@example.com", 25)
        
        assert user.username == "john123"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert manager.count_users() == 1
    
    def test_create_user_invalid_username(self):
        """Test creating user with invalid username."""
        manager = UserManager()
        with pytest.raises(ValueError, match="Invalid username"):
            manager.create_user("ab", "john@example.com", 25)
    
    def test_create_user_invalid_email(self):
        """Test creating user with invalid email."""
        manager = UserManager()
        with pytest.raises(ValueError, match="Invalid email"):
            manager.create_user("john123", "invalid-email", 25)
    
    def test_create_user_invalid_age(self):
        """Test creating user with invalid age."""
        manager = UserManager()
        with pytest.raises(ValueError, match="Invalid age"):
            manager.create_user("john123", "john@example.com", 10)
    
    def test_create_duplicate_user(self):
        """Test creating duplicate user raises error."""
        manager = UserManager()
        manager.create_user("john123", "john@example.com", 25)
        
        with pytest.raises(ValueError, match="already exists"):
            manager.create_user("john123", "other@example.com", 30)
    
    def test_get_user_exists(self):
        """Test getting an existing user."""
        manager = UserManager()
        created_user = manager.create_user("john123", "john@example.com", 25)
        retrieved_user = manager.get_user("john123")
        
        assert retrieved_user is created_user
        assert retrieved_user.username == "john123"
    
    def test_get_user_not_exists(self):
        """Test getting a non-existent user."""
        manager = UserManager()
        user = manager.get_user("nonexistent")
        assert user is None
    
    def test_delete_user_exists(self):
        """Test deleting an existing user."""
        manager = UserManager()
        manager.create_user("john123", "john@example.com", 25)
        
        result = manager.delete_user("john123")
        assert result is True
        assert manager.count_users() == 0
    
    def test_delete_user_not_exists(self):
        """Test deleting a non-existent user."""
        manager = UserManager()
        result = manager.delete_user("nonexistent")
        assert result is False
    
    def test_list_users(self):
        """Test listing all users."""
        manager = UserManager()
        user1 = manager.create_user("john123", "john@example.com", 25)
        user2 = manager.create_user("jane456", "jane@example.com", 30)
        
        users = manager.list_users()
        assert len(users) == 2
        assert user1 in users
        assert user2 in users
    
    def test_list_users_empty(self):
        """Test listing users when none exist."""
        manager = UserManager()
        users = manager.list_users()
        assert len(users) == 0
    
    def test_list_active_users(self):
        """Test listing only active users."""
        manager = UserManager()
        user1 = manager.create_user("john123", "john@example.com", 25)
        user2 = manager.create_user("jane456", "jane@example.com", 30)
        user1.deactivate()
        
        active_users = manager.list_active_users()
        assert len(active_users) == 1
        assert user2 in active_users
        assert user1 not in active_users
    
    def test_count_users(self):
        """Test counting users."""
        manager = UserManager()
        assert manager.count_users() == 0
        
        manager.create_user("john123", "john@example.com", 25)
        assert manager.count_users() == 1
        
        manager.create_user("jane456", "jane@example.com", 30)
        assert manager.count_users() == 2
    
    def test_update_email_success(self):
        """Test updating user email successfully."""
        manager = UserManager()
        manager.create_user("john123", "john@example.com", 25)
        
        result = manager.update_email("john123", "newemail@example.com")
        assert result is True
        
        user = manager.get_user("john123")
        assert user.email == "newemail@example.com"
    
    def test_update_email_invalid_format(self):
        """Test updating email with invalid format."""
        manager = UserManager()
        manager.create_user("john123", "john@example.com", 25)
        
        with pytest.raises(ValueError, match="Invalid email"):
            manager.update_email("john123", "invalid-email")
    
    def test_update_email_user_not_exists(self):
        """Test updating email for non-existent user."""
        manager = UserManager()
        result = manager.update_email("nonexistent", "new@example.com")
        assert result is False
