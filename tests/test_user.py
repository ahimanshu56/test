"""Tests for User model."""

import pytest
from datetime import datetime
from src.models.user import User


class TestUserCreation:
    """Tests for User creation and validation."""
    
    def test_user_creation_valid_all_fields(self):
        """Test creating user with all valid fields."""
        user = User("john_doe", "john@example.com", 25)
        
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert user.is_active is True
        assert isinstance(user.created_at, datetime)
    
    def test_user_creation_without_age(self):
        """Test creating user without age."""
        user = User("jane_doe", "jane@example.com")
        
        assert user.username == "jane_doe"
        assert user.email == "jane@example.com"
        assert user.age is None
    
    def test_user_creation_email_normalized_to_lowercase(self):
        """Test that email is normalized to lowercase."""
        user = User("john_doe", "John@EXAMPLE.COM")
        
        assert user.email == "john@example.com"
    
    def test_user_creation_sets_created_at(self):
        """Test that created_at is set automatically."""
        before = datetime.now()
        user = User("john_doe", "john@example.com")
        after = datetime.now()
        
        assert before <= user.created_at <= after
    
    def test_user_creation_active_by_default(self):
        """Test that user is active by default."""
        user = User("john_doe", "john@example.com")
        
        assert user.is_active is True


class TestUserUsernameValidation:
    """Tests for username validation."""
    
    def test_username_valid_alphanumeric(self):
        """Test valid alphanumeric username."""
        user = User("john123", "john@example.com")
        assert user.username == "john123"
    
    def test_username_valid_with_underscore(self):
        """Test valid username with underscore."""
        user = User("john_doe_123", "john@example.com")
        assert user.username == "john_doe_123"
    
    def test_username_valid_minimum_length(self):
        """Test username with minimum valid length (3 chars)."""
        user = User("abc", "test@example.com")
        assert user.username == "abc"
    
    def test_username_valid_maximum_length(self):
        """Test username with maximum valid length (20 chars)."""
        user = User("a" * 20, "test@example.com")
        assert user.username == "a" * 20
    
    def test_username_too_short_raises_error(self):
        """Test that username < 3 chars raises ValueError."""
        with pytest.raises(ValueError, match="Username must be 3-20 characters long"):
            User("ab", "test@example.com")
    
    def test_username_too_long_raises_error(self):
        """Test that username > 20 chars raises ValueError."""
        with pytest.raises(ValueError, match="Username must be 3-20 characters long"):
            User("a" * 21, "test@example.com")
    
    def test_username_empty_raises_error(self):
        """Test that empty username raises ValueError."""
        with pytest.raises(ValueError, match="Username must be 3-20 characters long"):
            User("", "test@example.com")
    
    def test_username_with_spaces_raises_error(self):
        """Test that username with spaces raises ValueError."""
        with pytest.raises(ValueError, match="Username can only contain alphanumeric characters"):
            User("john doe", "test@example.com")
    
    def test_username_with_special_chars_raises_error(self):
        """Test that username with special chars raises ValueError."""
        with pytest.raises(ValueError, match="Username can only contain alphanumeric characters"):
            User("john@doe", "test@example.com")
        
        with pytest.raises(ValueError, match="Username can only contain alphanumeric characters"):
            User("john-doe", "test@example.com")
    
    def test_username_not_string_raises_error(self):
        """Test that non-string username raises ValueError."""
        with pytest.raises(ValueError, match="Username must be a string"):
            User(123, "test@example.com")
        
        with pytest.raises(ValueError, match="Username must be a string"):
            User(None, "test@example.com")


