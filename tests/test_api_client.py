"""
Basic tests for api_client module (intentionally incomplete for initial coverage).
"""
import pytest
from src.api_client import APIClient, APIError


def test_create_client():
    """Test creating API client."""
    client = APIClient("https://api.example.com")
    
    assert client.base_url == "https://api.example.com"
    assert client.timeout == 30


def test_get_request():
    """Test GET request."""
    client = APIClient("https://api.example.com", api_key="test_key")
    
    response = client.get("/users")
    
    assert response["method"] == "GET"
    assert "Authorization" in response["headers"]
