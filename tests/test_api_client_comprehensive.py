"""
Comprehensive tests for api_client module to achieve high coverage.
"""
import pytest
from src.api_client import APIClient, APIError


class TestAPIClientInitialization:
    """Test API client initialization."""
    
    def test_create_client_with_base_url(self):
        """Test creating client with base URL."""
        client = APIClient("https://api.example.com")
        assert client.base_url == "https://api.example.com"
        assert client.api_key is None
        assert client.timeout == 30
        assert client.retry_count == 3
    
    def test_create_client_with_api_key(self):
        """Test creating client with API key."""
        client = APIClient("https://api.example.com", api_key="test_key")
        assert client.api_key == "test_key"
    
    def test_create_client_strips_trailing_slash(self):
        """Test that trailing slash is removed from base URL."""
        client = APIClient("https://api.example.com/")
        assert client.base_url == "https://api.example.com"
    
    def test_create_client_empty_url(self):
        """Test creating client with empty URL."""
        with pytest.raises(ValueError, match="base_url is required"):
            APIClient("")
    
    def test_create_client_none_url(self):
        """Test creating client with None URL."""
        with pytest.raises(ValueError, match="base_url is required"):
            APIClient(None)
    
    def test_create_client_invalid_url(self):
        """Test creating client with invalid URL."""
        with pytest.raises(ValueError, match="Invalid base_url format"):
            APIClient("not-a-valid-url")
        
        with pytest.raises(ValueError, match="Invalid base_url format"):
            APIClient("ftp://example.com")


class TestAPIClientURLBuilding:
    """Test URL building methods."""
    
    def test_build_url_with_endpoint(self):
        """Test building URL with endpoint."""
        client = APIClient("https://api.example.com")
        url = client._build_url("/users")
        assert url == "https://api.example.com/users"
    
    def test_build_url_without_leading_slash(self):
        """Test building URL when endpoint has no leading slash."""
        client = APIClient("https://api.example.com")
        url = client._build_url("users")
        assert url == "https://api.example.com/users"
    
    def test_build_url_empty_endpoint(self):
        """Test building URL with empty endpoint."""
        client = APIClient("https://api.example.com")
        url = client._build_url("")
        assert url == "https://api.example.com"
    
    def test_is_valid_url_valid(self):
        """Test URL validation with valid URLs."""
        client = APIClient("https://api.example.com")
        assert client._is_valid_url("https://api.example.com") is True
        assert client._is_valid_url("http://localhost:8080") is True
    
    def test_is_valid_url_invalid(self):
        """Test URL validation with invalid URLs."""
        client = APIClient("https://api.example.com")
        assert client._is_valid_url("not-a-url") is False
        assert client._is_valid_url("") is False


class TestAPIClientHeaders:
    """Test header building."""
    
    def test_build_headers_default(self):
        """Test building default headers."""
        client = APIClient("https://api.example.com")
        headers = client._build_headers()
        
        assert headers["Content-Type"] == "application/json"
        assert headers["User-Agent"] == "APIClient/1.0"
        assert "Authorization" not in headers
    
    def test_build_headers_with_api_key(self):
        """Test building headers with API key."""
        client = APIClient("https://api.example.com", api_key="test_key")
        headers = client._build_headers()
        
        assert headers["Authorization"] == "Bearer test_key"
    
    def test_build_headers_with_custom(self):
        """Test building headers with custom headers."""
        client = APIClient("https://api.example.com")
        custom = {"X-Custom-Header": "value"}
        headers = client._build_headers(custom)
        
        assert headers["X-Custom-Header"] == "value"
        assert headers["Content-Type"] == "application/json"


