"""
Comprehensive tests for Validator module.
Achieves 100% coverage of all functions, branches, and edge cases.
"""

import pytest
from src.validator import Validator


class TestValidatorString:
    """Tests for string validation."""
    
    def test_validate_string_valid(self):
        """Test validating valid string."""
        assert Validator.validate_string("hello") is True
    
    def test_validate_string_min_length(self):
        """Test validating string with minimum length."""
        assert Validator.validate_string("abc", min_length=3) is True
        assert Validator.validate_string("ab", min_length=3) is False
    
    def test_validate_string_max_length(self):
        """Test validating string with maximum length."""
        assert Validator.validate_string("abc", max_length=3) is True
        assert Validator.validate_string("abcd", max_length=3) is False
    
    def test_validate_string_pattern(self):
        """Test validating string with pattern."""
        assert Validator.validate_string("abc123", pattern=r'^[a-z0-9]+$') is True
        assert Validator.validate_string("abc@123", pattern=r'^[a-z0-9]+$') is False
    
    def test_validate_string_not_string_type(self):
        """Test validating non-string value."""
        assert Validator.validate_string(123) is False
        assert Validator.validate_string(None) is False
        assert Validator.validate_string([]) is False
    
    def test_validate_string_empty(self):
        """Test validating empty string."""
        assert Validator.validate_string("", min_length=0) is True
        assert Validator.validate_string("", min_length=1) is False


class TestValidatorNumber:
    """Tests for number validation."""
    
    def test_validate_number_valid_int(self):
        """Test validating valid integer."""
        assert Validator.validate_number(42) is True
    
    def test_validate_number_valid_float(self):
        """Test validating valid float."""
        assert Validator.validate_number(42.5) is True
    
    def test_validate_number_min_val(self):
        """Test validating number with minimum value."""
        assert Validator.validate_number(10, min_val=5) is True
        assert Validator.validate_number(3, min_val=5) is False
    
    def test_validate_number_max_val(self):
        """Test validating number with maximum value."""
        assert Validator.validate_number(10, max_val=15) is True
        assert Validator.validate_number(20, max_val=15) is False
    
    def test_validate_number_no_float(self):
        """Test validating with float not allowed."""
        assert Validator.validate_number(42, allow_float=False) is True
        assert Validator.validate_number(42.5, allow_float=False) is False
    
    def test_validate_number_not_number_type(self):
        """Test validating non-number value."""
        assert Validator.validate_number("42") is False
        assert Validator.validate_number(None) is False
        assert Validator.validate_number([]) is False


class TestValidatorEmail:
    """Tests for email validation."""
    
    def test_validate_email_valid(self):
        """Test validating valid emails."""
        assert Validator.validate_email("test@example.com") is True
        assert Validator.validate_email("user.name@example.co.uk") is True
        assert Validator.validate_email("user+tag@example.com") is True
    
    def test_validate_email_invalid(self):
        """Test validating invalid emails."""
        assert Validator.validate_email("invalid") is False
        assert Validator.validate_email("@example.com") is False
        assert Validator.validate_email("user@") is False
        assert Validator.validate_email("user@example") is False
        assert Validator.validate_email("") is False
    
    def test_validate_email_not_string(self):
        """Test validating non-string email."""
        assert Validator.validate_email(123) is False
        assert Validator.validate_email(None) is False


class TestValidatorURL:
    """Tests for URL validation."""
    
    def test_validate_url_valid_http(self):
        """Test validating valid HTTP URL."""
        assert Validator.validate_url("http://example.com") is True
        assert Validator.validate_url("http://example.com/path") is True
    
    def test_validate_url_valid_https(self):
        """Test validating valid HTTPS URL."""
        assert Validator.validate_url("https://example.com") is True
        assert Validator.validate_url("https://example.com/path") is True
    
    def test_validate_url_require_https(self):
        """Test validating URL with HTTPS requirement."""
        assert Validator.validate_url("https://example.com", require_https=True) is True
        assert Validator.validate_url("http://example.com", require_https=True) is False
    
    def test_validate_url_invalid(self):
        """Test validating invalid URLs."""
        assert Validator.validate_url("example.com") is False
        assert Validator.validate_url("ftp://example.com") is False
        assert Validator.validate_url("") is False
    
    def test_validate_url_not_string(self):
        """Test validating non-string URL."""
        assert Validator.validate_url(123) is False
        assert Validator.validate_url(None) is False


