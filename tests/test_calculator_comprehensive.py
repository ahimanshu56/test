"""
Comprehensive tests for Calculator module.
Achieves 100% coverage of all functions, branches, and edge cases.
"""

import pytest
import math
from src.calculator import Calculator


class TestCalculatorDiscount:
    """Tests for discount calculations."""
    
    def test_calculate_discount_valid(self):
        """Test calculating discount with valid inputs."""
        assert Calculator.calculate_discount(100, 10) == 90.0
        assert Calculator.calculate_discount(50, 20) == 40.0
        assert Calculator.calculate_discount(100, 0) == 100.0
    
    def test_calculate_discount_negative_price(self):
        """Test calculating discount with negative price."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            Calculator.calculate_discount(-100, 10)
    
    def test_calculate_discount_invalid_percent_negative(self):
        """Test calculating discount with negative percent."""
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            Calculator.calculate_discount(100, -10)
    
    def test_calculate_discount_invalid_percent_over_100(self):
        """Test calculating discount with percent over 100."""
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            Calculator.calculate_discount(100, 150)
    
    def test_calculate_discount_100_percent(self):
        """Test calculating 100% discount."""
        assert Calculator.calculate_discount(100, 100) == 0.0


class TestCalculatorTax:
    """Tests for tax calculations."""
    
    def test_calculate_tax_valid(self):
        """Test calculating tax with valid inputs."""
        assert Calculator.calculate_tax(100, 0.08) == 8.0
        assert Calculator.calculate_tax(50, 0.10) == 5.0
    
    def test_calculate_tax_negative_amount(self):
        """Test calculating tax with negative amount."""
        with pytest.raises(ValueError, match="Amount cannot be negative"):
            Calculator.calculate_tax(-100, 0.08)
    
    def test_calculate_tax_negative_rate(self):
        """Test calculating tax with negative rate."""
        with pytest.raises(ValueError, match="Tax rate cannot be negative"):
            Calculator.calculate_tax(100, -0.08)
    
    def test_calculate_tax_zero_rate(self):
        """Test calculating tax with zero rate."""
        assert Calculator.calculate_tax(100, 0) == 0.0
    
    def test_calculate_total_with_tax_valid(self):
        """Test calculating total with tax."""
        assert Calculator.calculate_total_with_tax(100, 0.08) == 108.0
        assert Calculator.calculate_total_with_tax(50, 0.10) == 55.0
    
    def test_calculate_total_with_tax_negative_amount(self):
        """Test calculating total with negative amount."""
        with pytest.raises(ValueError, match="Amount cannot be negative"):
            Calculator.calculate_total_with_tax(-100, 0.08)
    
    def test_calculate_total_with_tax_negative_rate(self):
        """Test calculating total with negative rate."""
        with pytest.raises(ValueError, match="Tax rate cannot be negative"):
            Calculator.calculate_total_with_tax(100, -0.08)


class TestCalculatorCompoundInterest:
    """Tests for compound interest calculations."""
    
    def test_calculate_compound_interest_valid(self):
        """Test calculating compound interest with valid inputs."""
        result = Calculator.calculate_compound_interest(1000, 0.05, 10, 1)
        assert result > 1000
        assert result == pytest.approx(1628.89, rel=0.01)
    
    def test_calculate_compound_interest_quarterly(self):
        """Test calculating compound interest with quarterly compounding."""
        result = Calculator.calculate_compound_interest(1000, 0.05, 10, 4)
        assert result > 1000
    
    def test_calculate_compound_interest_negative_principal(self):
        """Test calculating compound interest with negative principal."""
        with pytest.raises(ValueError, match="Principal cannot be negative"):
            Calculator.calculate_compound_interest(-1000, 0.05, 10, 1)
    
    def test_calculate_compound_interest_negative_rate(self):
        """Test calculating compound interest with negative rate."""
        with pytest.raises(ValueError, match="Rate cannot be negative"):
            Calculator.calculate_compound_interest(1000, -0.05, 10, 1)
    
    def test_calculate_compound_interest_negative_time(self):
        """Test calculating compound interest with negative time."""
        with pytest.raises(ValueError, match="Time cannot be negative"):
            Calculator.calculate_compound_interest(1000, 0.05, -10, 1)
    
    def test_calculate_compound_interest_invalid_compounds(self):
        """Test calculating compound interest with invalid compounds per year."""
        with pytest.raises(ValueError, match="Compounds per year must be at least 1"):
            Calculator.calculate_compound_interest(1000, 0.05, 10, 0)


class TestCalculatorLoanPayment:
    """Tests for loan payment calculations."""
    
    def test_calculate_loan_payment_valid(self):
        """Test calculating loan payment with valid inputs."""
        result = Calculator.calculate_loan_payment(10000, 0.05, 60)
        assert result > 0
        assert result == pytest.approx(188.71, rel=0.01)
    
    def test_calculate_loan_payment_zero_rate(self):
        """Test calculating loan payment with zero interest rate."""
        result = Calculator.calculate_loan_payment(12000, 0, 12)
        assert result == 1000.0
    
    def test_calculate_loan_payment_negative_principal(self):
        """Test calculating loan payment with negative principal."""
        with pytest.raises(ValueError, match="Principal must be positive"):
            Calculator.calculate_loan_payment(-10000, 0.05, 60)
    
    def test_calculate_loan_payment_zero_principal(self):
        """Test calculating loan payment with zero principal."""
        with pytest.raises(ValueError, match="Principal must be positive"):
            Calculator.calculate_loan_payment(0, 0.05, 60)
    
    def test_calculate_loan_payment_negative_rate(self):
        """Test calculating loan payment with negative rate."""
        with pytest.raises(ValueError, match="Rate cannot be negative"):
            Calculator.calculate_loan_payment(10000, -0.05, 60)
    
    def test_calculate_loan_payment_negative_months(self):
        """Test calculating loan payment with negative months."""
        with pytest.raises(ValueError, match="Months must be positive"):
            Calculator.calculate_loan_payment(10000, 0.05, -60)
    
    def test_calculate_loan_payment_zero_months(self):
        """Test calculating loan payment with zero months."""
        with pytest.raises(ValueError, match="Months must be positive"):
            Calculator.calculate_loan_payment(10000, 0.05, 0)


class TestCalculatorAverage:
    """Tests for average calculations."""
    
    def test_calculate_average_valid(self):
        """Test calculating average with valid inputs."""
        assert Calculator.calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert Calculator.calculate_average([10, 20, 30]) == 20.0
    
    def test_calculate_average_single_value(self):
        """Test calculating average with single value."""
        assert Calculator.calculate_average([42]) == 42.0
    
    def test_calculate_average_empty_list(self):
        """Test calculating average with empty list."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            Calculator.calculate_average([])
    
    def test_calculate_average_negative_values(self):
        """Test calculating average with negative values."""
        assert Calculator.calculate_average([-5, 0, 5]) == 0.0


