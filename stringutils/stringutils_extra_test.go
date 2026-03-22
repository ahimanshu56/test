package stringutils

import (
	"testing"
)

// TestReverseEdgeCases covers additional boundary conditions for Reverse
func TestReverseEdgeCases(t *testing.T) {
	tests := []struct {
		name          string
		input         string
		expected      string
	}{
		{"single char", "x", "x"},
		{"two chars", "ab", "ba"},
		{"spaces", " ab ", " ba "},
		{"unicode multibyte", "h\u00e9llo", "oll\u00e9h"},
		{"all same chars", "aaaa", "aaaa"},
		{"digits", "12345", "54321"},
		{"whitespace only", "   ", "   "},
		{"newline", "a\nb", "b\na"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Reverse(tt.input); got != tt.expected {
				t.Errorf("Reverse(%q) = %q; want %q", tt.input, got, tt.expected)
			}
		})
	}
}

// TestIsPalindromeEdgeCases covers additional boundary conditions for IsPalindrome
func TestIsPalindromeEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{"empty string", "", true},
		{"single char", "z", true},
		{"two same chars", "aa", true},
		{"two different chars", "ab", false},
		{"all same chars", "aaaa", true},
		{"mixed case palindrome", "RaceCar", true},
		{"numeric palindrome", "12321", true},
		{"numeric non-palindrome", "12345", false},
		{"odd length palindrome", "abcba", true},
		{"even length palindrome", "abba", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := IsPalindrome(tt.input); got != tt.expected {
				t.Errorf("IsPalindrome(%q) = %v; want %v", tt.input, got, tt.expected)
			}
		})
	}
}

// TestCapitalizeEdgeCases covers additional boundary conditions for Capitalize
func TestCapitalizeEdgeCases(t *testing.T) {
	tests := []struct {
		name          string
		input         string
		expected      string
	}{
		{"single word lowercase", "hello", "Hello"},
		{"single word uppercase", "HELLO", "HELLO"},
		{"multiple words", "the quick brown fox", "The Quick Brown Fox"},
		{"mixed case", "hElLo wOrLd", "HElLo WOrLd"},
		{"leading space", " hello", " Hello"},
		{"empty string", "", ""},
		{"digits unchanged", "123 abc", "123 Abc"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Capitalize(tt.input); got != tt.expected {
				t.Errorf("Capitalize(%q) = %q; want %q", tt.input, got, tt.expected)
			}
		})
	}
}

// TestCountVowelsEdgeCases covers additional boundary conditions for CountVowels
func TestCountVowelsEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{"all consonants", "rhythm", 0},
		{"all vowels lowercase", "aeiou", 5},
		{"all vowels uppercase", "AEIOU", 5},
		{"mixed vowels and consonants", "beautiful", 5},
		{"single vowel", "a", 1},
		{"single consonant", "b", 0},
		{"number string", "12345", 0},
		{"spaces only", "   ", 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CountVowels(tt.input); got != tt.expected {
				t.Errorf("CountVowels(%q) = %d; want %d", tt.input, got, tt.expected)
			}
		})
	}
}

// TestIsAlphaEdgeCases covers additional boundary conditions for IsAlpha
func TestIsAlphaEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{"single letter", "a", true},
		{"single letter uppercase", "Z", true},
		{"only digits", "12345", false},
		{"only space", " ", false},
		{"letter then digit", "a1", false},
		{"digit then letter", "1a", false},
		{"punctuation", "hello!", false},
		{"tab character", "a\tb", false},
		{"newline", "a\n", false},
		{"long alpha string", "abcdefghijklmnopqrstuvwxyz", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := IsAlpha(tt.input); got != tt.expected {
				t.Errorf("IsAlpha(%q) = %v; want %v", tt.input, got, tt.expected)
			}
		})
	}
}

// TestIsNumericEdgeCases covers additional boundary conditions for IsNumeric
func TestIsNumericEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected bool
	}{
		{"single digit", "5", true},
		{"all zeros", "000", true},
		{"leading zero", "007", true},
		{"negative sign", "-5", false},
		{"decimal point", "3.14", false},
		{"space", " ", false},
		{"mixed", "12 34", false},
		{"long numeric", "1234567890", true},
		{"only letters", "abc", false},
		{"letter at end", "123a", false},
		{"letter at start", "a123", false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := IsNumeric(tt.input); got != tt.expected {
				t.Errorf("IsNumeric(%q) = %v; want %v", tt.input, got, tt.expected)
			}
		})
	}
}

// TestContainsEdgeCases covers additional boundary conditions for Contains
func TestContainsEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		substr   string
		expected bool
	}{
		{"empty contains empty", "", "", true},
		{"non-empty contains empty", "hello", "", true},
		{"empty contains non-empty", "", "a", false},
		{"exact match", "hello", "hello", true},
		{"longer substr", "hi", "hello", false},
		{"case sensitive miss", "Hello", "hello", false},
		{"single char present", "abcde", "c", true},
		{"single char absent", "abcde", "z", false},
		{"substr at start", "hello world", "hello", true},
		{"substr at end", "hello world", "world", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Contains(tt.s, tt.substr); got != tt.expected {
				t.Errorf("Contains(%q, %q) = %v; want %v", tt.s, tt.substr, got, tt.expected)
			}
		})
	}
}

// TestRemoveSpacesEdgeCases covers additional boundary conditions for RemoveSpaces
func TestRemoveSpacesEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected string
	}{
		{"no spaces", "hello", "hello"},
		{"all spaces", "   ", ""},
		{"single space", " ", ""},
		{"tabs not removed", "a\tb", "a\tb"},
		{"newlines not removed", "a\nb", "a\nb"},
		{"multiple spaces between", "a   b   c", "abc"},
		{"space at start only", " hello", "hello"},
		{"space at end only", "hello ", "hello"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RemoveSpaces(tt.input); got != tt.expected {
				t.Errorf("RemoveSpaces(%q) = %q; want %q", tt.input, got, tt.expected)
			}
		})
	}
}

// TestWordCountEdgeCases covers additional boundary conditions for WordCount
func TestWordCountEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected int
	}{
		{"empty string", "", 0},
		{"single word", "hello", 1},
		{"spaces only", "    ", 0},
		{"tabs as separator", "a\tb\tc", 3},
		{"newlines as separator", "a\nb\nc", 3},
		{"mixed whitespace", "a \t b \n c", 3},
		{"many words", "one two three four five", 5},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := WordCount(tt.input); got != tt.expected {
				t.Errorf("WordCount(%q) = %d; want %d", tt.input, got, tt.expected)
			}
		})
	}
}

// TestTrimStringEdgeCases covers additional boundary conditions for TrimString
func TestTrimStringEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected string
	}{
		{"no trim needed", "hello", "hello"},
		{"left trim only", "   hello", "hello"},
		{"right trim only", "hello   ", "hello"},
		{"both sides trim", "  hello  ", "hello"},
		{"tabs trimmed", "\thello\t", "hello"},
		{"newlines trimmed", "\nhello\n", "hello"},
		{"mixed whitespace", " \t\n hello \n\t ", "hello"},
		{"all whitespace", "    ", ""},
		{"empty string", "", ""},
		{"internal spaces preserved", "  hello world  ", "hello world"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := TrimString(tt.input); got != tt.expected {
				t.Errorf("TrimString(%q) = %q; want %q", tt.input, got, tt.expected)
			}
		})
	}
}
