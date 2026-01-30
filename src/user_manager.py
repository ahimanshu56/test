"""
User management module with authentication and validation.
"""
import re
from typing import Optional, Dict, List


class UserManager:
    """Manages user accounts and authentication."""
    
    def __init__(self):
        self.users: Dict[str, Dict] = {}
        self.active_sessions: Dict[str, str] = {}
    
    def validate_email(self, email: str) -> bool:
        """Validate email format."""
        if not email or not isinstance(email, str):
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def validate_password(self, password: str) -> tuple[bool, Optional[str]]:
        """
        Validate password strength.
        Returns (is_valid, error_message).
        """
        if not password or not isinstance(password, str):
            return False, "Password cannot be empty"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter"
        
        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter"
        
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one digit"
        
        return True, None
    
    def create_user(self, username: str, email: str, password: str) -> Dict:
        """Create a new user account."""
        if not username or not isinstance(username, str):
            raise ValueError("Username is required")
        
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email format")
        
        is_valid, error = self.validate_password(password)
        if not is_valid:
            raise ValueError(error)
        
        user = {
            "username": username,
            "email": email,
            "password": password,  # In real app, this would be hashed
            "active": True,
            "login_attempts": 0
        }
        
        self.users[username] = user
        return {"username": username, "email": email, "active": True}
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return session token."""
        if not username or username not in self.users:
            return None
        
        user = self.users[username]
        
        if not user.get("active", False):
            return None
        
        if user.get("login_attempts", 0) >= 3:
            user["active"] = False
            return None
        
        if user["password"] != password:
            user["login_attempts"] = user.get("login_attempts", 0) + 1
            return None
        
        # Reset login attempts on successful login
        user["login_attempts"] = 0
        
        # Generate simple session token
        session_token = f"session_{username}_{len(self.active_sessions)}"
        self.active_sessions[session_token] = username
        
        return session_token
    
    def logout(self, session_token: str) -> bool:
        """Logout user by removing session."""
        if session_token in self.active_sessions:
            del self.active_sessions[session_token]
            return True
        return False
    
    def get_user(self, username: str) -> Optional[Dict]:
        """Get user information."""
        if username not in self.users:
            return None
        
        user = self.users[username].copy()
        user.pop("password", None)  # Don't return password
        return user
    
    def list_users(self, active_only: bool = False) -> List[Dict]:
        """List all users."""
        users = []
        for username, user in self.users.items():
            if active_only and not user.get("active", False):
                continue
            
            user_info = user.copy()
            user_info.pop("password", None)
            users.append(user_info)
        
        return users
    
    def deactivate_user(self, username: str) -> bool:
        """Deactivate a user account."""
        if username not in self.users:
            return False
        
        self.users[username]["active"] = False
        
        # Remove any active sessions
        sessions_to_remove = [
            token for token, user in self.active_sessions.items()
            if user == username
        ]
        for token in sessions_to_remove:
            del self.active_sessions[token]
        
        return True