class TestUserEmailValidation:
    """Tests for email validation."""
    
    def test_email_valid_standard(self):
        """Test valid standard email."""
        user = User("john_doe", "john@example.com")
        assert user.email == "john@example.com"
    
    def test_email_valid_with_subdomain(self):
        """Test valid email with subdomain."""
        user = User("john_doe", "john@mail.example.com")
        assert user.email == "john@mail.example.com"
    
    def test_email_valid_with_plus(self):
        """Test valid email with plus sign."""
        user = User("john_doe", "john+test@example.com")
        assert user.email == "john+test@example.com"
    
    def test_email_valid_with_dots(self):
        """Test valid email with dots."""
        user = User("john_doe", "john.doe@example.com")
        assert user.email == "john.doe@example.com"
    
    def test_email_valid_with_numbers(self):
        """Test valid email with numbers."""
        user = User("john_doe", "john123@example.com")
        assert user.email == "john123@example.com"
    
    def test_email_missing_at_raises_error(self):
        """Test that email without @ raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User("john_doe", "johnexample.com")
    
    def test_email_missing_domain_raises_error(self):
        """Test that email without domain raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User("john_doe", "john@")
    
    def test_email_missing_tld_raises_error(self):
        """Test that email without TLD raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User("john_doe", "john@example")
    
    def test_email_missing_local_part_raises_error(self):
        """Test that email without local part raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User("john_doe", "@example.com")
    
    def test_email_with_spaces_raises_error(self):
        """Test that email with spaces raises ValueError."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User("john_doe", "john doe@example.com")
    
    def test_email_not_string_raises_error(self):
        """Test that non-string email raises ValueError."""
        with pytest.raises(ValueError, match="Email must be a string"):
            User("john_doe", 123)
        
        with pytest.raises(ValueError, match="Email must be a string"):
            User("john_doe", None)


class TestUserAgeValidation:
    """Tests for age validation."""
    
    def test_age_valid_positive(self):
        """Test valid positive age."""
        user = User("john_doe", "john@example.com", 25)
        assert user.age == 25
    
    def test_age_valid_zero(self):
        """Test valid age of zero."""
        user = User("john_doe", "john@example.com", 0)
        assert user.age == 0
    
    def test_age_valid_maximum(self):
        """Test valid maximum age."""
        user = User("john_doe", "john@example.com", 150)
        assert user.age == 150
    
    def test_age_none_is_valid(self):
        """Test that None age is valid."""
        user = User("john_doe", "john@example.com", None)
        assert user.age is None
    
    def test_age_negative_raises_error(self):
        """Test that negative age raises ValueError."""
        with pytest.raises(ValueError, match="Age cannot be negative"):
            User("john_doe", "john@example.com", -1)
    
    def test_age_too_high_raises_error(self):
        """Test that age > 150 raises ValueError."""
        with pytest.raises(ValueError, match="Age must be realistic"):
            User("john_doe", "john@example.com", 151)
        
        with pytest.raises(ValueError, match="Age must be realistic"):
            User("john_doe", "john@example.com", 200)
    
    def test_age_not_integer_raises_error(self):
        """Test that non-integer age raises ValueError."""
        with pytest.raises(ValueError, match="Age must be an integer"):
            User("john_doe", "john@example.com", 25.5)
        
        with pytest.raises(ValueError, match="Age must be an integer"):
            User("john_doe", "john@example.com", "25")


class TestUserDeactivate:
    """Tests for user deactivation."""
    
    def test_deactivate_active_user(self):
        """Test deactivating an active user."""
        user = User("john_doe", "john@example.com")
        assert user.is_active is True
        
        user.deactivate()
        
        assert user.is_active is False
    
    def test_deactivate_already_inactive_user(self):
        """Test deactivating already inactive user."""
        user = User("john_doe", "john@example.com")
        user.deactivate()
        
        user.deactivate()
        
        assert user.is_active is False


class TestUserActivate:
    """Tests for user activation."""
    
    def test_activate_inactive_user(self):
        """Test activating an inactive user."""
        user = User("john_doe", "john@example.com")
        user.deactivate()
        assert user.is_active is False
        
        user.activate()
        
        assert user.is_active is True
    
    def test_activate_already_active_user(self):
        """Test activating already active user."""
        user = User("john_doe", "john@example.com")
        assert user.is_active is True
        
        user.activate()
        
        assert user.is_active is True


class TestUserUpdateEmail:
    """Tests for updating user email."""
    
    def test_update_email_valid(self):
        """Test updating email with valid address."""
        user = User("john_doe", "john@example.com")
        
        user.update_email("newemail@example.com")
        
        assert user.email == "newemail@example.com"
    
    def test_update_email_normalizes_case(self):
        """Test that updated email is normalized to lowercase."""
        user = User("john_doe", "john@example.com")
        
        user.update_email("NewEmail@EXAMPLE.COM")
        
        assert user.email == "newemail@example.com"
    
    def test_update_email_invalid_raises_error(self):
        """Test that invalid email raises ValueError."""
        user = User("john_doe", "john@example.com")
        
        with pytest.raises(ValueError, match="Invalid email format"):
            user.update_email("invalid-email")
    
    def test_update_email_preserves_other_fields(self):
        """Test that updating email doesn't affect other fields."""
        user = User("john_doe", "john@example.com", 25)
        original_username = user.username
        original_age = user.age
        original_created_at = user.created_at
        
        user.update_email("newemail@example.com")
        
        assert user.username == original_username
        assert user.age == original_age
        assert user.created_at == original_created_at


class TestUserToDict:
    """Tests for user to_dict method."""
    
    def test_to_dict_all_fields(self):
        """Test converting user with all fields to dict."""
        user = User("john_doe", "john@example.com", 25)
        
        user_dict = user.to_dict()
        
        assert user_dict['username'] == "john_doe"
        assert user_dict['email'] == "john@example.com"
        assert user_dict['age'] == 25
        assert user_dict['is_active'] is True
        assert 'created_at' in user_dict
        assert isinstance(user_dict['created_at'], str)
    
    def test_to_dict_without_age(self):
        """Test converting user without age to dict."""
        user = User("john_doe", "john@example.com")
        
        user_dict = user.to_dict()
        
        assert user_dict['age'] is None
    
    def test_to_dict_inactive_user(self):
        """Test converting inactive user to dict."""
        user = User("john_doe", "john@example.com")
        user.deactivate()
        
        user_dict = user.to_dict()
        
        assert user_dict['is_active'] is False
    
    def test_to_dict_created_at_is_iso_format(self):
        """Test that created_at is in ISO format."""
        user = User("john_doe", "john@example.com")
        
        user_dict = user.to_dict()
        
        # Should be able to parse ISO format
        datetime.fromisoformat(user_dict['created_at'])


class TestUserRepr:
    """Tests for user __repr__ method."""
    
    def test_repr_with_age(self):
        """Test string representation with age."""
        user = User("john_doe", "john@example.com", 25)
        
        repr_str = repr(user)
        
        assert "john_doe" in repr_str
        assert "john@example.com" in repr_str
        assert "25" in repr_str
    
    def test_repr_without_age(self):
        """Test string representation without age."""
        user = User("john_doe", "john@example.com")
        
        repr_str = repr(user)
        
        assert "john_doe" in repr_str
        assert "john@example.com" in repr_str
        assert "None" in repr_str


class TestUserEquality:
    """Tests for user equality comparison."""
    
    def test_equality_same_username_and_email(self):
        """Test that users with same username and email are equal."""
        user1 = User("john_doe", "john@example.com", 25)
        user2 = User("john_doe", "john@example.com", 30)
        
        assert user1 == user2
    
    def test_equality_different_username(self):
        """Test that users with different usernames are not equal."""
        user1 = User("john_doe", "john@example.com")
        user2 = User("jane_doe", "john@example.com")
        
        assert user1 != user2
    
    def test_equality_different_email(self):
        """Test that users with different emails are not equal."""
        user1 = User("john_doe", "john@example.com")
        user2 = User("john_doe", "jane@example.com")
        
        assert user1 != user2
    
    def test_equality_with_non_user_object(self):
        """Test that user is not equal to non-User object."""
        user = User("john_doe", "john@example.com")
        
        assert user != "john_doe"
        assert user != 123
        assert user != None
        assert user != {"username": "john_doe"}
    
    def test_equality_same_object(self):
        """Test that user equals itself."""
        user = User("john_doe", "john@example.com")
        
        assert user == user
