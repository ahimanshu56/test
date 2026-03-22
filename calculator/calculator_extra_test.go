package calculator

import (
	"testing"
)

// TestAddEdgeCases covers additional boundary conditions for Add
func TestAddEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
	}{
		{"large positive values", 1000000, 2000000, 3000000},
		{"large negative values", -1000000, -2000000, -3000000},
		{"overflow boundary zero sum", -5, 5, 0},
		{"identity with zero left", 0, 42, 42},
		{"identity with zero right", 42, 0, 42},
		{"both max-like positive", 999999, 1, 1000000},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Add(tt.a, tt.b); got != tt.expected {
				t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
			}
		})
	}
}

// TestSubtractEdgeCases covers additional boundary conditions for Subtract
func TestSubtractEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
	}{
		{"subtract self", 7, 7, 0},
		{"subtract larger from smaller", 3, 10, -7},
		{"subtract negative (becomes addition)", 5, -3, 8},
		{"subtract from zero", 0, 42, -42},
		{"zero minus zero", 0, 0, 0},
		{"large numbers", 1000000, 999999, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Subtract(tt.a, tt.b); got != tt.expected {
				t.Errorf("Subtract(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
			}
		})
	}
}

// TestMultiplyEdgeCases covers additional boundary conditions for Multiply
func TestMultiplyEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
	}{
		{"multiply by one", 99, 1, 99},
		{"multiply by minus one", 99, -1, -99},
		{"both negative", -4, -5, 20},
		{"zero times large", 0, 999999, 0},
		{"large times one", 999999, 1, 999999},
		{"identity 1x1", 1, 1, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Multiply(tt.a, tt.b); got != tt.expected {
				t.Errorf("Multiply(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
			}
		})
	}
}

// TestDivideEdgeCases covers additional boundary conditions for Divide
func TestDivideEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
		expectError bool
	}{
		{"divide by one", 100, 1, 100, false},
		{"divide by minus one", 100, -1, -100, false},
		{"negative dividend", -10, 2, -5, false},
		{"both negative", -10, -2, 5, false},
		{"zero dividend", 0, 5, 0, false},
		{"exact division", 81, 9, 9, false},
		{"integer truncation", 5, 2, 2, false},
		{"division by zero positive", 1, 0, 0, true},
		{"division by zero negative", -1, 0, 0, true},
		{"division by zero of zero", 0, 0, 0, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := Divide(tt.a, tt.b)
			if tt.expectError {
				if err == nil {
					t.Errorf("Divide(%d, %d) expected error, got nil", tt.a, tt.b)
				}
				if err != nil && err.Error() != "division by zero" {
					t.Errorf("Divide(%d, %d) unexpected error message: %v", tt.a, tt.b, err)
				}
			} else {
				if err != nil {
					t.Errorf("Divide(%d, %d) unexpected error: %v", tt.a, tt.b, err)
				}
				if got != tt.expected {
					t.Errorf("Divide(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
				}
			}
		})
	}
}

// TestIsEvenEdgeCases covers additional boundary conditions for IsEven
func TestIsEvenEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected bool
	}{
		{"zero is even", 0, true},
		{"one is odd", 1, false},
		{"minus two is even", -2, true},
		{"minus three is odd", -3, false},
		{"large even", 1000000, true},
		{"large odd", 999999, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := IsEven(tt.n); got != tt.expected {
				t.Errorf("IsEven(%d) = %v; want %v", tt.n, got, tt.expected)
			}
		})
	}
}

// TestMaxEdgeCases covers additional boundary conditions for Max
func TestMaxEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
	}{
		{"both zero", 0, 0, 0},
		{"both negative same", -5, -5, -5},
		{"first negative second positive", -1, 1, 1},
		{"first positive second negative", 1, -1, 1},
		{"large values", 1000000, 999999, 1000000},
		{"equal positive", 42, 42, 42},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Max(tt.a, tt.b); got != tt.expected {
				t.Errorf("Max(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
			}
		})
	}
}

// TestMinEdgeCases covers additional boundary conditions for Min
func TestMinEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		a, b        int
		expected    int
	}{
		{"both zero", 0, 0, 0},
		{"both negative same", -5, -5, -5},
		{"first negative second positive", -1, 1, -1},
		{"first positive second negative", 1, -1, -1},
		{"large values", 1000000, 999999, 999999},
		{"equal positive", 42, 42, 42},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Min(tt.a, tt.b); got != tt.expected {
				t.Errorf("Min(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
			}
		})
	}
}

// TestAbsEdgeCases covers additional boundary conditions for Abs
func TestAbsEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"zero", 0, 0},
		{"one", 1, 1},
		{"minus one", -1, 1},
		{"large positive", 1000000, 1000000},
		{"large negative", -1000000, 1000000},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Abs(tt.n); got != tt.expected {
				t.Errorf("Abs(%d) = %d; want %d", tt.n, got, tt.expected)
			}
		})
	}
}

// TestPowerEdgeCases covers additional boundary conditions for Power
func TestPowerEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		base, exp   int
		expected    int
	}{
		{"zero base positive exp", 0, 5, 0},
		{"one base any exp", 1, 100, 1},
		{"base zero exp zero", 0, 0, 1},
		{"negative base even exp", -2, 2, 4},
		{"negative base odd exp", -2, 3, -8},
		{"large exp", 2, 16, 65536},
		{"base 10 exp 3", 10, 3, 1000},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Power(tt.base, tt.exp); got != tt.expected {
				t.Errorf("Power(%d, %d) = %d; want %d", tt.base, tt.exp, got, tt.expected)
			}
		})
	}
}

// TestFactorialEdgeCases covers additional boundary conditions for Factorial
func TestFactorialEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"zero", 0, 1},
		{"one", 1, 1},
		{"two", 2, 2},
		{"three", 3, 6},
		{"four", 4, 24},
		{"ten", 10, 3628800},
		{"negative two", -2, -1},
		{"negative large", -100, -1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Factorial(tt.n); got != tt.expected {
				t.Errorf("Factorial(%d) = %d; want %d", tt.n, got, tt.expected)
			}
		})
	}
}
