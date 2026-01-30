"""String utility functions."""
import re
from typing import List, Optional


class StringUtils:
    """Utility class for string operations."""
    
    @staticmethod
    def reverse_string(text: str) -> str:
        """Reverse a string."""
        return text[::-1]
    
    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Check if string is a palindrome (case-insensitive)."""
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def count_words(text: str) -> int:
        """Count words in text."""
        if not text or not text.strip():
            return 0
        return len(text.split())
    
    @staticmethod
    def count_vowels(text: str) -> int:
        """Count vowels in text."""
        return sum(1 for char in text.lower() if char in 'aeiou')
    
    @staticmethod
    def count_consonants(text: str) -> int:
        """Count consonants in text."""
        return sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    
    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in text.split())
    
    @staticmethod
    def remove_whitespace(text: str) -> str:
        """Remove all whitespace from text."""
        return ''.join(text.split())
    
    @staticmethod
    def truncate(text: str, max_length: int, suffix: str = "...") -> str:
        """Truncate text to max length with suffix."""
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix
    
    @staticmethod
    def extract_numbers(text: str) -> List[int]:
        """Extract all numbers from text."""
        return [int(match) for match in re.findall(r'-?\d+', text)]
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """Extract email addresses from text."""
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)
    
    @staticmethod
    def snake_to_camel(text: str) -> str:
        """Convert snake_case to camelCase."""
        components = text.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    @staticmethod
    def camel_to_snake(text: str) -> str:
        """Convert camelCase to snake_case."""
        return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    
    @staticmethod
    def find_longest_word(text: str) -> Optional[str]:
        """Find the longest word in text."""
        if not text or not text.strip():
            return None
        words = text.split()
        return max(words, key=len) if words else None
