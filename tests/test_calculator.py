"""Comprehensive tests for calculator module."""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test Calculator class."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert result == 6
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        calc = Calculator()
        result = calc.add(10, -3)
        assert result == 7
    
    def test_add_floats(self):
        """Test adding float numbers."""
        calc = Calculator()
        result = calc.add(5.5, 2.3)
        assert abs(result - 7.8) < 0.0001
    
    def test_add_invalid_type(self):
        """Test add with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add("5", 3)
        with pytest.raises(TypeError):
            calc.add(5, "3")
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        calc = Calculator()
        result = calc.subtract(-5, -3)
        assert result == -2
    
    def test_subtract_invalid_type(self):
        """Test subtract with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.subtract("10", 4)
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        calc = Calculator()
        result = calc.multiply(5, 3)
        assert result == 15
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        calc = Calculator()
        result = calc.multiply(-5, -3)
        assert result == 15
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        calc = Calculator()
        result = calc.multiply(5, 0)
        assert result == 0
    
    def test_multiply_invalid_type(self):
        """Test multiply with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.multiply(5, None)
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5
    
    def test_divide_with_remainder(self):
        """Test dividing with remainder."""
        calc = Calculator()
        result = calc.divide(10, 3)
        assert abs(result - 3.333333) < 0.0001
    
    def test_divide_by_zero(self):
        """Test divide by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
    
    def test_divide_invalid_type(self):
        """Test divide with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.divide(10, "2")
    
    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        calc = Calculator()
        result = calc.power(2, 3)
        assert result == 8
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        calc = Calculator()
        result = calc.power(2, -2)
        assert result == 0.25
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        calc = Calculator()
        result = calc.power(5, 0)
        assert result == 1
    
    def test_power_invalid_type(self):
        """Test power with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.power("2", 3)
    
    def test_history_tracking(self):
        """Test calculation history is tracked."""
        calc = Calculator()
        calc.add(5, 3)
        calc.subtract(10, 4)
        calc.multiply(2, 3)
        
        history = calc.get_history()
        assert len(history) == 3
        assert "5 + 3 = 8" in history
        assert "10 - 4 = 6" in history
        assert "2 * 3 = 6" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        calc = Calculator()
        calc.add(5, 3)
        calc.subtract(10, 4)
        
        calc.clear_history()
        history = calc.get_history()
        assert len(history) == 0
    
    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not reference."""
        calc = Calculator()
        calc.add(5, 3)
        
        history1 = calc.get_history()
        history1.append("fake entry")
        
        history2 = calc.get_history()
        assert len(history2) == 1
        assert "fake entry" not in history2
