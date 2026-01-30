"""API request handlers."""

import json
from src.services.user_service import UserService


class APIHandler:
    """Handler for API requests."""
    
    def __init__(self):
        """Initialize the API handler."""
        self.user_service = UserService()
    
    def handle_create_user(self, request_data):
        """Handle create user request.
        
        Args:
            request_data: Dictionary with 'username', 'email', and optional 'age'
            
        Returns:
            Dictionary with 'success', 'user_id', and 'message' or 'error'
        """
        try:
            if not isinstance(request_data, dict):
                return {
                    'success': False,
                    'error': 'Invalid request format'
                }
            
            username = request_data.get('username')
            email = request_data.get('email')
            age = request_data.get('age')
            
            if not username or not email:
                return {
                    'success': False,
                    'error': 'Username and email are required'
                }
            
            user_id, user = self.user_service.create_user(username, email, age)
            
            return {
                'success': True,
                'user_id': user_id,
                'message': 'User created successfully',
                'user': user.to_dict()
            }
        
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Internal server error: {str(e)}'
            }
    
    def handle_get_user(self, user_id):
        """Handle get user request.
        
        Args:
            user_id: User ID
            
        Returns:
            Dictionary with 'success' and 'user' or 'error'
        """
        try:
            if not isinstance(user_id, int):
                return {
                    'success': False,
                    'error': 'User ID must be an integer'
                }
            
            user = self.user_service.get_user(user_id)
            
            if not user:
                return {
                    'success': False,
                    'error': 'User not found'
                }
            
            return {
                'success': True,
                'user': user.to_dict()
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f'Internal server error: {str(e)}'
            }
    
    def handle_update_user_email(self, user_id, new_email):
        """Handle update user email request.
        
        Args:
            user_id: User ID
            new_email: New email address
            
        Returns:
            Dictionary with 'success' and 'message' or 'error'
        """
        try:
            if not isinstance(user_id, int):
                return {
                    'success': False,
                    'error': 'User ID must be an integer'
                }
            
            if not new_email:
                return {
                    'success': False,
                    'error': 'New email is required'
                }
            
            updated = self.user_service.update_user_email(user_id, new_email)
            
            if not updated:
                return {
                    'success': False,
                    'error': 'User not found'
                }
            
            return {
                'success': True,
                'message': 'Email updated successfully'
            }
        
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Internal server error: {str(e)}'
            }
    
    def handle_delete_user(self, user_id):
        """Handle delete user request.
        
        Args:
            user_id: User ID
            
        Returns:
            Dictionary with 'success' and 'message' or 'error'
        """
        try:
            if not isinstance(user_id, int):
                return {
                    'success': False,
                    'error': 'User ID must be an integer'
                }
            
            deleted = self.user_service.delete_user(user_id)
            
            if not deleted:
                return {
                    'success': False,
                    'error': 'User not found'
                }
            
            return {
                'success': True,
                'message': 'User deleted successfully'
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f'Internal server error: {str(e)}'
            }
    
    def handle_list_users(self, active_only=False):
        """Handle list users request.
        
        Args:
            active_only: If True, return only active users
            
        Returns:
            Dictionary with 'success' and 'users' or 'error'
        """
        try:
            if active_only:
                users = self.user_service.list_active_users()
            else:
                users = list(self.user_service.users.items())
            
            return {
                'success': True,
                'users': [
                    {
                        'user_id': uid,
                        **user.to_dict()
                    }
                    for uid, user in users
                ],
                'count': len(users)
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f'Internal server error: {str(e)}'
            }
