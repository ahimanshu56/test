"""User service for managing users."""

from src.models.user import User


class UserService:
    """Service for managing user operations."""
    
    def __init__(self):
        """Initialize the user service."""
        self.users = {}
        self._next_id = 1
    
    def create_user(self, username, email, age=None):
        """Create a new user.
        
        Args:
            username: Username
            email: Email address
            age: Optional age
            
        Returns:
            Tuple of (user_id, User object)
            
        Raises:
            ValueError: If username already exists or validation fails
        """
        # Check if username already exists
        for user in self.users.values():
            if user.username == username:
                raise ValueError(f"Username '{username}' already exists")
        
        # Create user (validation happens in User.__init__)
        user = User(username, email, age)
        user_id = self._next_id
        self.users[user_id] = user
        self._next_id += 1
        
        return user_id, user
    
    def get_user(self, user_id):
        """Get a user by ID.
        
        Args:
            user_id: User ID
            
        Returns:
            User object or None if not found
        """
        return self.users.get(user_id)
    
    def get_user_by_username(self, username):
        """Get a user by username.
        
        Args:
            username: Username to search for
            
        Returns:
            Tuple of (user_id, User) or (None, None) if not found
        """
        for user_id, user in self.users.items():
            if user.username == username:
                return user_id, user
        return None, None
    
    def update_user_email(self, user_id, new_email):
        """Update a user's email.
        
        Args:
            user_id: User ID
            new_email: New email address
            
        Returns:
            True if updated, False if user not found
            
        Raises:
            ValueError: If email format is invalid
        """
        user = self.users.get(user_id)
        if not user:
            return False
        
        user.update_email(new_email)
        return True
    
    def delete_user(self, user_id):
        """Delete a user.
        
        Args:
            user_id: User ID
            
        Returns:
            True if deleted, False if user not found
        """
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def deactivate_user(self, user_id):
        """Deactivate a user account.
        
        Args:
            user_id: User ID
            
        Returns:
            True if deactivated, False if user not found
        """
        user = self.users.get(user_id)
        if not user:
            return False
        
        user.deactivate()
        return True
    
    def activate_user(self, user_id):
        """Activate a user account.
        
        Args:
            user_id: User ID
            
        Returns:
            True if activated, False if user not found
        """
        user = self.users.get(user_id)
        if not user:
            return False
        
        user.activate()
        return True
    
    def list_active_users(self):
        """Get all active users.
        
        Returns:
            List of tuples (user_id, User) for active users
        """
        return [(uid, user) for uid, user in self.users.items() if user.is_active]
    
    def count_users(self):
        """Count total number of users.
        
        Returns:
            Total number of users
        """
        return len(self.users)
    
    def count_active_users(self):
        """Count number of active users.
        
        Returns:
            Number of active users
        """
        return sum(1 for user in self.users.values() if user.is_active)
