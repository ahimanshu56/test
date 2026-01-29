package main

import (
	"math"
	"testing"
)

func TestClamp(t *testing.T) {
	tests := []struct {
		value    float64
		min      float64
		max      float64
		expected float64
	}{
		{5.0, 0.0, 10.0, 5.0},
		{-5.0, 0.0, 10.0, 0.0},
		{15.0, 0.0, 10.0, 10.0},
		{5.0, 5.0, 5.0, 5.0},
		{3.5, 2.0, 8.0, 3.5},
	}

	for _, tt := range tests {
		result := Clamp(tt.value, tt.min, tt.max)
		if result != tt.expected {
			t.Errorf("Clamp(%f, %f, %f) = %f, want %f", tt.value, tt.min, tt.max, result, tt.expected)
		}
	}
}

func TestAverage(t *testing.T) {
	tests := []struct {
		input    []float64
		expected float64
	}{
		{[]float64{1.0, 2.0, 3.0}, 2.0},
		{[]float64{5.0}, 5.0},
		{[]float64{}, 0.0},
		{[]float64{10.0, 20.0, 30.0}, 20.0},
		{[]float64{-5.0, 5.0}, 0.0},
	}

	for _, tt := range tests {
		result := Average(tt.input)
		if result != tt.expected {
			t.Errorf("Average(%v) = %f, want %f", tt.input, result, tt.expected)
		}
	}
}

func TestMedian(t *testing.T) {
	tests := []struct {
		input    []float64
		expected float64
	}{
		{[]float64{1.0, 2.0, 3.0}, 2.0},
		{[]float64{1.0, 2.0, 3.0, 4.0}, 2.5},
		{[]float64{5.0}, 5.0},
		{[]float64{}, 0.0},
		{[]float64{3.0, 1.0, 2.0}, 2.0},
		{[]float64{4.0, 1.0, 3.0, 2.0}, 2.5},
	}

	for _, tt := range tests {
		result := Median(tt.input)
		if result != tt.expected {
			t.Errorf("Median(%v) = %f, want %f", tt.input, result, tt.expected)
		}
	}
}

func TestFactorial(t *testing.T) {
	tests := []struct {
		input       int
		expected    int
		expectError bool
	}{
		{0, 1, false},
		{1, 1, false},
		{5, 120, false},
		{10, 3628800, false},
		{-1, 0, true},
		{3, 6, false},
	}

	for _, tt := range tests {
		result, err := Factorial(tt.input)
		if tt.expectError {
			if err == nil {
				t.Errorf("Factorial(%d) expected error, got nil", tt.input)
			}
		} else {
			if err != nil {
				t.Errorf("Factorial(%d) unexpected error: %v", tt.input, err)
			}
			if result != tt.expected {
				t.Errorf("Factorial(%d) = %d, want %d", tt.input, result, tt.expected)
			}
		}
	}
}

func TestIsPrime(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{2, true},
		{3, true},
		{4, false},
		{5, true},
		{17, true},
		{20, false},
		{1, false},
		{0, false},
		{-5, false},
		{97, true},
		{100, false},
	}

	for _, tt := range tests {
		result := IsPrime(tt.input)
		if result != tt.expected {
			t.Errorf("IsPrime(%d) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestGCD(t *testing.T) {
	tests := []struct {
		a        int
		b        int
		expected int
	}{
		{12, 8, 4},
		{15, 25, 5},
		{7, 13, 1},
		{0, 5, 5},
		{5, 0, 5},
		{-12, 8, 4},
		{12, -8, 4},
		{100, 50, 50},
	}

	for _, tt := range tests {
		result := GCD(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("GCD(%d, %d) = %d, want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestLCM(t *testing.T) {
	tests := []struct {
		a        int
		b        int
		expected int
	}{
		{4, 6, 12},
		{3, 5, 15},
		{12, 8, 24},
		{0, 5, 0},
		{5, 0, 0},
		{7, 7, 7},
	}

	for _, tt := range tests {
		result := LCM(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("LCM(%d, %d) = %d, want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestAbs(t *testing.T) {
	tests := []struct {
		input    int
		expected int
	}{
		{5, 5},
		{-5, 5},
		{0, 0},
		{-100, 100},
	}

	for _, tt := range tests {
		result := abs(tt.input)
		if result != tt.expected {
			t.Errorf("abs(%d) = %d, want %d", tt.input, result, tt.expected)
		}
	}
}

func TestPower(t *testing.T) {
	tests := []struct {
		base     int
		exponent int
		expected int
	}{
		{2, 3, 8},
		{5, 0, 1},
		{3, 2, 9},
		{10, 3, 1000},
		{2, -1, 0},
		{0, 5, 0},
		{7, 1, 7},
	}

	for _, tt := range tests {
		result := Power(tt.base, tt.exponent)
		if result != tt.expected {
			t.Errorf("Power(%d, %d) = %d, want %d", tt.base, tt.exponent, result, tt.expected)
		}
	}
}

func TestIsEven(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{2, true},
		{3, false},
		{0, true},
		{-2, true},
		{-3, false},
		{100, true},
		{101, false},
	}

	for _, tt := range tests {
		result := IsEven(tt.input)
		if result != tt.expected {
			t.Errorf("IsEven(%d) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestIsOdd(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{2, false},
		{3, true},
		{0, false},
		{-2, false},
		{-3, true},
		{100, false},
		{101, true},
	}

	for _, tt := range tests {
		result := IsOdd(tt.input)
		if result != tt.expected {
			t.Errorf("IsOdd(%d) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

// Helper function to compare floats with tolerance
func floatEquals(a, b, tolerance float64) bool {
	return math.Abs(a-b) < tolerance
}