class TestCalculatorPercentage:
    """Tests for percentage calculations."""
    
    def test_calculate_percentage_valid(self):
        """Test calculating percentage with valid inputs."""
        assert Calculator.calculate_percentage(25, 100) == 25.0
        assert Calculator.calculate_percentage(50, 200) == 25.0
    
    def test_calculate_percentage_zero_whole(self):
        """Test calculating percentage with zero whole."""
        with pytest.raises(ValueError, match="Cannot calculate percentage with zero whole"):
            Calculator.calculate_percentage(25, 0)
    
    def test_calculate_percentage_over_100(self):
        """Test calculating percentage over 100."""
        assert Calculator.calculate_percentage(150, 100) == 150.0


class TestCalculatorBMI:
    """Tests for BMI calculations."""
    
    def test_calculate_bmi_valid(self):
        """Test calculating BMI with valid inputs."""
        result = Calculator.calculate_bmi(70, 1.75)
        assert result == pytest.approx(22.86, rel=0.01)
    
    def test_calculate_bmi_negative_weight(self):
        """Test calculating BMI with negative weight."""
        with pytest.raises(ValueError, match="Weight must be positive"):
            Calculator.calculate_bmi(-70, 1.75)
    
    def test_calculate_bmi_zero_weight(self):
        """Test calculating BMI with zero weight."""
        with pytest.raises(ValueError, match="Weight must be positive"):
            Calculator.calculate_bmi(0, 1.75)
    
    def test_calculate_bmi_negative_height(self):
        """Test calculating BMI with negative height."""
        with pytest.raises(ValueError, match="Height must be positive"):
            Calculator.calculate_bmi(70, -1.75)
    
    def test_calculate_bmi_zero_height(self):
        """Test calculating BMI with zero height."""
        with pytest.raises(ValueError, match="Height must be positive"):
            Calculator.calculate_bmi(70, 0)


class TestCalculatorDistance:
    """Tests for distance calculations."""
    
    def test_calculate_distance_valid(self):
        """Test calculating distance with valid inputs."""
        result = Calculator.calculate_distance(0, 0, 3, 4)
        assert result == 5.0
    
    def test_calculate_distance_same_point(self):
        """Test calculating distance between same points."""
        result = Calculator.calculate_distance(5, 5, 5, 5)
        assert result == 0.0
    
    def test_calculate_distance_negative_coordinates(self):
        """Test calculating distance with negative coordinates."""
        result = Calculator.calculate_distance(-3, -4, 0, 0)
        assert result == 5.0


class TestCalculatorFactorial:
    """Tests for factorial calculations."""
    
    def test_calculate_factorial_zero(self):
        """Test calculating factorial of zero."""
        assert Calculator.calculate_factorial(0) == 1
    
    def test_calculate_factorial_one(self):
        """Test calculating factorial of one."""
        assert Calculator.calculate_factorial(1) == 1
    
    def test_calculate_factorial_positive(self):
        """Test calculating factorial of positive numbers."""
        assert Calculator.calculate_factorial(5) == 120
        assert Calculator.calculate_factorial(10) == 3628800
    
    def test_calculate_factorial_negative(self):
        """Test calculating factorial of negative number."""
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            Calculator.calculate_factorial(-5)


class TestCalculatorPrime:
    """Tests for prime number checking."""
    
    def test_is_prime_small_primes(self):
        """Test checking small prime numbers."""
        assert Calculator.is_prime(2) is True
        assert Calculator.is_prime(3) is True
        assert Calculator.is_prime(5) is True
        assert Calculator.is_prime(7) is True
    
    def test_is_prime_large_primes(self):
        """Test checking larger prime numbers."""
        assert Calculator.is_prime(11) is True
        assert Calculator.is_prime(13) is True
        assert Calculator.is_prime(97) is True
    
    def test_is_prime_not_prime(self):
        """Test checking non-prime numbers."""
        assert Calculator.is_prime(4) is False
        assert Calculator.is_prime(6) is False
        assert Calculator.is_prime(9) is False
        assert Calculator.is_prime(100) is False
    
    def test_is_prime_less_than_two(self):
        """Test checking numbers less than 2."""
        assert Calculator.is_prime(0) is False
        assert Calculator.is_prime(1) is False
        assert Calculator.is_prime(-5) is False
    
    def test_is_prime_even_numbers(self):
        """Test checking even numbers."""
        assert Calculator.is_prime(2) is True  # Only even prime
        assert Calculator.is_prime(4) is False
        assert Calculator.is_prime(8) is False
