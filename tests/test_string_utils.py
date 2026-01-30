"""Comprehensive tests for string_utils module."""
import pytest
from src.string_utils import StringUtils


class TestStringUtils:
    """Test StringUtils class."""
    
    def test_reverse_string(self):
        """Test reversing a string."""
        assert StringUtils.reverse_string("hello") == "olleh"
        assert StringUtils.reverse_string("Python") == "nohtyP"
    
    def test_reverse_string_empty(self):
        """Test reversing empty string."""
        assert StringUtils.reverse_string("") == ""
    
    def test_reverse_string_single_char(self):
        """Test reversing single character."""
        assert StringUtils.reverse_string("a") == "a"
    
    def test_is_palindrome_true(self):
        """Test palindrome detection with palindromes."""
        assert StringUtils.is_palindrome("racecar") is True
        assert StringUtils.is_palindrome("A man a plan a canal Panama") is True
        assert StringUtils.is_palindrome("Was it a car or a cat I saw") is True
    
    def test_is_palindrome_false(self):
        """Test palindrome detection with non-palindromes."""
        assert StringUtils.is_palindrome("hello") is False
        assert StringUtils.is_palindrome("Python") is False
    
    def test_is_palindrome_empty(self):
        """Test palindrome detection with empty string."""
        assert StringUtils.is_palindrome("") is True
    
    def test_is_palindrome_single_char(self):
        """Test palindrome detection with single character."""
        assert StringUtils.is_palindrome("a") is True
    
    def test_is_palindrome_with_numbers(self):
        """Test palindrome detection with numbers."""
        assert StringUtils.is_palindrome("12321") is True
        assert StringUtils.is_palindrome("12345") is False
    
    def test_count_words(self):
        """Test counting words."""
        assert StringUtils.count_words("Hello world") == 2
        assert StringUtils.count_words("The quick brown fox") == 4
    
    def test_count_words_single_word(self):
        """Test counting single word."""
        assert StringUtils.count_words("Hello") == 1
    
    def test_count_words_empty(self):
        """Test counting words in empty string."""
        assert StringUtils.count_words("") == 0
        assert StringUtils.count_words("   ") == 0
    
    def test_count_words_extra_spaces(self):
        """Test counting words with extra spaces."""
        assert StringUtils.count_words("Hello   world") == 2
    
    def test_count_vowels(self):
        """Test counting vowels."""
        assert StringUtils.count_vowels("hello") == 2
        assert StringUtils.count_vowels("AEIOU") == 5
        assert StringUtils.count_vowels("Python") == 1
    
    def test_count_vowels_no_vowels(self):
        """Test counting vowels with no vowels."""
        assert StringUtils.count_vowels("xyz") == 0
    
    def test_count_vowels_empty(self):
        """Test counting vowels in empty string."""
        assert StringUtils.count_vowels("") == 0
    
    def test_count_consonants(self):
        """Test counting consonants."""
        assert StringUtils.count_consonants("hello") == 3
        assert StringUtils.count_consonants("Python") == 5
    
    def test_count_consonants_no_consonants(self):
        """Test counting consonants with no consonants."""
        assert StringUtils.count_consonants("aeiou") == 0
    
    def test_count_consonants_with_numbers(self):
        """Test counting consonants ignores numbers."""
        assert StringUtils.count_consonants("hello123") == 3
    
    def test_capitalize_words(self):
        """Test capitalizing words."""
        assert StringUtils.capitalize_words("hello world") == "Hello World"
        assert StringUtils.capitalize_words("python programming") == "Python Programming"
    
    def test_capitalize_words_already_capitalized(self):
        """Test capitalizing already capitalized words."""
        assert StringUtils.capitalize_words("Hello World") == "Hello World"
    
    def test_capitalize_words_mixed_case(self):
        """Test capitalizing mixed case words."""
        assert StringUtils.capitalize_words("hELLo WoRLd") == "Hello World"
    
    def test_remove_whitespace(self):
        """Test removing whitespace."""
        assert StringUtils.remove_whitespace("hello world") == "helloworld"
        assert StringUtils.remove_whitespace("  a  b  c  ") == "abc"
    
    def test_remove_whitespace_no_spaces(self):
        """Test removing whitespace when none exist."""
        assert StringUtils.remove_whitespace("hello") == "hello"
    
    def test_remove_whitespace_tabs_newlines(self):
        """Test removing tabs and newlines."""
        assert StringUtils.remove_whitespace("hello\tworld\n") == "helloworld"
    
    def test_truncate_short_text(self):
        """Test truncating text shorter than max length."""
        result = StringUtils.truncate("hello", 10)
        assert result == "hello"
    
    def test_truncate_long_text(self):
        """Test truncating long text."""
        result = StringUtils.truncate("hello world", 8)
        assert result == "hello..."
        assert len(result) == 8
    
    def test_truncate_custom_suffix(self):
        """Test truncating with custom suffix."""
        result = StringUtils.truncate("hello world", 8, suffix=">>")
        assert result == "hello>>"
    
    def test_truncate_exact_length(self):
        """Test truncating text at exact max length."""
        result = StringUtils.truncate("hello", 5)
        assert result == "hello"
    
    def test_extract_numbers(self):
        """Test extracting numbers from text."""
        result = StringUtils.extract_numbers("I have 3 apples and 5 oranges")
        assert result == [3, 5]
    
    def test_extract_numbers_negative(self):
        """Test extracting negative numbers."""
        result = StringUtils.extract_numbers("Temperature is -5 degrees")
        assert result == [-5]
    
    def test_extract_numbers_none(self):
        """Test extracting numbers when none exist."""
        result = StringUtils.extract_numbers("No numbers here")
        assert result == []
    
    def test_extract_numbers_multiple_digits(self):
        """Test extracting multi-digit numbers."""
        result = StringUtils.extract_numbers("Year 2024 has 365 days")
        assert result == [2024, 365]
    
    def test_extract_emails(self):
        """Test extracting email addresses."""
        text = "Contact us at info@example.com or support@test.org"
        result = StringUtils.extract_emails(text)
        assert "info@example.com" in result
        assert "support@test.org" in result
    
    def test_extract_emails_none(self):
        """Test extracting emails when none exist."""
        result = StringUtils.extract_emails("No emails here")
        assert result == []
    
    def test_extract_emails_complex(self):
        """Test extracting complex email addresses."""
        text = "Email: user.name+tag@example.co.uk"
        result = StringUtils.extract_emails(text)
        assert len(result) > 0
    
    def test_snake_to_camel(self):
        """Test converting snake_case to camelCase."""
        assert StringUtils.snake_to_camel("hello_world") == "helloWorld"
        assert StringUtils.snake_to_camel("user_name_field") == "userNameField"
    
    def test_snake_to_camel_no_underscores(self):
        """Test converting snake_case with no underscores."""
        assert StringUtils.snake_to_camel("hello") == "hello"
    
    def test_snake_to_camel_single_underscore(self):
        """Test converting snake_case with single underscore."""
        assert StringUtils.snake_to_camel("hello_world") == "helloWorld"
    
    def test_camel_to_snake(self):
        """Test converting camelCase to snake_case."""
        assert StringUtils.camel_to_snake("helloWorld") == "hello_world"
        assert StringUtils.camel_to_snake("userNameField") == "user_name_field"
    
    def test_camel_to_snake_no_capitals(self):
        """Test converting camelCase with no capitals."""
        assert StringUtils.camel_to_snake("hello") == "hello"
    
    def test_camel_to_snake_pascal_case(self):
        """Test converting PascalCase to snake_case."""
        assert StringUtils.camel_to_snake("HelloWorld") == "hello_world"
    
    def test_find_longest_word(self):
        """Test finding longest word."""
        result = StringUtils.find_longest_word("The quick brown fox")
        assert result == "quick" or result == "brown"
    
    def test_find_longest_word_single_word(self):
        """Test finding longest word with single word."""
        result = StringUtils.find_longest_word("Hello")
        assert result == "Hello"
    
    def test_find_longest_word_empty(self):
        """Test finding longest word in empty string."""
        result = StringUtils.find_longest_word("")
        assert result is None
    
    def test_find_longest_word_whitespace_only(self):
        """Test finding longest word with only whitespace."""
        result = StringUtils.find_longest_word("   ")
        assert result is None