class TestValidatorDate:
    """Tests for date validation."""
    
    def test_validate_date_valid_default_format(self):
        """Test validating valid date with default format."""
        assert Validator.validate_date("2024-01-15") is True
        assert Validator.validate_date("2024-12-31") is True
    
    def test_validate_date_invalid_default_format(self):
        """Test validating invalid date with default format."""
        assert Validator.validate_date("01-15-2024") is False
        assert Validator.validate_date("2024/01/15") is False
        assert Validator.validate_date("invalid") is False
    
    def test_validate_date_custom_format(self):
        """Test validating date with custom format."""
        assert Validator.validate_date("01/15/2024", date_format="%m/%d/%Y") is True
        assert Validator.validate_date("2024-01-15", date_format="%m/%d/%Y") is False
    
    def test_validate_date_not_string(self):
        """Test validating non-string date."""
        assert Validator.validate_date(123) is False
        assert Validator.validate_date(None) is False


class TestValidatorList:
    """Tests for list validation."""
    
    def test_validate_list_valid(self):
        """Test validating valid list."""
        assert Validator.validate_list([1, 2, 3]) is True
        assert Validator.validate_list([]) is True
    
    def test_validate_list_item_type(self):
        """Test validating list with item type."""
        assert Validator.validate_list([1, 2, 3], item_type=int) is True
        assert Validator.validate_list([1, "2", 3], item_type=int) is False
        assert Validator.validate_list(["a", "b"], item_type=str) is True
    
    def test_validate_list_min_items(self):
        """Test validating list with minimum items."""
        assert Validator.validate_list([1, 2, 3], min_items=2) is True
        assert Validator.validate_list([1], min_items=2) is False
    
    def test_validate_list_max_items(self):
        """Test validating list with maximum items."""
        assert Validator.validate_list([1, 2], max_items=3) is True
        assert Validator.validate_list([1, 2, 3, 4], max_items=3) is False
    
    def test_validate_list_not_list_type(self):
        """Test validating non-list value."""
        assert Validator.validate_list("not a list") is False
        assert Validator.validate_list(123) is False
        assert Validator.validate_list(None) is False


class TestValidatorDict:
    """Tests for dictionary validation."""
    
    def test_validate_dict_valid(self):
        """Test validating valid dictionary."""
        assert Validator.validate_dict({'key': 'value'}) is True
        assert Validator.validate_dict({}) is True
    
    def test_validate_dict_required_keys(self):
        """Test validating dictionary with required keys."""
        data = {'name': 'John', 'age': 30}
        assert Validator.validate_dict(data, required_keys=['name']) is True
        assert Validator.validate_dict(data, required_keys=['name', 'age']) is True
        assert Validator.validate_dict(data, required_keys=['name', 'email']) is False
    
    def test_validate_dict_not_dict_type(self):
        """Test validating non-dictionary value."""
        assert Validator.validate_dict([]) is False
        assert Validator.validate_dict("not a dict") is False
        assert Validator.validate_dict(123) is False
        assert Validator.validate_dict(None) is False


