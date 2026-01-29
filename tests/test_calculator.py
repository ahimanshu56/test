"""
Initial minimal tests for Calculator (intentionally incomplete for baseline).
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Basic tests for Calculator."""
    
    def test_calculate_discount(self):
        """Test discount calculation."""
        result = Calculator.calculate_discount(100, 10)
        assert result == 90.0
    
    def test_calculate_average(self):
        """Test average calculation."""
        result = Calculator.calculate_average([1, 2, 3, 4, 5])
        assert result == 3.0
