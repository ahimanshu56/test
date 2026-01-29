package main

import (
	"reflect"
	"testing"
)

func TestUnique(t *testing.T) {
	tests := []struct {
		input    []int
		expected []int
	}{
		{[]int{1, 2, 2, 3}, []int{1, 2, 3}},
		{[]int{1, 1, 1}, []int{1}},
		{[]int{}, []int{}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{5, 4, 3, 2, 1, 1, 2, 3}, []int{5, 4, 3, 2, 1}},
	}

	for _, tt := range tests {
		result := Unique(tt.input)
		if !reflect.DeepEqual(result, tt.expected) {
			t.Errorf("Unique(%v) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestChunk(t *testing.T) {
	tests := []struct {
		input       []int
		size        int
		expected    [][]int
		expectError bool
	}{
		{[]int{1, 2, 3, 4}, 2, [][]int{{1, 2}, {3, 4}}, false},
		{[]int{1, 2, 3, 4, 5}, 2, [][]int{{1, 2}, {3, 4}, {5}}, false},
		{[]int{1, 2, 3}, 5, [][]int{{1, 2, 3}}, false},
		{[]int{}, 2, [][]int{}, false},
		{[]int{1, 2, 3}, 0, nil, true},
		{[]int{1, 2, 3}, -1, nil, true},
		{[]int{1, 2, 3, 4, 5, 6}, 3, [][]int{{1, 2, 3}, {4, 5, 6}}, false},
	}

	for _, tt := range tests {
		result, err := Chunk(tt.input, tt.size)
		if tt.expectError {
			if err == nil {
				t.Errorf("Chunk(%v, %d) expected error, got nil", tt.input, tt.size)
			}
		} else {
			if err != nil {
				t.Errorf("Chunk(%v, %d) unexpected error: %v", tt.input, tt.size, err)
			}
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("Chunk(%v, %d) = %v, want %v", tt.input, tt.size, result, tt.expected)
			}
		}
	}
}

func TestFlatten(t *testing.T) {
	tests := []struct {
		input    [][]int
		expected []int
	}{
		{[][]int{{1, 2}, {3, 4}}, []int{1, 2, 3, 4}},
		{[][]int{{1}, {2}, {3}}, []int{1, 2, 3}},
		{[][]int{}, []int{}},
		{[][]int{{1, 2, 3}}, []int{1, 2, 3}},
		{[][]int{{}, {1}, {}}, []int{1}},
	}

	for _, tt := range tests {
		result := Flatten(tt.input)
		if !reflect.DeepEqual(result, tt.expected) {
			t.Errorf("Flatten(%v) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestSum(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{[]int{1, 2, 3, 4}, 10},
		{[]int{}, 0},
		{[]int{5}, 5},
		{[]int{-1, 1}, 0},
		{[]int{10, 20, 30}, 60},
	}

	for _, tt := range tests {
		result := Sum(tt.input)
		if result != tt.expected {
			t.Errorf("Sum(%v) = %d, want %d", tt.input, result, tt.expected)
		}
	}
}

func TestMax(t *testing.T) {
	tests := []struct {
		input       []int
		expected    int
		expectError bool
	}{
		{[]int{1, 2, 3, 4}, 4, false},
		{[]int{5}, 5, false},
		{[]int{-1, -5, -3}, -1, false},
		{[]int{}, 0, true},
		{[]int{10, 5, 20, 15}, 20, false},
	}

	for _, tt := range tests {
		result, err := Max(tt.input)
		if tt.expectError {
			if err == nil {
				t.Errorf("Max(%v) expected error, got nil", tt.input)
			}
		} else {
			if err != nil {
				t.Errorf("Max(%v) unexpected error: %v", tt.input, err)
			}
			if result != tt.expected {
				t.Errorf("Max(%v) = %d, want %d", tt.input, result, tt.expected)
			}
		}
	}
}

func TestMin(t *testing.T) {
	tests := []struct {
		input       []int
		expected    int
		expectError bool
	}{
		{[]int{1, 2, 3, 4}, 1, false},
		{[]int{5}, 5, false},
		{[]int{-1, -5, -3}, -5, false},
		{[]int{}, 0, true},
		{[]int{10, 5, 20, 15}, 5, false},
	}

	for _, tt := range tests {
		result, err := Min(tt.input)
		if tt.expectError {
			if err == nil {
				t.Errorf("Min(%v) expected error, got nil", tt.input)
			}
		} else {
			if err != nil {
				t.Errorf("Min(%v) unexpected error: %v", tt.input, err)
			}
			if result != tt.expected {
				t.Errorf("Min(%v) = %d, want %d", tt.input, result, tt.expected)
			}
		}
	}
}

func TestReverse(t *testing.T) {
	tests := []struct {
		input    []int
		expected []int
	}{
		{[]int{1, 2, 3, 4}, []int{4, 3, 2, 1}},
		{[]int{1}, []int{1}},
		{[]int{}, []int{}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
	}

	for _, tt := range tests {
		result := Reverse(tt.input)
		if !reflect.DeepEqual(result, tt.expected) {
			t.Errorf("Reverse(%v) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestFilter(t *testing.T) {
	isEven := func(n int) bool { return n%2 == 0 }
	isPositive := func(n int) bool { return n > 0 }

	tests := []struct {
		input     []int
		predicate func(int) bool
		expected  []int
	}{
		{[]int{1, 2, 3, 4, 5}, isEven, []int{2, 4}},
		{[]int{-2, -1, 0, 1, 2}, isPositive, []int{1, 2}},
		{[]int{}, isEven, []int{}},
		{[]int{1, 3, 5}, isEven, []int{}},
	}

	for _, tt := range tests {
		result := Filter(tt.input, tt.predicate)
		if !reflect.DeepEqual(result, tt.expected) {
			t.Errorf("Filter(%v) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestMap(t *testing.T) {
	double := func(n int) int { return n * 2 }
	square := func(n int) int { return n * n }

	tests := []struct {
		input    []int
		fn       func(int) int
		expected []int
	}{
		{[]int{1, 2, 3}, double, []int{2, 4, 6}},
		{[]int{2, 3, 4}, square, []int{4, 9, 16}},
		{[]int{}, double, []int{}},
	}

	for _, tt := range tests {
		result := Map(tt.input, tt.fn)
		if !reflect.DeepEqual(result, tt.expected) {
			t.Errorf("Map(%v) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}
