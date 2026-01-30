"""Tests for math utility functions."""

import pytest
from src.utils.math_utils import (
    calculate_average,
    is_prime,
    factorial,
    fibonacci
)


class TestCalculateAverage:
    """Tests for calculate_average function."""
    
    def test_calculate_average_valid_integers(self):
        """Test calculating average with valid integers."""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20, 30]) == 20.0
        assert calculate_average([5]) == 5.0
    
    def test_calculate_average_valid_floats(self):
        """Test calculating average with floats."""
        assert calculate_average([1.5, 2.5, 3.5]) == 2.5
        assert calculate_average([0.1, 0.2, 0.3]) == pytest.approx(0.2, rel=1e-9)
    
    def test_calculate_average_mixed_numbers(self):
        """Test calculating average with mixed int and float."""
        assert calculate_average([1, 2.5, 3, 4.5]) == 2.75
    
    def test_calculate_average_negative_numbers(self):
        """Test calculating average with negative numbers."""
        assert calculate_average([-1, -2, -3]) == -2.0
        assert calculate_average([-5, 5]) == 0.0
    
    def test_calculate_average_zero(self):
        """Test calculating average with zeros."""
        assert calculate_average([0, 0, 0]) == 0.0
    
    def test_calculate_average_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            calculate_average([])
    
    def test_calculate_average_invalid_type_raises_error(self):
        """Test that non-numeric elements raise TypeError."""
        with pytest.raises(TypeError, match="All elements must be numbers"):
            calculate_average([1, 2, "3"])
        
        with pytest.raises(TypeError, match="All elements must be numbers"):
            calculate_average([1, None, 3])
        
        with pytest.raises(TypeError, match="All elements must be numbers"):
            calculate_average(["a", "b", "c"])


class TestIsPrime:
    """Tests for is_prime function."""
    
    def test_is_prime_valid_primes(self):
        """Test with valid prime numbers."""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
        assert is_prime(97) is True
    
    def test_is_prime_non_primes(self):
        """Test with non-prime numbers."""
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(100) is False
    
    def test_is_prime_edge_case_two(self):
        """Test edge case for 2 (only even prime)."""
        assert is_prime(2) is True
    
    def test_is_prime_large_prime(self):
        """Test with larger prime number."""
        assert is_prime(101) is True
        assert is_prime(103) is True
    
    def test_is_prime_large_non_prime(self):
        """Test with larger non-prime number."""
        assert is_prime(100) is False
        assert is_prime(102) is False
    
    def test_is_prime_less_than_two_raises_error(self):
        """Test that numbers < 2 raise ValueError."""
        with pytest.raises(ValueError, match="Prime numbers must be >= 2"):
            is_prime(1)
        
        with pytest.raises(ValueError, match="Prime numbers must be >= 2"):
            is_prime(0)
        
        with pytest.raises(ValueError, match="Prime numbers must be >= 2"):
            is_prime(-5)
    
    def test_is_prime_invalid_type_raises_error(self):
        """Test that non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            is_prime(5.5)
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            is_prime("5")
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            is_prime(None)


class TestFactorial:
    """Tests for factorial function."""
    
    def test_factorial_valid_positive_numbers(self):
        """Test factorial with valid positive numbers."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(10) == 3628800
    
    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1
    
    def test_factorial_large_number(self):
        """Test factorial of larger number."""
        assert factorial(6) == 720
        assert factorial(7) == 5040
    
    def test_factorial_negative_raises_error(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
        
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-10)
    
    def test_factorial_invalid_type_raises_error(self):
        """Test that non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial(5.5)
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial("5")
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial(None)


class TestFibonacci:
    """Tests for fibonacci function."""
    
    def test_fibonacci_valid_input(self):
        """Test fibonacci with valid input."""
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(3) == [0, 1, 1]
        assert fibonacci(4) == [0, 1, 1, 2]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
        assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    
    def test_fibonacci_one(self):
        """Test fibonacci with n=1."""
        assert fibonacci(1) == [0]
    
    def test_fibonacci_two(self):
        """Test fibonacci with n=2."""
        assert fibonacci(2) == [0, 1]
    
    def test_fibonacci_larger_sequence(self):
        """Test fibonacci with larger n."""
        result = fibonacci(10)
        assert len(result) == 10
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_fibonacci_sequence_property(self):
        """Test that fibonacci sequence follows the property."""
        result = fibonacci(8)
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]
    
    def test_fibonacci_less_than_one_raises_error(self):
        """Test that n < 1 raises ValueError."""
        with pytest.raises(ValueError, match="n must be at least 1"):
            fibonacci(0)
        
        with pytest.raises(ValueError, match="n must be at least 1"):
            fibonacci(-1)
        
        with pytest.raises(ValueError, match="n must be at least 1"):
            fibonacci(-10)
    
    def test_fibonacci_invalid_type_raises_error(self):
        """Test that non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            fibonacci(5.5)
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            fibonacci("5")
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            fibonacci(None)
