package main

import (
	"regexp"
	"strings"
)

// Capitalize returns a string with the first letter capitalized
func Capitalize(s string) string {
	if s == "" {
		return ""
	}
	return strings.ToUpper(s[:1]) + strings.ToLower(s[1:])
}

// Truncate shortens a string to maxLength, adding "..." if truncated
func Truncate(s string, maxLength int) string {
	if s == "" {
		return ""
	}
	if len(s) <= maxLength {
		return s
	}
	if maxLength <= 3 {
		return "..."
	}
	return s[:maxLength-3] + "..."
}

// Slugify converts a string to a URL-friendly slug
func Slugify(s string) string {
	s = strings.ToLower(s)
	s = strings.TrimSpace(s)
	
	// Remove non-alphanumeric characters except spaces and hyphens
	reg := regexp.MustCompile(`[^\w\s-]`)
	s = reg.ReplaceAllString(s, "")
	
	// Replace spaces and underscores with hyphens
	reg = regexp.MustCompile(`[\s_-]+`)
	s = reg.ReplaceAllString(s, "-")
	
	// Remove leading and trailing hyphens
	s = strings.Trim(s, "-")
	
	return s
}

// IsEmail checks if a string is a valid email format
func IsEmail(s string) bool {
	emailRegex := regexp.MustCompile(`^[^\s@]+@[^\s@]+\.[^\s@]+$`)
	return emailRegex.MatchString(s)
}

// CountWords returns the number of words in a string
func CountWords(s string) int {
	if s == "" {
		return 0
	}
	words := strings.Fields(s)
	return len(words)
}

// ReverseString reverses a string
func ReverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome checks if a string is a palindrome
func IsPalindrome(s string) bool {
	// Remove non-alphanumeric and convert to lowercase
	reg := regexp.MustCompile(`[^a-z0-9]`)
	cleaned := reg.ReplaceAllString(strings.ToLower(s), "")
	
	for i := 0; i < len(cleaned)/2; i++ {
		if cleaned[i] != cleaned[len(cleaned)-1-i] {
			return false
		}
	}
	return true
}

// Contains checks if a string contains a substring
func Contains(s, substr string) bool {
	return strings.Contains(s, substr)
}

// Repeat repeats a string n times
func Repeat(s string, n int) string {
	if n < 0 {
		return ""
	}
	return strings.Repeat(s, n)
}
