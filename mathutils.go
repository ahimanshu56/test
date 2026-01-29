package main

import (
	"errors"
	"math"
)

// Clamp restricts a value to be within a specified range
func Clamp(value, min, max float64) float64 {
	if value < min {
		return min
	}
	if value > max {
		return max
	}
	return value
}

// Average calculates the mean of a slice of numbers
func Average(numbers []float64) float64 {
	if len(numbers) == 0 {
		return 0
	}
	sum := 0.0
	for _, num := range numbers {
		sum += num
	}
	return sum / float64(len(numbers))
}

// Median calculates the median of a slice of numbers
func Median(numbers []float64) float64 {
	if len(numbers) == 0 {
		return 0
	}
	
	// Create a copy and sort it
	sorted := make([]float64, len(numbers))
	copy(sorted, numbers)
	
	// Simple bubble sort for demonstration
	for i := 0; i < len(sorted); i++ {
		for j := i + 1; j < len(sorted); j++ {
			if sorted[i] > sorted[j] {
				sorted[i], sorted[j] = sorted[j], sorted[i]
			}
		}
	}
	
	mid := len(sorted) / 2
	if len(sorted)%2 == 0 {
		return (sorted[mid-1] + sorted[mid]) / 2
	}
	return sorted[mid]
}

// Factorial calculates the factorial of n
func Factorial(n int) (int, error) {
	if n < 0 {
		return 0, errors.New("factorial is not defined for negative numbers")
	}
	if n == 0 || n == 1 {
		return 1, nil
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result, nil
}

// IsPrime checks if a number is prime
func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// GCD calculates the greatest common divisor
func GCD(a, b int) int {
	a = abs(a)
	b = abs(b)
	
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// LCM calculates the least common multiple
func LCM(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}
	return abs(a*b) / GCD(a, b)
}

// Abs returns the absolute value
func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

// Power calculates base^exponent
func Power(base, exponent int) int {
	if exponent == 0 {
		return 1
	}
	if exponent < 0 {
		return 0 // Integer division would give 0 anyway
	}
	
	result := 1
	for i := 0; i < exponent; i++ {
		result *= base
	}
	return result
}

// IsEven checks if a number is even
func IsEven(n int) bool {
	return n%2 == 0
}

// IsOdd checks if a number is odd
func IsOdd(n int) bool {
	return n%2 != 0
}
