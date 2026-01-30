"""
Comprehensive tests for utils module to achieve high coverage.
"""
import pytest
from datetime import datetime
from src.utils import (
    sanitize_string, truncate_string, parse_date, format_date,
    add_days, days_between, is_weekend, chunk_list,
    flatten_list, remove_duplicates
)


class TestSanitizeString:
    """Test sanitize_string function."""
    
    def test_sanitize_string_normal(self):
        """Test sanitizing normal string."""
        result = sanitize_string("  hello   world  ")
        assert result == "hello world"
    
    def test_sanitize_string_with_max_length(self):
        """Test sanitizing with max length."""
        result = sanitize_string("hello world", max_length=5)
        assert result == "hello"
    
    def test_sanitize_string_empty(self):
        """Test sanitizing empty string."""
        result = sanitize_string("")
        assert result == ""
    
    def test_sanitize_string_none(self):
        """Test sanitizing None."""
        result = sanitize_string(None)
        assert result == ""
    
    def test_sanitize_string_non_string(self):
        """Test sanitizing non-string."""
        result = sanitize_string(123)
        assert result == ""
    
    def test_sanitize_string_max_length_zero(self):
        """Test with max_length of zero."""
        result = sanitize_string("hello", max_length=0)
        assert result == ""
    
    def test_sanitize_string_max_length_none(self):
        """Test with max_length of None."""
        result = sanitize_string("hello world", max_length=None)
        assert result == "hello world"


class TestTruncateString:
    """Test truncate_string function."""
    
    def test_truncate_string_normal(self):
        """Test truncating normal string."""
        result = truncate_string("hello world", 8)
        assert result == "hello..."
    
    def test_truncate_string_no_truncation_needed(self):
        """Test when string is shorter than length."""
        result = truncate_string("hello", 10)
        assert result == "hello"
    
    def test_truncate_string_empty(self):
        """Test truncating empty string."""
        result = truncate_string("", 5)
        assert result == ""
    
    def test_truncate_string_zero_length(self):
        """Test with zero length."""
        result = truncate_string("hello", 0)
        assert result == ""
    
    def test_truncate_string_negative_length(self):
        """Test with negative length."""
        result = truncate_string("hello", -5)
        assert result == ""
    
    def test_truncate_string_custom_suffix(self):
        """Test with custom suffix."""
        result = truncate_string("hello world", 8, suffix=">>")
        assert result == "hello >>"
    
    def test_truncate_string_suffix_longer_than_length(self):
        """Test when suffix is longer than length."""
        result = truncate_string("hello world", 2, suffix="...")
        assert result == "he"


class TestParseDate:
    """Test parse_date function."""
    
    def test_parse_date_valid(self):
        """Test parsing valid date."""
        result = parse_date("2024-01-15")
        assert result is not None
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15
    
    def test_parse_date_custom_format(self):
        """Test parsing with custom format."""
        result = parse_date("15/01/2024", format_string="%d/%m/%Y")
        assert result is not None
        assert result.year == 2024
    
    def test_parse_date_invalid(self):
        """Test parsing invalid date."""
        result = parse_date("not-a-date")
        assert result is None
    
    def test_parse_date_empty(self):
        """Test parsing empty string."""
        result = parse_date("")
        assert result is None
    
    def test_parse_date_wrong_format(self):
        """Test parsing with wrong format."""
        result = parse_date("2024-01-15", format_string="%d/%m/%Y")
        assert result is None


class TestFormatDate:
    """Test format_date function."""
    
    def test_format_date_valid(self):
        """Test formatting valid date."""
        date = datetime(2024, 1, 15)
        result = format_date(date)
        assert result == "2024-01-15"
    
    def test_format_date_custom_format(self):
        """Test formatting with custom format."""
        date = datetime(2024, 1, 15)
        result = format_date(date, format_string="%d/%m/%Y")
        assert result == "15/01/2024"
    
    def test_format_date_none(self):
        """Test formatting None."""
        result = format_date(None)
        assert result == ""
    
    def test_format_date_non_datetime(self):
        """Test formatting non-datetime."""
        result = format_date("not-a-date")
        assert result == ""


class TestAddDays:
    """Test add_days function."""
    
    def test_add_days_positive(self):
        """Test adding positive days."""
        date = datetime(2024, 1, 15)
        result = add_days(date, 5)
        assert result.day == 20
    
    def test_add_days_negative(self):
        """Test adding negative days."""
        date = datetime(2024, 1, 15)
        result = add_days(date, -5)
        assert result.day == 10
    
    def test_add_days_zero(self):
        """Test adding zero days."""
        date = datetime(2024, 1, 15)
        result = add_days(date, 0)
        assert result == date
    
    def test_add_days_invalid_date(self):
        """Test with invalid date."""
        with pytest.raises(TypeError, match="must be a datetime object"):
            add_days("not-a-date", 5)


