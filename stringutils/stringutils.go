package stringutils

import (
	"strings"
	"unicode"
)

// Reverse returns the reversed string
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome checks if a string is a palindrome
func IsPalindrome(s string) bool {
	s = strings.ToLower(s)
	left, right := 0, len(s)-1
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}

// Capitalize returns a string with the first letter of each word capitalized
func Capitalize(s string) string {
	return strings.Title(s)
}

// CountVowels counts the number of vowels in a string
func CountVowels(s string) int {
	vowels := "aeiouAEIOU"
	count := 0
	for _, char := range s {
		if strings.ContainsRune(vowels, char) {
			count++
		}
	}
	return count
}

// IsAlpha checks if a string contains only alphabetic characters
func IsAlpha(s string) bool {
	if len(s) == 0 {
		return false
	}
	for _, char := range s {
		if !unicode.IsLetter(char) {
			return false
		}
	}
	return true
}

// IsNumeric checks if a string contains only numeric characters
func IsNumeric(s string) bool {
	if len(s) == 0 {
		return false
	}
	for _, char := range s {
		if !unicode.IsDigit(char) {
			return false
		}
	}
	return true
}

// Contains checks if a string contains a substring
func Contains(s, substr string) bool {
	return strings.Contains(s, substr)
}

// RemoveSpaces removes all spaces from a string
func RemoveSpaces(s string) string {
	return strings.ReplaceAll(s, " ", "")
}

// WordCount returns the number of words in a string
func WordCount(s string) int {
	words := strings.Fields(s)
	return len(words)
}

// TrimString trims leading and trailing spaces
func TrimString(s string) string {
	return strings.TrimSpace(s)
}

