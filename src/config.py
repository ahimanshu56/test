"""
Configuration Module
Handles application configuration and environment settings.
"""

import os
from typing import Any, Dict, Optional


class Config:
    """Application configuration manager."""
    
    def __init__(self, env: str = 'development'):
        """
        Initialize configuration.
        
        Args:
            env: Environment name ('development', 'production', 'testing')
        """
        self.env = env
        self.settings: Dict[str, Any] = {}
        self._load_defaults()
    
    def _load_defaults(self) -> None:
        """Load default configuration values."""
        self.settings = {
            'app_name': 'TestApp',
            'version': '1.0.0',
            'debug': self.env == 'development',
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'testdb'
            },
            'api': {
                'timeout': 30,
                'max_retries': 3,
                'base_url': 'http://localhost:8000'
            },
            'security': {
                'secret_key': 'default-secret-key',
                'token_expiry': 3600
            }
        }
        
        if self.env == 'production':
            self.settings['debug'] = False
            self.settings['api']['base_url'] = 'https://api.production.com'
        elif self.env == 'testing':
            self.settings['database']['name'] = 'testdb_test'
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'database.host')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split('.')
        settings = self.settings
        
        for k in keys[:-1]:
            if k not in settings:
                settings[k] = {}
            settings = settings[k]
        
        settings[keys[-1]] = value
    
    def load_from_env(self, prefix: str = 'APP_') -> None:
        """
        Load configuration from environment variables.
        
        Args:
            prefix: Prefix for environment variables
        """
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower().replace('_', '.')
                self.set(config_key, value)
    
    def get_database_url(self) -> str:
        """Get database connection URL."""
        db_config = self.settings.get('database', {})
        host = db_config.get('host', 'localhost')
        port = db_config.get('port', 5432)
        name = db_config.get('name', 'testdb')
        
        return f"postgresql://{host}:{port}/{name}"
    
    def is_debug(self) -> bool:
        """Check if debug mode is enabled."""
        return bool(self.settings.get('debug', False))
    
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.env == 'production'
    
    def validate(self) -> bool:
        """
        Validate configuration.
        
        Returns:
            True if configuration is valid
            
        Raises:
            ValueError: If configuration is invalid
        """
        if not self.settings.get('app_name'):
            raise ValueError("app_name is required")
        
        if self.env == 'production':
            secret_key = self.get('security.secret_key')
            if not secret_key or secret_key == 'default-secret-key':
                raise ValueError("Production requires a custom secret_key")
        
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Export configuration as dictionary."""
        return self.settings.copy()
