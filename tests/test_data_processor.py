"""
Basic tests for data_processor module (intentionally incomplete for initial coverage).
"""
import pytest
from src.data_processor import DataProcessor


def test_calculate_statistics():
    """Test calculating statistics for a list of numbers."""
    processor = DataProcessor()
    numbers = [1, 2, 3, 4, 5]
    
    stats = processor.calculate_statistics(numbers)
    
    assert stats["mean"] == 3.0
    assert stats["median"] == 3
    assert stats["min"] == 1
    assert stats["max"] == 5
    assert stats["count"] == 5


def test_normalize_data():
    """Test normalizing data to 0-1 range."""
    processor = DataProcessor()
    numbers = [0, 50, 100]
    
    normalized = processor.normalize_data(numbers)
    
    assert normalized[0] == 0.0
    assert normalized[1] == 0.5
    assert normalized[2] == 1.0
