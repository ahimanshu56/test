"""String utility functions."""


def capitalize_words(text):
    """Capitalize the first letter of each word in a string.
    
    Args:
        text: Input string to capitalize
        
    Returns:
        String with each word capitalized
        
    Raises:
        TypeError: If text is not a string
        ValueError: If text is empty
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text):
    """Reverse a string.
    
    Args:
        text: Input string to reverse
        
    Returns:
        Reversed string
        
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text[::-1]


def count_vowels(text):
    """Count the number of vowels in a string.
    
    Args:
        text: Input string
        
    Returns:
        Number of vowels (a, e, i, o, u) in the string
        
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def truncate_string(text, max_length, suffix='...'):
    """Truncate a string to a maximum length.
    
    Args:
        text: Input string to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add if truncated (default: '...')
        
    Returns:
        Truncated string with suffix if needed
        
    Raises:
        TypeError: If text is not a string or max_length is not an integer
        ValueError: If max_length is less than the suffix length
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    
    if not isinstance(max_length, int):
        raise TypeError("Max length must be an integer")
    
    if max_length < len(suffix):
        raise ValueError("Max length must be at least as long as the suffix")
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix
