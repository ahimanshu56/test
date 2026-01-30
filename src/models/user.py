"""User model."""

import re
from datetime import datetime


class User:
    """User model with validation."""
    
    def __init__(self, username, email, age=None):
        """Initialize a user.
        
        Args:
            username: Username (3-20 alphanumeric characters)
            email: Valid email address
            age: Optional age (must be >= 0 if provided)
            
        Raises:
            ValueError: If validation fails
        """
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.age = self._validate_age(age) if age is not None else None
        self.created_at = datetime.now()
        self.is_active = True
    
    def _validate_username(self, username):
        """Validate username format."""
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        
        if not 3 <= len(username) <= 20:
            raise ValueError("Username must be 3-20 characters long")
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError("Username can only contain alphanumeric characters and underscores")
        
        return username
    
    def _validate_email(self, email):
        """Validate email format."""
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        
        return email.lower()
    
    def _validate_age(self, age):
        """Validate age."""
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if age > 150:
            raise ValueError("Age must be realistic (<=150)")
        
        return age
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True
    
    def update_email(self, new_email):
        """Update user email.
        
        Args:
            new_email: New email address
            
        Raises:
            ValueError: If email format is invalid
        """
        self.email = self._validate_email(new_email)
    
    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username and self.email == other.email
