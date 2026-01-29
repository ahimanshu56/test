"""
Validation Module
Provides input validation and data sanitization functions.
"""

import re
from typing import Any, List, Dict, Optional
from datetime import datetime


class Validator:
    """Validate and sanitize input data."""
    
    @staticmethod
    def validate_string(value: Any, min_length: int = 0, max_length: Optional[int] = None, 
                       pattern: Optional[str] = None) -> bool:
        """
        Validate a string value.
        
        Args:
            value: Value to validate
            min_length: Minimum string length
            max_length: Maximum string length (None for no limit)
            pattern: Regex pattern to match
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(value, str):
            return False
        
        if len(value) < min_length:
            return False
        
        if max_length is not None and len(value) > max_length:
            return False
        
        if pattern is not None:
            if not re.match(pattern, value):
                return False
        
        return True
    
    @staticmethod
    def validate_number(value: Any, min_val: Optional[float] = None, 
                       max_val: Optional[float] = None, allow_float: bool = True) -> bool:
        """
        Validate a numeric value.
        
        Args:
            value: Value to validate
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            allow_float: Whether to allow float values
            
        Returns:
            True if valid, False otherwise
        """
        if not allow_float and not isinstance(value, int):
            return False
        
        if not isinstance(value, (int, float)):
            return False
        
        if min_val is not None and value < min_val:
            return False
        
        if max_val is not None and value > max_val:
            return False
        
        return True
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email address format."""
        if not isinstance(email, str):
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_url(url: str, require_https: bool = False) -> bool:
        """
        Validate URL format.
        
        Args:
            url: URL to validate
            require_https: Whether to require HTTPS protocol
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(url, str):
            return False
        
        if require_https:
            pattern = r'^https://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        else:
            pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        
        return bool(re.match(pattern, url))
    
    @staticmethod
    def validate_date(date_string: str, date_format: str = '%Y-%m-%d') -> bool:
        """
        Validate date string format.
        
        Args:
            date_string: Date string to validate
            date_format: Expected date format
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(date_string, str):
            return False
        
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_list(value: Any, item_type: type = None, min_items: int = 0, 
                     max_items: Optional[int] = None) -> bool:
        """
        Validate a list value.
        
        Args:
            value: Value to validate
            item_type: Required type for list items
            min_items: Minimum number of items
            max_items: Maximum number of items
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(value, list):
            return False
        
        if len(value) < min_items:
            return False
        
        if max_items is not None and len(value) > max_items:
            return False
        
        if item_type is not None:
            for item in value:
                if not isinstance(item, item_type):
                    return False
        
        return True
    
    @staticmethod
    def validate_dict(value: Any, required_keys: Optional[List[str]] = None) -> bool:
        """
        Validate a dictionary value.
        
        Args:
            value: Value to validate
            required_keys: List of required keys
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(value, dict):
            return False
        
        if required_keys:
            for key in required_keys:
                if key not in value:
                    return False
        
        return True
    
    @staticmethod
    def sanitize_string(value: str, remove_html: bool = True, 
                       remove_special: bool = False) -> str:
        """
        Sanitize a string value.
        
        Args:
            value: String to sanitize
            remove_html: Whether to remove HTML tags
            remove_special: Whether to remove special characters
            
        Returns:
            Sanitized string
        """
        if not isinstance(value, str):
            return ""
        
        result = value
        
        if remove_html:
            # Remove HTML tags
            result = re.sub(r'<[^>]+>', '', result)
        
        if remove_special:
            # Keep only alphanumeric and spaces
            result = re.sub(r'[^a-zA-Z0-9\s]', '', result)
        
        return result.strip()
    
    @staticmethod
    def validate_phone(phone: str, country_code: str = 'US') -> bool:
        """
        Validate phone number format.
        
        Args:
            phone: Phone number to validate
            country_code: Country code for validation rules
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(phone, str):
            return False
        
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
        
        if country_code == 'US':
            # US phone: 10 digits, optional +1 prefix
            pattern = r'^(\+?1)?[2-9]\d{9}$'
            return bool(re.match(pattern, cleaned))
        
        # Generic: 7-15 digits
        pattern = r'^\+?[1-9]\d{6,14}$'
        return bool(re.match(pattern, cleaned))
    
    @staticmethod
    def validate_credit_card(card_number: str) -> bool:
        """
        Validate credit card number using Luhn algorithm.
        
        Args:
            card_number: Credit card number to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(card_number, str):
            return False
        
        # Remove spaces and dashes
        cleaned = re.sub(r'[\s\-]', '', card_number)
        
        # Check if all digits
        if not cleaned.isdigit():
            return False
        
        # Check length (13-19 digits)
        if len(cleaned) < 13 or len(cleaned) > 19:
            return False
        
        # Luhn algorithm
        digits = [int(d) for d in cleaned]
        checksum = 0
        
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled
        
        checksum = sum(digits)
        return checksum % 10 == 0
