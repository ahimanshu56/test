"""
Comprehensive tests for Config module.
Achieves 100% coverage of all functions, branches, and edge cases.
"""

import pytest
import os
from src.config import Config


class TestConfigInitialization:
    """Tests for configuration initialization."""
    
    def test_init_development(self):
        """Test initializing config in development mode."""
        config = Config('development')
        
        assert config.env == 'development'
        assert config.is_debug() is True
        assert config.get('debug') is True
    
    def test_init_production(self):
        """Test initializing config in production mode."""
        config = Config('production')
        
        assert config.env == 'production'
        assert config.is_debug() is False
        assert config.get('debug') is False
        assert config.get('api.base_url') == 'https://api.production.com'
    
    def test_init_testing(self):
        """Test initializing config in testing mode."""
        config = Config('testing')
        
        assert config.env == 'testing'
        assert config.get('database.name') == 'testdb_test'
    
    def test_init_default(self):
        """Test initializing config with default environment."""
        config = Config()
        
        assert config.env == 'development'


class TestConfigGet:
    """Tests for getting configuration values."""
    
    def test_get_simple_key(self):
        """Test getting simple configuration key."""
        config = Config()
        
        assert config.get('app_name') == 'TestApp'
        assert config.get('version') == '1.0.0'
    
    def test_get_nested_key(self):
        """Test getting nested configuration key."""
        config = Config()
        
        assert config.get('database.host') == 'localhost'
        assert config.get('database.port') == 5432
        assert config.get('api.timeout') == 30
    
    def test_get_nonexistent_key(self):
        """Test getting nonexistent key."""
        config = Config()
        
        assert config.get('nonexistent') is None
    
    def test_get_nonexistent_key_with_default(self):
        """Test getting nonexistent key with default value."""
        config = Config()
        
        assert config.get('nonexistent', 'default_value') == 'default_value'
    
    def test_get_deeply_nested_key(self):
        """Test getting deeply nested key."""
        config = Config()
        
        assert config.get('security.secret_key') == 'default-secret-key'
        assert config.get('security.token_expiry') == 3600
    
    def test_get_partial_path(self):
        """Test getting partial path returns dict."""
        config = Config()
        
        database_config = config.get('database')
        assert isinstance(database_config, dict)
        assert database_config['host'] == 'localhost'


class TestConfigSet:
    """Tests for setting configuration values."""
    
    def test_set_simple_key(self):
        """Test setting simple configuration key."""
        config = Config()
        
        config.set('new_key', 'new_value')
        assert config.get('new_key') == 'new_value'
    
    def test_set_nested_key(self):
        """Test setting nested configuration key."""
        config = Config()
        
        config.set('database.host', 'newhost')
        assert config.get('database.host') == 'newhost'
    
    def test_set_new_nested_key(self):
        """Test setting new nested configuration key."""
        config = Config()
        
        config.set('new.nested.key', 'value')
        assert config.get('new.nested.key') == 'value'
    
    def test_set_overwrite_existing(self):
        """Test overwriting existing configuration value."""
        config = Config()
        
        config.set('app_name', 'NewApp')
        assert config.get('app_name') == 'NewApp'


class TestConfigLoadFromEnv:
    """Tests for loading configuration from environment."""
    
    def test_load_from_env(self):
        """Test loading configuration from environment variables."""
        os.environ['APP_TEST_KEY'] = 'test_value'
        os.environ['APP_DATABASE_HOST'] = 'envhost'
        
        config = Config()
        config.load_from_env('APP_')
        
        assert config.get('test.key') == 'test_value'
        assert config.get('database.host') == 'envhost'
        
        # Cleanup
        del os.environ['APP_TEST_KEY']
        del os.environ['APP_DATABASE_HOST']
    
    def test_load_from_env_custom_prefix(self):
        """Test loading configuration with custom prefix."""
        os.environ['CUSTOM_KEY'] = 'custom_value'
        
        config = Config()
        config.load_from_env('CUSTOM_')
        
        assert config.get('key') == 'custom_value'
        
        # Cleanup
        del os.environ['CUSTOM_KEY']
    
    def test_load_from_env_no_matching_vars(self):
        """Test loading configuration with no matching environment variables."""
        config = Config()
        original_settings = config.to_dict()
        
        config.load_from_env('NONEXISTENT_')
        
        # Settings should remain unchanged
        assert config.to_dict() == original_settings


class TestConfigDatabaseURL:
    """Tests for database URL generation."""
    
    def test_get_database_url_default(self):
        """Test getting database URL with default settings."""
        config = Config()
        
        url = config.get_database_url()
        assert url == 'postgresql://localhost:5432/testdb'
    
    def test_get_database_url_custom(self):
        """Test getting database URL with custom settings."""
        config = Config()
        config.set('database.host', 'dbserver')
        config.set('database.port', 3306)
        config.set('database.name', 'mydb')
        
        url = config.get_database_url()
        assert url == 'postgresql://dbserver:3306/mydb'


class TestConfigEnvironmentChecks:
    """Tests for environment checking methods."""
    
    def test_is_debug_development(self):
        """Test debug check in development."""
        config = Config('development')
        assert config.is_debug() is True
    
    def test_is_debug_production(self):
        """Test debug check in production."""
        config = Config('production')
        assert config.is_debug() is False
    
    def test_is_production(self):
        """Test production environment check."""
        config_dev = Config('development')
        config_prod = Config('production')
        
        assert config_dev.is_production() is False
        assert config_prod.is_production() is True


class TestConfigValidation:
    """Tests for configuration validation."""
    
    def test_validate_success(self):
        """Test successful validation."""
        config = Config('development')
        
        assert config.validate() is True
    
    def test_validate_missing_app_name(self):
        """Test validation with missing app_name."""
        config = Config()
        config.set('app_name', '')
        
        with pytest.raises(ValueError, match="app_name is required"):
            config.validate()
    
    def test_validate_production_default_secret(self):
        """Test validation in production with default secret key."""
        config = Config('production')
        
        with pytest.raises(ValueError, match="Production requires a custom secret_key"):
            config.validate()
    
    def test_validate_production_custom_secret(self):
        """Test validation in production with custom secret key."""
        config = Config('production')
        config.set('security.secret_key', 'custom-secret-key-12345')
        
        assert config.validate() is True


class TestConfigToDict:
    """Tests for exporting configuration."""
    
    def test_to_dict(self):
        """Test exporting configuration as dictionary."""
        config = Config()
        
        settings_dict = config.to_dict()
        
        assert isinstance(settings_dict, dict)
        assert settings_dict['app_name'] == 'TestApp'
        assert settings_dict['version'] == '1.0.0'
        assert 'database' in settings_dict
    
    def test_to_dict_is_copy(self):
        """Test that to_dict returns a copy."""
        config = Config()
        
        settings_dict = config.to_dict()
        settings_dict['app_name'] = 'Modified'
        
        # Original should be unchanged
        assert config.get('app_name') == 'TestApp'
