"""Tests for string utility functions."""

import pytest
from src.utils.string_utils import (
    capitalize_words,
    reverse_string,
    count_vowels,
    truncate_string
)


class TestCapitalizeWords:
    """Tests for capitalize_words function."""
    
    def test_capitalize_words_valid_input(self):
        """Test capitalizing words with valid input."""
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"
        assert capitalize_words("test") == "Test"
    
    def test_capitalize_words_already_capitalized(self):
        """Test with already capitalized words."""
        assert capitalize_words("Hello World") == "Hello World"
    
    def test_capitalize_words_mixed_case(self):
        """Test with mixed case input."""
        assert capitalize_words("hELLo WoRLd") == "Hello World"
    
    def test_capitalize_words_multiple_spaces(self):
        """Test with multiple spaces between words."""
        assert capitalize_words("hello  world") == "Hello World"
    
    def test_capitalize_words_single_word(self):
        """Test with single word."""
        assert capitalize_words("hello") == "Hello"
    
    def test_capitalize_words_empty_string_raises_error(self):
        """Test that empty string raises ValueError."""
        with pytest.raises(ValueError, match="Input string cannot be empty"):
            capitalize_words("")
    
    def test_capitalize_words_invalid_type_raises_error(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be a string"):
            capitalize_words(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            capitalize_words(None)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            capitalize_words(["hello"])


class TestReverseString:
    """Tests for reverse_string function."""
    
    def test_reverse_string_valid_input(self):
        """Test reversing string with valid input."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("python") == "nohtyp"
        assert reverse_string("a") == "a"
    
    def test_reverse_string_empty_string(self):
        """Test reversing empty string."""
        assert reverse_string("") == ""
    
    def test_reverse_string_palindrome(self):
        """Test reversing palindrome."""
        assert reverse_string("racecar") == "racecar"
        assert reverse_string("noon") == "noon"
    
    def test_reverse_string_with_spaces(self):
        """Test reversing string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"
    
    def test_reverse_string_with_special_chars(self):
        """Test reversing string with special characters."""
        assert reverse_string("hello!@#") == "#@!olleh"
    
    def test_reverse_string_invalid_type_raises_error(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(None)


class TestCountVowels:
    """Tests for count_vowels function."""
    
    def test_count_vowels_valid_input(self):
        """Test counting vowels with valid input."""
        assert count_vowels("hello") == 2
        assert count_vowels("python") == 1
        assert count_vowels("aeiou") == 5
    
    def test_count_vowels_no_vowels(self):
        """Test string with no vowels."""
        assert count_vowels("xyz") == 0
        assert count_vowels("bcdfg") == 0
    
    def test_count_vowels_all_vowels(self):
        """Test string with all vowels."""
        assert count_vowels("aeiouAEIOU") == 10
    
    def test_count_vowels_empty_string(self):
        """Test empty string."""
        assert count_vowels("") == 0
    
    def test_count_vowels_mixed_case(self):
        """Test with mixed case vowels."""
        assert count_vowels("HeLLo WoRLd") == 3
    
    def test_count_vowels_with_numbers(self):
        """Test string with numbers."""
        assert count_vowels("hello123") == 2
    
    def test_count_vowels_with_special_chars(self):
        """Test string with special characters."""
        assert count_vowels("hello!@#world") == 3
    
    def test_count_vowels_invalid_type_raises_error(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be a string"):
            count_vowels(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            count_vowels(None)


class TestTruncateString:
    """Tests for truncate_string function."""
    
    def test_truncate_string_no_truncation_needed(self):
        """Test when string is shorter than max length."""
        assert truncate_string("hello", 10) == "hello"
        assert truncate_string("test", 10) == "test"
    
    def test_truncate_string_exact_length(self):
        """Test when string is exactly max length."""
        assert truncate_string("hello", 5) == "hello"
    
    def test_truncate_string_with_truncation(self):
        """Test truncating longer string."""
        assert truncate_string("hello world", 8) == "hello..."
        assert truncate_string("python programming", 10) == "python ..."
    
    def test_truncate_string_custom_suffix(self):
        """Test with custom suffix."""
        assert truncate_string("hello world", 8, ">>") == "hello >>"
        assert truncate_string("python programming", 10, " [more]") == "pyt [more]"
    
    def test_truncate_string_empty_suffix(self):
        """Test with empty suffix."""
        assert truncate_string("hello world", 5, "") == "hello"
    
    def test_truncate_string_empty_string(self):
        """Test with empty string."""
        assert truncate_string("", 10) == ""
    
    def test_truncate_string_invalid_text_type_raises_error(self):
        """Test that non-string text raises TypeError."""
        with pytest.raises(TypeError, match="Text must be a string"):
            truncate_string(123, 10)
    
    def test_truncate_string_invalid_max_length_type_raises_error(self):
        """Test that non-integer max_length raises TypeError."""
        with pytest.raises(TypeError, match="Max length must be an integer"):
            truncate_string("hello", "10")
        
        with pytest.raises(TypeError, match="Max length must be an integer"):
            truncate_string("hello", 10.5)
    
    def test_truncate_string_max_length_less_than_suffix_raises_error(self):
        """Test that max_length < suffix length raises ValueError."""
        with pytest.raises(ValueError, match="Max length must be at least as long as the suffix"):
            truncate_string("hello", 2, "...")
        
        with pytest.raises(ValueError, match="Max length must be at least as long as the suffix"):
            truncate_string("hello", 1, ">>")
    
    def test_truncate_string_boundary_case(self):
        """Test boundary case where max_length equals suffix length."""
        assert truncate_string("hello world", 3, "...") == "..."
