"""Tests for UserService."""

import pytest
from src.services.user_service import UserService
from src.models.user import User


class TestUserServiceCreateUser:
    """Tests for UserService.create_user method."""
    
    def test_create_user_valid_input(self):
        """Test creating user with valid input."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com", 25)
        
        assert user_id == 1
        assert isinstance(user, User)
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert user.is_active is True
    
    def test_create_user_without_age(self):
        """Test creating user without age."""
        service = UserService()
        user_id, user = service.create_user("jane_doe", "jane@example.com")
        
        assert user_id == 1
        assert user.username == "jane_doe"
        assert user.email == "jane@example.com"
        assert user.age is None
    
    def test_create_user_increments_id(self):
        """Test that user IDs increment correctly."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        user_id2, _ = service.create_user("user2", "user2@example.com")
        user_id3, _ = service.create_user("user3", "user3@example.com")
        
        assert user_id1 == 1
        assert user_id2 == 2
        assert user_id3 == 3
    
    def test_create_user_duplicate_username_raises_error(self):
        """Test that duplicate username raises ValueError."""
        service = UserService()
        service.create_user("john_doe", "john@example.com")
        
        with pytest.raises(ValueError, match="Username 'john_doe' already exists"):
            service.create_user("john_doe", "different@example.com")
    
    def test_create_user_invalid_username_raises_error(self):
        """Test that invalid username raises ValueError."""
        service = UserService()
        
        with pytest.raises(ValueError):
            service.create_user("ab", "test@example.com")  # Too short
    
    def test_create_user_invalid_email_raises_error(self):
        """Test that invalid email raises ValueError."""
        service = UserService()
        
        with pytest.raises(ValueError):
            service.create_user("john_doe", "invalid-email")
    
    def test_create_user_invalid_age_raises_error(self):
        """Test that invalid age raises ValueError."""
        service = UserService()
        
        with pytest.raises(ValueError):
            service.create_user("john_doe", "john@example.com", -5)


class TestUserServiceGetUser:
    """Tests for UserService.get_user method."""
    
    def test_get_user_exists(self):
        """Test getting existing user."""
        service = UserService()
        user_id, created_user = service.create_user("john_doe", "john@example.com")
        
        retrieved_user = service.get_user(user_id)
        
        assert retrieved_user is not None
        assert retrieved_user.username == "john_doe"
        assert retrieved_user == created_user
    
    def test_get_user_not_exists(self):
        """Test getting non-existent user."""
        service = UserService()
        
        user = service.get_user(999)
        
        assert user is None
    
    def test_get_user_after_multiple_creates(self):
        """Test getting specific user after creating multiple."""
        service = UserService()
        user_id1, user1 = service.create_user("user1", "user1@example.com")
        user_id2, user2 = service.create_user("user2", "user2@example.com")
        user_id3, user3 = service.create_user("user3", "user3@example.com")
        
        assert service.get_user(user_id1) == user1
        assert service.get_user(user_id2) == user2
        assert service.get_user(user_id3) == user3


class TestUserServiceGetUserByUsername:
    """Tests for UserService.get_user_by_username method."""
    
    def test_get_user_by_username_exists(self):
        """Test getting user by username when exists."""
        service = UserService()
        created_id, created_user = service.create_user("john_doe", "john@example.com")
        
        user_id, user = service.get_user_by_username("john_doe")
        
        assert user_id == created_id
        assert user == created_user
    
    def test_get_user_by_username_not_exists(self):
        """Test getting user by username when not exists."""
        service = UserService()
        
        user_id, user = service.get_user_by_username("nonexistent")
        
        assert user_id is None
        assert user is None
    
    def test_get_user_by_username_multiple_users(self):
        """Test getting specific user by username with multiple users."""
        service = UserService()
        service.create_user("user1", "user1@example.com")
        user_id2, user2 = service.create_user("user2", "user2@example.com")
        service.create_user("user3", "user3@example.com")
        
        found_id, found_user = service.get_user_by_username("user2")
        
        assert found_id == user_id2
        assert found_user == user2


class TestUserServiceUpdateUserEmail:
    """Tests for UserService.update_user_email method."""
    
    def test_update_user_email_valid(self):
        """Test updating user email with valid data."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        
        result = service.update_user_email(user_id, "newemail@example.com")
        
        assert result is True
        assert user.email == "newemail@example.com"
    
    def test_update_user_email_user_not_found(self):
        """Test updating email for non-existent user."""
        service = UserService()
        
        result = service.update_user_email(999, "test@example.com")
        
        assert result is False
    
    def test_update_user_email_invalid_email_raises_error(self):
        """Test updating with invalid email raises ValueError."""
        service = UserService()
        user_id, _ = service.create_user("john_doe", "john@example.com")
        
        with pytest.raises(ValueError):
            service.update_user_email(user_id, "invalid-email")
    
    def test_update_user_email_normalizes_case(self):
        """Test that email is normalized to lowercase."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        
        service.update_user_email(user_id, "NewEmail@EXAMPLE.COM")
        
        assert user.email == "newemail@example.com"


