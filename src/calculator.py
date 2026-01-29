"""
Calculator Module
Provides business logic calculations and mathematical operations.
"""

from typing import List, Optional
import math


class Calculator:
    """Perform calculations and business logic operations."""
    
    @staticmethod
    def calculate_discount(price: float, discount_percent: float) -> float:
        """
        Calculate discounted price.
        
        Args:
            price: Original price
            discount_percent: Discount percentage (0-100)
            
        Returns:
            Discounted price
            
        Raises:
            ValueError: If inputs are invalid
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    
    @staticmethod
    def calculate_tax(amount: float, tax_rate: float) -> float:
        """
        Calculate tax amount.
        
        Args:
            amount: Base amount
            tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
            
        Returns:
            Tax amount
            
        Raises:
            ValueError: If inputs are invalid
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        
        return amount * tax_rate
    
    @staticmethod
    def calculate_total_with_tax(amount: float, tax_rate: float) -> float:
        """Calculate total amount including tax."""
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        
        return amount * (1 + tax_rate)
    
    @staticmethod
    def calculate_compound_interest(principal: float, rate: float, time: float, 
                                   compounds_per_year: int = 1) -> float:
        """
        Calculate compound interest.
        
        Args:
            principal: Initial principal amount
            rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
            time: Time in years
            compounds_per_year: Number of times interest compounds per year
            
        Returns:
            Final amount after compound interest
            
        Raises:
            ValueError: If inputs are invalid
        """
        if principal < 0:
            raise ValueError("Principal cannot be negative")
        
        if rate < 0:
            raise ValueError("Rate cannot be negative")
        
        if time < 0:
            raise ValueError("Time cannot be negative")
        
        if compounds_per_year < 1:
            raise ValueError("Compounds per year must be at least 1")
        
        amount = principal * math.pow(1 + (rate / compounds_per_year), 
                                     compounds_per_year * time)
        return round(amount, 2)
    
    @staticmethod
    def calculate_loan_payment(principal: float, annual_rate: float, 
                              months: int) -> float:
        """
        Calculate monthly loan payment.
        
        Args:
            principal: Loan principal amount
            annual_rate: Annual interest rate (as decimal)
            months: Loan term in months
            
        Returns:
            Monthly payment amount
            
        Raises:
            ValueError: If inputs are invalid
        """
        if principal <= 0:
            raise ValueError("Principal must be positive")
        
        if annual_rate < 0:
            raise ValueError("Rate cannot be negative")
        
        if months <= 0:
            raise ValueError("Months must be positive")
        
        if annual_rate == 0:
            return principal / months
        
        monthly_rate = annual_rate / 12
        payment = principal * (monthly_rate * math.pow(1 + monthly_rate, months)) / \
                  (math.pow(1 + monthly_rate, months) - 1)
        
        return round(payment, 2)
    
    @staticmethod
    def calculate_average(numbers: List[float]) -> float:
        """
        Calculate average of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Average value
            
        Raises:
            ValueError: If list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def calculate_percentage(part: float, whole: float) -> float:
        """
        Calculate what percentage 'part' is of 'whole'.
        
        Args:
            part: Part value
            whole: Whole value
            
        Returns:
            Percentage
            
        Raises:
            ValueError: If whole is zero
        """
        if whole == 0:
            raise ValueError("Cannot calculate percentage with zero whole")
        
        return (part / whole) * 100
    
    @staticmethod
    def calculate_bmi(weight_kg: float, height_m: float) -> float:
        """
        Calculate Body Mass Index.
        
        Args:
            weight_kg: Weight in kilograms
            height_m: Height in meters
            
        Returns:
            BMI value
            
        Raises:
            ValueError: If inputs are invalid
        """
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")
        
        if height_m <= 0:
            raise ValueError("Height must be positive")
        
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    
    @staticmethod
    def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        Calculate Euclidean distance between two points.
        
        Args:
            x1, y1: Coordinates of first point
            x2, y2: Coordinates of second point
            
        Returns:
            Distance between points
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    @staticmethod
    def calculate_factorial(n: int) -> int:
        """
        Calculate factorial of n.
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        
        if n == 0 or n == 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        return result
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Check if a number is prime.
        
        Args:
            n: Integer to check
            
        Returns:
            True if prime, False otherwise
        """
        if n < 2:
            return False
        
        if n == 2:
            return True
        
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True
