"""
Basic tests for utils module (intentionally incomplete for initial coverage).
"""
import pytest
from datetime import datetime
from src.utils import sanitize_string, truncate_string, parse_date


def test_sanitize_string():
    """Test sanitizing a string."""
    result = sanitize_string("  hello   world  ")
    assert result == "hello world"


def test_truncate_string():
    """Test truncating a string."""
    result = truncate_string("hello world", 8)
    assert result == "hello..."
