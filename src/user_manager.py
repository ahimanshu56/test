"""
User Management Module
Handles user authentication, validation, and CRUD operations.
"""

import hashlib
import re
from typing import Optional, Dict, List


class UserManager:
    """Manages user accounts and authentication."""
    
    def __init__(self):
        self.users: Dict[str, Dict] = {}
        self.sessions: Dict[str, str] = {}
    
    def create_user(self, username: str, email: str, password: str) -> Dict:
        """
        Create a new user account.
        
        Args:
            username: User's username (3-20 alphanumeric characters)
            email: User's email address
            password: User's password (min 8 characters)
            
        Returns:
            Dict containing user information
            
        Raises:
            ValueError: If validation fails
        """
        # Validate username
        if not username or len(username) < 3 or len(username) > 20:
            raise ValueError("Username must be 3-20 characters")
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError("Username must be alphanumeric")
        
        if username in self.users:
            raise ValueError("Username already exists")
        
        # Validate email
        if not self._is_valid_email(email):
            raise ValueError("Invalid email address")
        
        # Validate password
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        # Create user
        user_data = {
            'username': username,
            'email': email,
            'password_hash': self._hash_password(password),
            'active': True,
            'role': 'user'
        }
        
        self.users[username] = user_data
        return {
            'username': username,
            'email': email,
            'active': True,
            'role': 'user'
        }
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """
        Authenticate a user and create a session.
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            Session token if successful, None otherwise
        """
        if not username or not password:
            return None
        
        user = self.users.get(username)
        if not user:
            return None
        
        if not user.get('active', False):
            return None
        
        password_hash = self._hash_password(password)
        if user['password_hash'] != password_hash:
            return None
        
        # Create session
        session_token = self._generate_session_token(username)
        self.sessions[session_token] = username
        return session_token
    
    def get_user(self, username: str) -> Optional[Dict]:
        """Get user information by username."""
        user = self.users.get(username)
        if not user:
            return None
        
        return {
            'username': user['username'],
            'email': user['email'],
            'active': user['active'],
            'role': user['role']
        }
    
    def update_user(self, username: str, **kwargs) -> bool:
        """
        Update user information.
        
        Args:
            username: User's username
            **kwargs: Fields to update (email, active, role)
            
        Returns:
            True if successful, False otherwise
        """
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        if 'email' in kwargs:
            if not self._is_valid_email(kwargs['email']):
                raise ValueError("Invalid email address")
            user['email'] = kwargs['email']
        
        if 'active' in kwargs:
            user['active'] = bool(kwargs['active'])
        
        if 'role' in kwargs:
            if kwargs['role'] not in ['user', 'admin', 'moderator']:
                raise ValueError("Invalid role")
            user['role'] = kwargs['role']
        
        return True
    
    def delete_user(self, username: str) -> bool:
        """Delete a user account."""
        if username not in self.users:
            return False
        
        del self.users[username]
        
        # Remove all sessions for this user
        sessions_to_remove = [
            token for token, user in self.sessions.items()
            if user == username
        ]
        for token in sessions_to_remove:
            del self.sessions[token]
        
        return True
    
    def list_users(self, active_only: bool = False) -> List[Dict]:
        """List all users."""
        users = []
        for user in self.users.values():
            if active_only and not user.get('active', False):
                continue
            
            users.append({
                'username': user['username'],
                'email': user['email'],
                'active': user['active'],
                'role': user['role']
            })
        
        return users
    
    def validate_session(self, session_token: str) -> Optional[str]:
        """Validate a session token and return username."""
        return self.sessions.get(session_token)
    
    def logout(self, session_token: str) -> bool:
        """Logout a user by removing their session."""
        if session_token in self.sessions:
            del self.sessions[session_token]
            return True
        return False
    
    def _is_valid_email(self, email: str) -> bool:
        """Validate email format."""
        if not email:
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def _hash_password(self, password: str) -> str:
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _generate_session_token(self, username: str) -> str:
        """Generate a session token."""
        import time
        data = f"{username}:{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()