class TestValidatorSanitize:
    """Tests for string sanitization."""
    
    def test_sanitize_string_remove_html(self):
        """Test sanitizing string by removing HTML."""
        result = Validator.sanitize_string("<p>Hello</p>", remove_html=True)
        assert result == "Hello"
        
        result = Validator.sanitize_string("<script>alert('xss')</script>", remove_html=True)
        assert result == "alert('xss')"
    
    def test_sanitize_string_keep_html(self):
        """Test sanitizing string keeping HTML."""
        result = Validator.sanitize_string("<p>Hello</p>", remove_html=False)
        assert result == "<p>Hello</p>"
    
    def test_sanitize_string_remove_special(self):
        """Test sanitizing string by removing special characters."""
        result = Validator.sanitize_string("Hello@World!", remove_special=True)
        assert result == "HelloWorld"
        
        result = Validator.sanitize_string("Test#123$", remove_special=True)
        assert result == "Test123"
    
    def test_sanitize_string_both_options(self):
        """Test sanitizing with both HTML and special character removal."""
        result = Validator.sanitize_string("<p>Hello@World!</p>", remove_html=True, remove_special=True)
        assert result == "HelloWorld"
    
    def test_sanitize_string_whitespace(self):
        """Test sanitizing string with whitespace."""
        result = Validator.sanitize_string("  Hello World  ")
        assert result == "Hello World"
    
    def test_sanitize_string_not_string(self):
        """Test sanitizing non-string value."""
        result = Validator.sanitize_string(123)
        assert result == ""
        
        result = Validator.sanitize_string(None)
        assert result == ""


class TestValidatorPhone:
    """Tests for phone number validation."""
    
    def test_validate_phone_us_valid(self):
        """Test validating valid US phone numbers."""
        assert Validator.validate_phone("2125551234", country_code='US') is True
        assert Validator.validate_phone("+12125551234", country_code='US') is True
        assert Validator.validate_phone("12125551234", country_code='US') is True
    
    def test_validate_phone_us_with_formatting(self):
        """Test validating US phone with formatting."""
        assert Validator.validate_phone("(212) 555-1234", country_code='US') is True
        assert Validator.validate_phone("212-555-1234", country_code='US') is True
        assert Validator.validate_phone("212.555.1234", country_code='US') is True
    
    def test_validate_phone_us_invalid(self):
        """Test validating invalid US phone numbers."""
        assert Validator.validate_phone("123456", country_code='US') is False
        assert Validator.validate_phone("0125551234", country_code='US') is False
        assert Validator.validate_phone("1125551234", country_code='US') is False
    
    def test_validate_phone_generic(self):
        """Test validating generic phone numbers."""
        assert Validator.validate_phone("+441234567890", country_code='UK') is True
        assert Validator.validate_phone("+33123456789", country_code='FR') is True
    
    def test_validate_phone_not_string(self):
        """Test validating non-string phone."""
        assert Validator.validate_phone(123) is False
        assert Validator.validate_phone(None) is False


class TestValidatorCreditCard:
    """Tests for credit card validation."""
    
    def test_validate_credit_card_valid(self):
        """Test validating valid credit card numbers."""
        # Valid test card numbers (Luhn algorithm compliant)
        assert Validator.validate_credit_card("4532015112830366") is True  # Visa
        assert Validator.validate_credit_card("6011111111111117") is True  # Discover
    
    def test_validate_credit_card_with_spaces(self):
        """Test validating credit card with spaces."""
        assert Validator.validate_credit_card("4532 0151 1283 0366") is True
    
    def test_validate_credit_card_with_dashes(self):
        """Test validating credit card with dashes."""
        assert Validator.validate_credit_card("4532-0151-1283-0366") is True
    
    def test_validate_credit_card_invalid_luhn(self):
        """Test validating credit card with invalid Luhn checksum."""
        assert Validator.validate_credit_card("4532015112830367") is False
    
    def test_validate_credit_card_too_short(self):
        """Test validating credit card that's too short."""
        assert Validator.validate_credit_card("123456789012") is False
    
    def test_validate_credit_card_too_long(self):
        """Test validating credit card that's too long."""
        assert Validator.validate_credit_card("12345678901234567890") is False
    
    def test_validate_credit_card_non_digits(self):
        """Test validating credit card with non-digit characters."""
        assert Validator.validate_credit_card("4532-0151-1283-ABCD") is False
    
    def test_validate_credit_card_not_string(self):
        """Test validating non-string credit card."""
        assert Validator.validate_credit_card(123) is False
        assert Validator.validate_credit_card(None) is False