class TestAPIClientResponseHandling:
    """Test response handling."""
    
    def test_handle_response_success(self):
        """Test handling successful responses."""
        client = APIClient("https://api.example.com")
        data = {"result": "success"}
        
        result = client._handle_response(200, data)
        assert result == data
        
        result = client._handle_response(201, data)
        assert result == data
    
    def test_handle_response_bad_request(self):
        """Test handling 400 Bad Request."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(400, {})
        
        assert exc_info.value.status_code == 400
        assert "Bad Request" in str(exc_info.value)
    
    def test_handle_response_unauthorized(self):
        """Test handling 401 Unauthorized."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(401, {})
        
        assert exc_info.value.status_code == 401
        assert "Unauthorized" in str(exc_info.value)
    
    def test_handle_response_forbidden(self):
        """Test handling 403 Forbidden."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(403, {})
        
        assert exc_info.value.status_code == 403
    
    def test_handle_response_not_found(self):
        """Test handling 404 Not Found."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(404, {})
        
        assert exc_info.value.status_code == 404
    
    def test_handle_response_rate_limit(self):
        """Test handling 429 Rate Limit."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(429, {})
        
        assert exc_info.value.status_code == 429
        assert "Rate Limit" in str(exc_info.value)
    
    def test_handle_response_server_error(self):
        """Test handling 500 Server Error."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(500, {})
        
        assert exc_info.value.status_code == 500
        assert "Server Error" in str(exc_info.value)
    
    def test_handle_response_other_error(self):
        """Test handling other error codes."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(APIError) as exc_info:
            client._handle_response(418, {})
        
        assert exc_info.value.status_code == 418


class TestAPIClientRequests:
    """Test HTTP request methods."""
    
    def test_get_request(self):
        """Test GET request."""
        client = APIClient("https://api.example.com", api_key="test_key")
        response = client.get("/users")
        
        assert response["method"] == "GET"
        assert response["url"] == "https://api.example.com/users"
        assert "Authorization" in response["headers"]
    
    def test_get_request_with_params(self):
        """Test GET request with parameters."""
        client = APIClient("https://api.example.com")
        params = {"page": 1, "limit": 10}
        response = client.get("/users", params=params)
        
        assert response["params"] == params
    
    def test_get_request_no_params(self):
        """Test GET request without parameters."""
        client = APIClient("https://api.example.com")
        response = client.get("/users")
        
        assert response["params"] == {}
    
    def test_post_request(self):
        """Test POST request."""
        client = APIClient("https://api.example.com")
        data = {"name": "John", "email": "john@example.com"}
        response = client.post("/users", data=data)
        
        assert response["method"] == "POST"
        assert response["data"] == data
    
    def test_post_request_no_data(self):
        """Test POST request without data."""
        client = APIClient("https://api.example.com")
        response = client.post("/users")
        
        assert response["data"] == {}
    
    def test_put_request(self):
        """Test PUT request."""
        client = APIClient("https://api.example.com")
        data = {"name": "John Updated"}
        response = client.put("/users/1", data=data)
        
        assert response["method"] == "PUT"
        assert response["data"] == data
    
    def test_put_request_no_data(self):
        """Test PUT request without data."""
        client = APIClient("https://api.example.com")
        response = client.put("/users/1")
        
        assert response["data"] == {}
    
    def test_delete_request(self):
        """Test DELETE request."""
        client = APIClient("https://api.example.com")
        response = client.delete("/users/1")
        
        assert response["method"] == "DELETE"
        assert response["url"] == "https://api.example.com/users/1"


class TestAPIClientConfiguration:
    """Test client configuration methods."""
    
    def test_set_timeout_valid(self):
        """Test setting valid timeout."""
        client = APIClient("https://api.example.com")
        client.set_timeout(60)
        assert client.timeout == 60
    
    def test_set_timeout_invalid(self):
        """Test setting invalid timeout."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(ValueError, match="Timeout must be positive"):
            client.set_timeout(0)
        
        with pytest.raises(ValueError, match="Timeout must be positive"):
            client.set_timeout(-10)
    
    def test_set_retry_count_valid(self):
        """Test setting valid retry count."""
        client = APIClient("https://api.example.com")
        client.set_retry_count(5)
        assert client.retry_count == 5
    
    def test_set_retry_count_zero(self):
        """Test setting retry count to zero."""
        client = APIClient("https://api.example.com")
        client.set_retry_count(0)
        assert client.retry_count == 0
    
    def test_set_retry_count_invalid(self):
        """Test setting invalid retry count."""
        client = APIClient("https://api.example.com")
        
        with pytest.raises(ValueError, match="cannot be negative"):
            client.set_retry_count(-1)


class TestAPIError:
    """Test APIError exception."""
    
    def test_api_error_with_status_code(self):
        """Test creating APIError with status code."""
        error = APIError("Test error", status_code=404)
        assert error.message == "Test error"
        assert error.status_code == 404
        assert str(error) == "Test error"
    
    def test_api_error_without_status_code(self):
        """Test creating APIError without status code."""
        error = APIError("Test error")
        assert error.message == "Test error"
        assert error.status_code is None
