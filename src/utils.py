"""
Utility functions for string manipulation and date handling.
"""
from datetime import datetime, timedelta
from typing import Optional, List


def sanitize_string(text: str, max_length: Optional[int] = None) -> str:
    """Sanitize string by removing special characters and trimming."""
    if not text or not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace
    sanitized = text.strip()
    
    # Remove multiple spaces
    sanitized = " ".join(sanitized.split())
    
    # Truncate if max_length specified
    if max_length and max_length > 0:
        sanitized = sanitized[:max_length]
    
    return sanitized


def truncate_string(text: str, length: int, suffix: str = "...") -> str:
    """Truncate string to specified length with suffix."""
    if not text:
        return ""
    
    if length <= 0:
        return ""
    
    if len(text) <= length:
        return text
    
    if len(suffix) >= length:
        return text[:length]
    
    return text[:length - len(suffix)] + suffix


def parse_date(date_string: str, format_string: str = "%Y-%m-%d") -> Optional[datetime]:
    """Parse date string to datetime object."""
    if not date_string:
        return None
    
    try:
        return datetime.strptime(date_string, format_string)
    except ValueError:
        return None


def format_date(date: datetime, format_string: str = "%Y-%m-%d") -> str:
    """Format datetime object to string."""
    if not date or not isinstance(date, datetime):
        return ""
    
    try:
        return date.strftime(format_string)
    except Exception:
        return ""


def add_days(date: datetime, days: int) -> datetime:
    """Add days to a datetime object."""
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object")
    
    return date + timedelta(days=days)


def days_between(date1: datetime, date2: datetime) -> int:
    """Calculate days between two dates."""
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise TypeError("Both arguments must be datetime objects")
    
    delta = date2 - date1
    return abs(delta.days)


def is_weekend(date: datetime) -> bool:
    """Check if date falls on weekend."""
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object")
    
    # Monday is 0, Sunday is 6
    return date.weekday() in [5, 6]


def chunk_list(items: List, chunk_size: int) -> List[List]:
    """Split list into chunks of specified size."""
    if not items:
        return []
    
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    
    return chunks


def flatten_list(nested_list: List[List]) -> List:
    """Flatten a nested list."""
    if not nested_list:
        return []
    
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    
    return flattened


def remove_duplicates(items: List, preserve_order: bool = True) -> List:
    """Remove duplicates from list."""
    if not items:
        return []
    
    if preserve_order:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    else:
        return list(set(items))
