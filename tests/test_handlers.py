"""Tests for API handlers."""

import pytest
from src.api.handlers import APIHandler


class TestHandleCreateUser:
    """Tests for APIHandler.handle_create_user method."""
    
    def test_handle_create_user_valid_with_age(self):
        """Test creating user with valid data including age."""
        handler = APIHandler()
        request_data = {
            'username': 'john_doe',
            'email': 'john@example.com',
            'age': 25
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is True
        assert response['user_id'] == 1
        assert 'message' in response
        assert response['user']['username'] == 'john_doe'
        assert response['user']['email'] == 'john@example.com'
        assert response['user']['age'] == 25
    
    def test_handle_create_user_valid_without_age(self):
        """Test creating user without age."""
        handler = APIHandler()
        request_data = {
            'username': 'jane_doe',
            'email': 'jane@example.com'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is True
        assert response['user']['age'] is None
    
    def test_handle_create_user_invalid_request_format(self):
        """Test with invalid request format (not a dict)."""
        handler = APIHandler()
        
        response = handler.handle_create_user("invalid")
        
        assert response['success'] is False
        assert 'Invalid request format' in response['error']
    
    def test_handle_create_user_missing_username(self):
        """Test with missing username."""
        handler = APIHandler()
        request_data = {
            'email': 'john@example.com'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'Username and email are required' in response['error']
    
    def test_handle_create_user_missing_email(self):
        """Test with missing email."""
        handler = APIHandler()
        request_data = {
            'username': 'john_doe'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'Username and email are required' in response['error']
    
    def test_handle_create_user_empty_username(self):
        """Test with empty username."""
        handler = APIHandler()
        request_data = {
            'username': '',
            'email': 'john@example.com'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'Username and email are required' in response['error']
    
    def test_handle_create_user_empty_email(self):
        """Test with empty email."""
        handler = APIHandler()
        request_data = {
            'username': 'john_doe',
            'email': ''
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'Username and email are required' in response['error']
    
    def test_handle_create_user_invalid_username(self):
        """Test with invalid username format."""
        handler = APIHandler()
        request_data = {
            'username': 'ab',  # Too short
            'email': 'john@example.com'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'error' in response
    
    def test_handle_create_user_invalid_email(self):
        """Test with invalid email format."""
        handler = APIHandler()
        request_data = {
            'username': 'john_doe',
            'email': 'invalid-email'
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'error' in response
    
    def test_handle_create_user_invalid_age(self):
        """Test with invalid age."""
        handler = APIHandler()
        request_data = {
            'username': 'john_doe',
            'email': 'john@example.com',
            'age': -5
        }
        
        response = handler.handle_create_user(request_data)
        
        assert response['success'] is False
        assert 'error' in response
    
    def test_handle_create_user_duplicate_username(self):
        """Test creating user with duplicate username."""
        handler = APIHandler()
        request_data1 = {
            'username': 'john_doe',
            'email': 'john@example.com'
        }
        request_data2 = {
            'username': 'john_doe',
            'email': 'different@example.com'
        }
        
        handler.handle_create_user(request_data1)
        response = handler.handle_create_user(request_data2)
        
        assert response['success'] is False
        assert 'already exists' in response['error']
    
    def test_handle_create_user_none_request(self):
        """Test with None request."""
        handler = APIHandler()
        
        response = handler.handle_create_user(None)
        
        assert response['success'] is False
        assert 'Invalid request format' in response['error']


class TestHandleGetUser:
    """Tests for APIHandler.handle_get_user method."""
    
    def test_handle_get_user_valid_existing_user(self):
        """Test getting existing user."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com',
            'age': 25
        })
        user_id = create_response['user_id']
        
        response = handler.handle_get_user(user_id)
        
        assert response['success'] is True
        assert response['user']['username'] == 'john_doe'
        assert response['user']['email'] == 'john@example.com'
        assert response['user']['age'] == 25
    
    def test_handle_get_user_not_found(self):
        """Test getting non-existent user."""
        handler = APIHandler()
        
        response = handler.handle_get_user(999)
        
        assert response['success'] is False
        assert 'User not found' in response['error']
    
    def test_handle_get_user_invalid_id_type(self):
        """Test with invalid user ID type."""
        handler = APIHandler()
        
        response = handler.handle_get_user("invalid")
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']
    
    def test_handle_get_user_none_id(self):
        """Test with None user ID."""
        handler = APIHandler()
        
        response = handler.handle_get_user(None)
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']
    
    def test_handle_get_user_float_id(self):
        """Test with float user ID."""
        handler = APIHandler()
        
        response = handler.handle_get_user(1.5)
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']


class TestHandleUpdateUserEmail:
    """Tests for APIHandler.handle_update_user_email method."""
    
    def test_handle_update_user_email_valid(self):
        """Test updating user email with valid data."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_update_user_email(user_id, 'newemail@example.com')
        
        assert response['success'] is True
        assert 'Email updated successfully' in response['message']
    
    def test_handle_update_user_email_user_not_found(self):
        """Test updating email for non-existent user."""
        handler = APIHandler()
        
        response = handler.handle_update_user_email(999, 'test@example.com')
        
        assert response['success'] is False
        assert 'User not found' in response['error']
    
    def test_handle_update_user_email_invalid_id_type(self):
        """Test with invalid user ID type."""
        handler = APIHandler()
        
        response = handler.handle_update_user_email("invalid", 'test@example.com')
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']
    
    def test_handle_update_user_email_empty_email(self):
        """Test with empty new email."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_update_user_email(user_id, '')
        
        assert response['success'] is False
        assert 'New email is required' in response['error']
    
    def test_handle_update_user_email_none_email(self):
        """Test with None new email."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_update_user_email(user_id, None)
        
        assert response['success'] is False
        assert 'New email is required' in response['error']
    
    def test_handle_update_user_email_invalid_format(self):
        """Test with invalid email format."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_update_user_email(user_id, 'invalid-email')
        
        assert response['success'] is False
        assert 'error' in response
    
    def test_handle_update_user_email_verifies_update(self):
        """Test that email is actually updated."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        handler.handle_update_user_email(user_id, 'newemail@example.com')
        get_response = handler.handle_get_user(user_id)
        
        assert get_response['user']['email'] == 'newemail@example.com'


class TestHandleDeleteUser:
    """Tests for APIHandler.handle_delete_user method."""
    
    def test_handle_delete_user_valid(self):
        """Test deleting existing user."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_delete_user(user_id)
        
        assert response['success'] is True
        assert 'User deleted successfully' in response['message']
    
    def test_handle_delete_user_not_found(self):
        """Test deleting non-existent user."""
        handler = APIHandler()
        
        response = handler.handle_delete_user(999)
        
        assert response['success'] is False
        assert 'User not found' in response['error']
    
    def test_handle_delete_user_invalid_id_type(self):
        """Test with invalid user ID type."""
        handler = APIHandler()
        
        response = handler.handle_delete_user("invalid")
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']
    
    def test_handle_delete_user_verifies_deletion(self):
        """Test that user is actually deleted."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        handler.handle_delete_user(user_id)
        get_response = handler.handle_get_user(user_id)
        
        assert get_response['success'] is False
        assert 'User not found' in get_response['error']
    
    def test_handle_delete_user_none_id(self):
        """Test with None user ID."""
        handler = APIHandler()
        
        response = handler.handle_delete_user(None)
        
        assert response['success'] is False
        assert 'User ID must be an integer' in response['error']


class TestHandleListUsers:
    """Tests for APIHandler.handle_list_users method."""
    
    def test_handle_list_users_empty(self):
        """Test listing users when none exist."""
        handler = APIHandler()
        
        response = handler.handle_list_users()
        
        assert response['success'] is True
        assert response['users'] == []
        assert response['count'] == 0
    
    def test_handle_list_users_multiple_users(self):
        """Test listing multiple users."""
        handler = APIHandler()
        handler.handle_create_user({
            'username': 'user1',
            'email': 'user1@example.com'
        })
        handler.handle_create_user({
            'username': 'user2',
            'email': 'user2@example.com'
        })
        handler.handle_create_user({
            'username': 'user3',
            'email': 'user3@example.com'
        })
        
        response = handler.handle_list_users()
        
        assert response['success'] is True
        assert len(response['users']) == 3
        assert response['count'] == 3
    
    def test_handle_list_users_includes_user_id(self):
        """Test that listed users include user_id."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        
        response = handler.handle_list_users()
        
        assert response['users'][0]['user_id'] == user_id
    
    def test_handle_list_users_includes_all_fields(self):
        """Test that listed users include all fields."""
        handler = APIHandler()
        handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com',
            'age': 25
        })
        
        response = handler.handle_list_users()
        
        user = response['users'][0]
        assert 'user_id' in user
        assert 'username' in user
        assert 'email' in user
        assert 'age' in user
        assert 'is_active' in user
        assert 'created_at' in user
    
    def test_handle_list_users_includes_inactive(self):
        """Test that listing includes inactive users by default."""
        handler = APIHandler()
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com'
        })
        user_id = create_response['user_id']
        handler.user_service.deactivate_user(user_id)
        
        response = handler.handle_list_users()
        
        assert response['count'] == 1
        assert response['users'][0]['is_active'] is False
    
    def test_handle_list_users_active_only_true(self):
        """Test listing only active users."""
        handler = APIHandler()
        user_id1 = handler.handle_create_user({
            'username': 'user1',
            'email': 'user1@example.com'
        })['user_id']
        handler.handle_create_user({
            'username': 'user2',
            'email': 'user2@example.com'
        })
        user_id3 = handler.handle_create_user({
            'username': 'user3',
            'email': 'user3@example.com'
        })['user_id']
        
        handler.user_service.deactivate_user(user_id1)
        handler.user_service.deactivate_user(user_id3)
        
        response = handler.handle_list_users(active_only=True)
        
        assert response['success'] is True
        assert response['count'] == 1
        assert response['users'][0]['username'] == 'user2'
    
    def test_handle_list_users_active_only_false(self):
        """Test listing all users explicitly."""
        handler = APIHandler()
        user_id = handler.handle_create_user({
            'username': 'user1',
            'email': 'user1@example.com'
        })['user_id']
        handler.handle_create_user({
            'username': 'user2',
            'email': 'user2@example.com'
        })
        
        handler.user_service.deactivate_user(user_id)
        
        response = handler.handle_list_users(active_only=False)
        
        assert response['success'] is True
        assert response['count'] == 2
    
    def test_handle_list_users_active_only_no_active_users(self):
        """Test listing active users when none are active."""
        handler = APIHandler()
        user_id1 = handler.handle_create_user({
            'username': 'user1',
            'email': 'user1@example.com'
        })['user_id']
        user_id2 = handler.handle_create_user({
            'username': 'user2',
            'email': 'user2@example.com'
        })['user_id']
        
        handler.user_service.deactivate_user(user_id1)
        handler.user_service.deactivate_user(user_id2)
        
        response = handler.handle_list_users(active_only=True)
        
        assert response['success'] is True
        assert response['count'] == 0
        assert response['users'] == []


class TestAPIHandlerIntegration:
    """Integration tests for API handler workflows."""
    
    def test_full_user_lifecycle(self):
        """Test complete user lifecycle: create, get, update, delete."""
        handler = APIHandler()
        
        # Create user
        create_response = handler.handle_create_user({
            'username': 'john_doe',
            'email': 'john@example.com',
            'age': 25
        })
        assert create_response['success'] is True
        user_id = create_response['user_id']
        
        # Get user
        get_response = handler.handle_get_user(user_id)
        assert get_response['success'] is True
        assert get_response['user']['username'] == 'john_doe'
        
        # Update email
        update_response = handler.handle_update_user_email(user_id, 'newemail@example.com')
        assert update_response['success'] is True
        
        # Verify update
        get_response2 = handler.handle_get_user(user_id)
        assert get_response2['user']['email'] == 'newemail@example.com'
        
        # Delete user
        delete_response = handler.handle_delete_user(user_id)
        assert delete_response['success'] is True
        
        # Verify deletion
        get_response3 = handler.handle_get_user(user_id)
        assert get_response3['success'] is False
    
    def test_multiple_users_management(self):
        """Test managing multiple users."""
        handler = APIHandler()
        
        # Create multiple users
        user_ids = []
        for i in range(1, 4):
            response = handler.handle_create_user({
                'username': f'user{i}',
                'email': f'user{i}@example.com'
            })
            user_ids.append(response['user_id'])
        
        # List all users
        list_response = handler.handle_list_users()
        assert list_response['count'] == 3
        
        # Deactivate one user
        handler.user_service.deactivate_user(user_ids[1])
        
        # List active users only
        active_response = handler.handle_list_users(active_only=True)
        assert active_response['count'] == 2
        
        # Delete one user
        handler.handle_delete_user(user_ids[0])
        
        # List all users
        final_response = handler.handle_list_users()
        assert final_response['count'] == 2