class TestUserServiceDeleteUser:
    """Tests for UserService.delete_user method."""
    
    def test_delete_user_exists(self):
        """Test deleting existing user."""
        service = UserService()
        user_id, _ = service.create_user("john_doe", "john@example.com")
        
        result = service.delete_user(user_id)
        
        assert result is True
        assert service.get_user(user_id) is None
        assert service.count_users() == 0
    
    def test_delete_user_not_exists(self):
        """Test deleting non-existent user."""
        service = UserService()
        
        result = service.delete_user(999)
        
        assert result is False
    
    def test_delete_user_multiple_users(self):
        """Test deleting one user doesn't affect others."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        user_id2, _ = service.create_user("user2", "user2@example.com")
        user_id3, _ = service.create_user("user3", "user3@example.com")
        
        service.delete_user(user_id2)
        
        assert service.get_user(user_id1) is not None
        assert service.get_user(user_id2) is None
        assert service.get_user(user_id3) is not None
        assert service.count_users() == 2


class TestUserServiceDeactivateUser:
    """Tests for UserService.deactivate_user method."""
    
    def test_deactivate_user_exists(self):
        """Test deactivating existing user."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        
        result = service.deactivate_user(user_id)
        
        assert result is True
        assert user.is_active is False
    
    def test_deactivate_user_not_exists(self):
        """Test deactivating non-existent user."""
        service = UserService()
        
        result = service.deactivate_user(999)
        
        assert result is False
    
    def test_deactivate_already_inactive_user(self):
        """Test deactivating already inactive user."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        service.deactivate_user(user_id)
        
        result = service.deactivate_user(user_id)
        
        assert result is True
        assert user.is_active is False


class TestUserServiceActivateUser:
    """Tests for UserService.activate_user method."""
    
    def test_activate_user_exists(self):
        """Test activating existing inactive user."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        user.deactivate()
        
        result = service.activate_user(user_id)
        
        assert result is True
        assert user.is_active is True
    
    def test_activate_user_not_exists(self):
        """Test activating non-existent user."""
        service = UserService()
        
        result = service.activate_user(999)
        
        assert result is False
    
    def test_activate_already_active_user(self):
        """Test activating already active user."""
        service = UserService()
        user_id, user = service.create_user("john_doe", "john@example.com")
        
        result = service.activate_user(user_id)
        
        assert result is True
        assert user.is_active is True


class TestUserServiceListActiveUsers:
    """Tests for UserService.list_active_users method."""
    
    def test_list_active_users_all_active(self):
        """Test listing when all users are active."""
        service = UserService()
        user_id1, user1 = service.create_user("user1", "user1@example.com")
        user_id2, user2 = service.create_user("user2", "user2@example.com")
        
        active_users = service.list_active_users()
        
        assert len(active_users) == 2
        assert (user_id1, user1) in active_users
        assert (user_id2, user2) in active_users
    
    def test_list_active_users_some_inactive(self):
        """Test listing when some users are inactive."""
        service = UserService()
        user_id1, user1 = service.create_user("user1", "user1@example.com")
        user_id2, _ = service.create_user("user2", "user2@example.com")
        user_id3, user3 = service.create_user("user3", "user3@example.com")
        
        service.deactivate_user(user_id2)
        
        active_users = service.list_active_users()
        
        assert len(active_users) == 2
        assert (user_id1, user1) in active_users
        assert (user_id3, user3) in active_users
    
    def test_list_active_users_none_active(self):
        """Test listing when no users are active."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        user_id2, _ = service.create_user("user2", "user2@example.com")
        
        service.deactivate_user(user_id1)
        service.deactivate_user(user_id2)
        
        active_users = service.list_active_users()
        
        assert len(active_users) == 0
    
    def test_list_active_users_empty_service(self):
        """Test listing when no users exist."""
        service = UserService()
        
        active_users = service.list_active_users()
        
        assert len(active_users) == 0


class TestUserServiceCountUsers:
    """Tests for UserService.count_users method."""
    
    def test_count_users_empty(self):
        """Test counting users in empty service."""
        service = UserService()
        
        assert service.count_users() == 0
    
    def test_count_users_single(self):
        """Test counting with single user."""
        service = UserService()
        service.create_user("user1", "user1@example.com")
        
        assert service.count_users() == 1
    
    def test_count_users_multiple(self):
        """Test counting with multiple users."""
        service = UserService()
        service.create_user("user1", "user1@example.com")
        service.create_user("user2", "user2@example.com")
        service.create_user("user3", "user3@example.com")
        
        assert service.count_users() == 3
    
    def test_count_users_includes_inactive(self):
        """Test that count includes inactive users."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        service.create_user("user2", "user2@example.com")
        
        service.deactivate_user(user_id1)
        
        assert service.count_users() == 2
    
    def test_count_users_after_deletion(self):
        """Test count after deleting users."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        service.create_user("user2", "user2@example.com")
        
        service.delete_user(user_id1)
        
        assert service.count_users() == 1


class TestUserServiceCountActiveUsers:
    """Tests for UserService.count_active_users method."""
    
    def test_count_active_users_all_active(self):
        """Test counting when all users are active."""
        service = UserService()
        service.create_user("user1", "user1@example.com")
        service.create_user("user2", "user2@example.com")
        
        assert service.count_active_users() == 2
    
    def test_count_active_users_some_inactive(self):
        """Test counting when some users are inactive."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        service.create_user("user2", "user2@example.com")
        service.create_user("user3", "user3@example.com")
        
        service.deactivate_user(user_id1)
        
        assert service.count_active_users() == 2
    
    def test_count_active_users_none_active(self):
        """Test counting when no users are active."""
        service = UserService()
        user_id1, _ = service.create_user("user1", "user1@example.com")
        user_id2, _ = service.create_user("user2", "user2@example.com")
        
        service.deactivate_user(user_id1)
        service.deactivate_user(user_id2)
        
        assert service.count_active_users() == 0
    
    def test_count_active_users_empty_service(self):
        """Test counting in empty service."""
        service = UserService()
        
        assert service.count_active_users() == 0
