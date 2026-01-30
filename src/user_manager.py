"""User management module."""
import re
from typing import Dict, List, Optional


class User:
    """Represents a user in the system."""
    
    def __init__(self, username: str, email: str, age: int):
        """Initialize a user."""
        self.username = username
        self.email = email
        self.age = age
        self.is_active = True
    
    def __repr__(self):
        """String representation of user."""
        return f"User(username={self.username}, email={self.email}, age={self.age})"
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True


class UserManager:
    """Manages user accounts."""
    
    def __init__(self):
        """Initialize user manager."""
        self.users: Dict[str, User] = {}
    
    def validate_email(self, email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def validate_username(self, username: str) -> bool:
        """Validate username (alphanumeric, 3-20 chars)."""
        if not username or len(username) < 3 or len(username) > 20:
            return False
        return username.isalnum()
    
    def validate_age(self, age: int) -> bool:
        """Validate age (must be between 13 and 120)."""
        return isinstance(age, int) and 13 <= age <= 120
    
    def create_user(self, username: str, email: str, age: int) -> User:
        """Create a new user."""
        if not self.validate_username(username):
            raise ValueError("Invalid username. Must be alphanumeric and 3-20 characters.")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        
        if not self.validate_age(age):
            raise ValueError("Invalid age. Must be between 13 and 120.")
        
        if username in self.users:
            raise ValueError(f"User {username} already exists.")
        
        user = User(username, email, age)
        self.users[username] = user
        return user
    
    def get_user(self, username: str) -> Optional[User]:
        """Get a user by username."""
        return self.users.get(username)
    
    def delete_user(self, username: str) -> bool:
        """Delete a user by username."""
        if username in self.users:
            del self.users[username]
            return True
        return False
    
    def list_users(self) -> List[User]:
        """List all users."""
        return list(self.users.values())
    
    def list_active_users(self) -> List[User]:
        """List only active users."""
        return [user for user in self.users.values() if user.is_active]
    
    def count_users(self) -> int:
        """Count total users."""
        return len(self.users)
    
    def update_email(self, username: str, new_email: str) -> bool:
        """Update user's email."""
        if username not in self.users:
            return False
        
        if not self.validate_email(new_email):
            raise ValueError("Invalid email format.")
        
        self.users[username].email = new_email
        return True
