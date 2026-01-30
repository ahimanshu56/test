"""
API client module for HTTP requests and error handling.
"""
from typing import Optional, Dict, Any
from urllib.parse import urljoin, urlparse


class APIError(Exception):
    """Custom exception for API errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class APIClient:
    """HTTP API client with error handling."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        if not base_url:
            raise ValueError("base_url is required")
        
        if not self._is_valid_url(base_url):
            raise ValueError("Invalid base_url format")
        
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = 30
        self.retry_count = 3
    
    def _is_valid_url(self, url: str) -> bool:
        """Validate URL format."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False
    
    def _build_url(self, endpoint: str) -> str:
        """Build full URL from endpoint."""
        if not endpoint:
            return self.base_url
        
        endpoint = endpoint.lstrip('/')
        return urljoin(self.base_url + '/', endpoint)
    
    def _build_headers(self, custom_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Build request headers."""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "APIClient/1.0"
        }
        
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        if custom_headers:
            headers.update(custom_headers)
        
        return headers
    
    def _handle_response(self, status_code: int, response_data: Any) -> Any:
        """Handle API response and errors."""
        if 200 <= status_code < 300:
            return response_data
        
        if status_code == 400:
            raise APIError("Bad Request", status_code)
        elif status_code == 401:
            raise APIError("Unauthorized", status_code)
        elif status_code == 403:
            raise APIError("Forbidden", status_code)
        elif status_code == 404:
            raise APIError("Not Found", status_code)
        elif status_code == 429:
            raise APIError("Rate Limit Exceeded", status_code)
        elif 500 <= status_code < 600:
            raise APIError("Server Error", status_code)
        else:
            raise APIError(f"HTTP Error {status_code}", status_code)
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Simulate GET request."""
        url = self._build_url(endpoint)
        headers = self._build_headers()
        
        # Simulated response for testing
        return {
            "method": "GET",
            "url": url,
            "headers": headers,
            "params": params or {}
        }
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Simulate POST request."""
        url = self._build_url(endpoint)
        headers = self._build_headers()
        
        if data is None:
            data = {}
        
        # Simulated response for testing
        return {
            "method": "POST",
            "url": url,
            "headers": headers,
            "data": data
        }
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Simulate PUT request."""
        url = self._build_url(endpoint)
        headers = self._build_headers()
        
        return {
            "method": "PUT",
            "url": url,
            "headers": headers,
            "data": data or {}
        }
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Simulate DELETE request."""
        url = self._build_url(endpoint)
        headers = self._build_headers()
        
        return {
            "method": "DELETE",
            "url": url,
            "headers": headers
        }
    
    def set_timeout(self, timeout: int) -> None:
        """Set request timeout."""
        if timeout <= 0:
            raise ValueError("Timeout must be positive")
        self.timeout = timeout
    
    def set_retry_count(self, count: int) -> None:
        """Set retry count for failed requests."""
        if count < 0:
            raise ValueError("Retry count cannot be negative")
        self.retry_count = count
