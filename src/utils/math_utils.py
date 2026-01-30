"""Mathematical utility functions."""


def calculate_average(numbers):
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Average of the numbers
        
    Raises:
        ValueError: If the list is empty
        TypeError: If any element is not a number
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, got {type(num).__name__}")
    
    return sum(numbers) / len(numbers)


def is_prime(n):
    """Check if a number is prime.
    
    Args:
        n: Number to check
        
    Returns:
        True if n is prime, False otherwise
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 2
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Prime numbers must be >= 2")
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def factorial(n):
    """Calculate the factorial of a number.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def fibonacci(n):
    """Generate the first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Returns:
        List of the first n Fibonacci numbers
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 1
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("n must be at least 1")
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib
