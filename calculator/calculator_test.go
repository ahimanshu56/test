package calculator

import "testing"

func TestAdd(t *testing.T) {
	tests := []struct {
		a, b, expected int
	}{
		{2, 3, 5},
		{-1, 1, 0},
		{0, 0, 0},
		{100, 200, 300},
	}

	for _, tt := range tests {
		result := Add(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestSubtract(t *testing.T) {
	tests := []struct {
		a, b, expected int
	}{
		{5, 3, 2},
		{1, 1, 0},
		{0, 5, -5},
		{100, 50, 50},
	}

	for _, tt := range tests {
		result := Subtract(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Subtract(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestMultiply(t *testing.T) {
	tests := []struct {
		a, b, expected int
	}{
		{2, 3, 6},
		{-2, 3, -6},
		{0, 5, 0},
		{10, 10, 100},
	}

	for _, tt := range tests {
		result := Multiply(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Multiply(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestDivide(t *testing.T) {
	tests := []struct {
		a, b        int
		expected    int
		expectError bool
	}{
		{6, 2, 3, false},
		{10, 5, 2, false},
		{7, 2, 3, false},
		{10, 0, 0, true},
	}

	for _, tt := range tests {
		result, err := Divide(tt.a, tt.b)
		if tt.expectError {
			if err == nil {
				t.Errorf("Divide(%d, %d) expected error but got none", tt.a, tt.b)
			}
		} else {
			if err != nil {
				t.Errorf("Divide(%d, %d) unexpected error: %v", tt.a, tt.b, err)
			}
			if result != tt.expected {
				t.Errorf("Divide(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
			}
		}
	}
}

func TestIsEven(t *testing.T) {
	tests := []struct {
		n        int
		expected bool
	}{
		{2, true},
		{3, false},
		{0, true},
		{-4, true},
		{-5, false},
	}

	for _, tt := range tests {
		result := IsEven(tt.n)
		if result != tt.expected {
			t.Errorf("IsEven(%d) = %v; want %v", tt.n, result, tt.expected)
		}
	}
}

func TestMax(t *testing.T) {
	tests := []struct {
		a, b, expected int
	}{
		{5, 3, 5},
		{3, 5, 5},
		{5, 5, 5},
		{-1, -5, -1},
	}

	for _, tt := range tests {
		result := Max(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Max(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestMin(t *testing.T) {
	tests := []struct {
		a, b, expected int
	}{
		{5, 3, 3},
		{3, 5, 3},
		{5, 5, 5},
		{-1, -5, -5},
	}

	for _, tt := range tests {
		result := Min(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Min(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}

func TestAbs(t *testing.T) {
	tests := []struct {
		n, expected int
	}{
		{5, 5},
		{-5, 5},
		{0, 0},
		{-100, 100},
	}

	for _, tt := range tests {
		result := Abs(tt.n)
		if result != tt.expected {
			t.Errorf("Abs(%d) = %d; want %d", tt.n, result, tt.expected)
		}
	}
}

func TestPower(t *testing.T) {
	tests := []struct {
		base, exp, expected int
	}{
		{2, 3, 8},
		{5, 0, 1},
		{3, 2, 9},
		{10, 2, 100},
		{2, 10, 1024},
	}

	for _, tt := range tests {
		result := Power(tt.base, tt.exp)
		if result != tt.expected {
			t.Errorf("Power(%d, %d) = %d; want %d", tt.base, tt.exp, result, tt.expected)
		}
	}
}

func TestFactorial(t *testing.T) {
	tests := []struct {
		n, expected int
	}{
		{0, 1},
		{1, 1},
		{5, 120},
		{6, 720},
		{-1, -1},
	}

	for _, tt := range tests {
		result := Factorial(tt.n)
		if result != tt.expected {
			t.Errorf("Factorial(%d) = %d; want %d", tt.n, result, tt.expected)
		}
	}
}

