package main

import "errors"

// Chunk splits a slice into chunks of specified size
func Chunk(slice []int, size int) ([][]int, error) {
	if size <= 0 {
		return nil, errors.New("chunk size must be positive")
	}
	
	chunks := [][]int{}
	for i := 0; i < len(slice); i += size {
		end := i + size
		if end > len(slice) {
			end = len(slice)
		}
		chunks = append(chunks, slice[i:end])
	}
	return chunks, nil
}

// Unique returns a slice with duplicate elements removed
func Unique(slice []int) []int {
	seen := make(map[int]bool)
	result := []int{}
	
	for _, val := range slice {
		if !seen[val] {
			seen[val] = true
			result = append(result, val)
		}
	}
	return result
}

// Flatten flattens a 2D slice into a 1D slice
func Flatten(slice [][]int) []int {
	result := []int{}
	for _, subSlice := range slice {
		result = append(result, subSlice...)
	}
	return result
}

// Sum returns the sum of all elements in a slice
func Sum(slice []int) int {
	total := 0
	for _, val := range slice {
		total += val
	}
	return total
}

// Max returns the maximum value in a slice
func Max(slice []int) (int, error) {
	if len(slice) == 0 {
		return 0, errors.New("slice is empty")
	}
	
	max := slice[0]
	for _, val := range slice[1:] {
		if val > max {
			max = val
		}
	}
	return max, nil
}

// Min returns the minimum value in a slice
func Min(slice []int) (int, error) {
	if len(slice) == 0 {
		return 0, errors.New("slice is empty")
	}
	
	min := slice[0]
	for _, val := range slice[1:] {
		if val < min {
			min = val
		}
	}
	return min, nil
}

// Reverse reverses a slice
func Reverse(slice []int) []int {
	result := make([]int, len(slice))
	for i, val := range slice {
		result[len(slice)-1-i] = val
	}
	return result
}

// Filter returns elements that satisfy the predicate
func Filter(slice []int, predicate func(int) bool) []int {
	result := []int{}
	for _, val := range slice {
		if predicate(val) {
			result = append(result, val)
		}
	}
	return result
}

// Map applies a function to each element
func Map(slice []int, fn func(int) int) []int {
	result := make([]int, len(slice))
	for i, val := range slice {
		result[i] = fn(val)
	}
	return result
}