class TestDaysBetween:
    """Test days_between function."""
    
    def test_days_between_normal(self):
        """Test calculating days between two dates."""
        date1 = datetime(2024, 1, 15)
        date2 = datetime(2024, 1, 20)
        result = days_between(date1, date2)
        assert result == 5
    
    def test_days_between_reverse_order(self):
        """Test with dates in reverse order."""
        date1 = datetime(2024, 1, 20)
        date2 = datetime(2024, 1, 15)
        result = days_between(date1, date2)
        assert result == 5
    
    def test_days_between_same_date(self):
        """Test with same date."""
        date = datetime(2024, 1, 15)
        result = days_between(date, date)
        assert result == 0
    
    def test_days_between_invalid_first_date(self):
        """Test with invalid first date."""
        date = datetime(2024, 1, 15)
        with pytest.raises(TypeError, match="must be datetime objects"):
            days_between("not-a-date", date)
    
    def test_days_between_invalid_second_date(self):
        """Test with invalid second date."""
        date = datetime(2024, 1, 15)
        with pytest.raises(TypeError, match="must be datetime objects"):
            days_between(date, "not-a-date")


class TestIsWeekend:
    """Test is_weekend function."""
    
    def test_is_weekend_saturday(self):
        """Test with Saturday."""
        date = datetime(2024, 1, 13)  # Saturday
        assert is_weekend(date) is True
    
    def test_is_weekend_sunday(self):
        """Test with Sunday."""
        date = datetime(2024, 1, 14)  # Sunday
        assert is_weekend(date) is True
    
    def test_is_weekend_weekday(self):
        """Test with weekday."""
        date = datetime(2024, 1, 15)  # Monday
        assert is_weekend(date) is False
    
    def test_is_weekend_invalid_date(self):
        """Test with invalid date."""
        with pytest.raises(TypeError, match="must be a datetime object"):
            is_weekend("not-a-date")


class TestChunkList:
    """Test chunk_list function."""
    
    def test_chunk_list_normal(self):
        """Test chunking normal list."""
        items = [1, 2, 3, 4, 5, 6, 7]
        chunks = chunk_list(items, 3)
        assert len(chunks) == 3
        assert chunks[0] == [1, 2, 3]
        assert chunks[1] == [4, 5, 6]
        assert chunks[2] == [7]
    
    def test_chunk_list_empty(self):
        """Test chunking empty list."""
        chunks = chunk_list([], 3)
        assert chunks == []
    
    def test_chunk_list_chunk_size_one(self):
        """Test with chunk size of 1."""
        items = [1, 2, 3]
        chunks = chunk_list(items, 1)
        assert len(chunks) == 3
        assert all(len(chunk) == 1 for chunk in chunks)
    
    def test_chunk_list_chunk_size_larger_than_list(self):
        """Test with chunk size larger than list."""
        items = [1, 2, 3]
        chunks = chunk_list(items, 10)
        assert len(chunks) == 1
        assert chunks[0] == items
    
    def test_chunk_list_invalid_chunk_size(self):
        """Test with invalid chunk size."""
        with pytest.raises(ValueError, match="must be positive"):
            chunk_list([1, 2, 3], 0)
        
        with pytest.raises(ValueError, match="must be positive"):
            chunk_list([1, 2, 3], -5)


class TestFlattenList:
    """Test flatten_list function."""
    
    def test_flatten_list_normal(self):
        """Test flattening normal nested list."""
        nested = [[1, 2], [3, 4], [5]]
        result = flatten_list(nested)
        assert result == [1, 2, 3, 4, 5]
    
    def test_flatten_list_empty(self):
        """Test flattening empty list."""
        result = flatten_list([])
        assert result == []
    
    def test_flatten_list_mixed(self):
        """Test flattening mixed list with non-list items."""
        nested = [[1, 2], 3, [4, 5]]
        result = flatten_list(nested)
        assert result == [1, 2, 3, 4, 5]
    
    def test_flatten_list_no_nesting(self):
        """Test flattening list with no nesting."""
        items = [1, 2, 3]
        result = flatten_list(items)
        assert result == [1, 2, 3]


class TestRemoveDuplicates:
    """Test remove_duplicates function."""
    
    def test_remove_duplicates_preserve_order(self):
        """Test removing duplicates while preserving order."""
        items = [1, 2, 3, 2, 4, 1, 5]
        result = remove_duplicates(items, preserve_order=True)
        assert result == [1, 2, 3, 4, 5]
    
    def test_remove_duplicates_no_preserve_order(self):
        """Test removing duplicates without preserving order."""
        items = [1, 2, 3, 2, 4, 1, 5]
        result = remove_duplicates(items, preserve_order=False)
        assert set(result) == {1, 2, 3, 4, 5}
        assert len(result) == 5
    
    def test_remove_duplicates_empty(self):
        """Test removing duplicates from empty list."""
        result = remove_duplicates([])
        assert result == []
    
    def test_remove_duplicates_no_duplicates(self):
        """Test with list that has no duplicates."""
        items = [1, 2, 3, 4, 5]
        result = remove_duplicates(items)
        assert result == items
    
    def test_remove_duplicates_all_same(self):
        """Test with list where all items are the same."""
        items = [1, 1, 1, 1]
        result = remove_duplicates(items)
        assert result == [1]
