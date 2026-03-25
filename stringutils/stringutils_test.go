package stringutils

import "testing"

func TestReverse(t *testing.T) {
	tests := []struct {
		input, expected string
	}{
		{"hello", "olleh"},
		{"", ""},
		{"a", "a"},
		{"racecar", "racecar"},
		{"Go", "oG"},
		{"12345", "54321"},
		{"Hello, World!", "!dlroW ,olleH"},
		{"ab", "ba"},
	}

	for _, tt := range tests {
		result := Reverse(tt.input)
		if result != tt.expected {
			t.Errorf("Reverse(%q) = %q; want %q", tt.input, result, tt.expected)
		}
	}
}

func TestReverseUnicode(t *testing.T) {
	// Test with unicode characters
	result := Reverse("h\u00e9llo")
	if len(result) == 0 {
		t.Error("Reverse of unicode string returned empty")
	}
}

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"racecar", true},
		{"hello", false},
		{"A", true},
		{"Aa", true},
		{"aba", true},
		{"abc", false},
		{"", true},
		{"abba", true},
		{"abcd", false},
		{"level", true},
	}

	for _, tt := range tests {
		result := IsPalindrome(tt.input)
		if result != tt.expected {
			t.Errorf("IsPalindrome(%q) = %v; want %v", tt.input, result, tt.expected)
		}
	}
}

func TestCapitalize(t *testing.T) {
	tests := []struct {
		input, expected string
	}{
		{"hello world", "Hello World"},
		{"go", "Go"},
		{"", ""},
		{"HELLO", "HELLO"},
		{"a b c", "A B C"},
		{"one two three", "One Two Three"},
	}

	for _, tt := range tests {
		result := Capitalize(tt.input)
		if result != tt.expected {
			t.Errorf("Capitalize(%q) = %q; want %q", tt.input, result, tt.expected)
		}
	}
}

func TestCountVowels(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"hello", 2},
		{"aeiou", 5},
		{"xyz", 0},
		{"", 0},
		{"AEIOU", 5},
		{"Hello World", 3},
		{"bcdfg", 0},
		{"a", 1},
		{"rhythm", 0},
		{"aAbBEeIiOoUu", 12},
	}

	for _, tt := range tests {
		result := CountVowels(tt.input)
		if result != tt.expected {
			t.Errorf("CountVowels(%q) = %d; want %d", tt.input, result, tt.expected)
		}
	}
}

func TestIsAlpha(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"hello", true},
		{"hello123", false},
		{"", false},
		{"ABC", true},
		{"hello world", false},
		{"a", true},
		{"Z", true},
		{"123", false},
		{"abc!", false},
	}

	for _, tt := range tests {
		result := IsAlpha(tt.input)
		if result != tt.expected {
			t.Errorf("IsAlpha(%q) = %v; want %v", tt.input, result, tt.expected)
		}
	}
}

func TestIsNumeric(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"123", true},
		{"hello", false},
		{"", false},
		{"123abc", false},
		{"0", true},
		{"9999", true},
		{"3.14", false},
		{"-1", false},
		{"00", true},
	}

	for _, tt := range tests {
		result := IsNumeric(tt.input)
		if result != tt.expected {
			t.Errorf("IsNumeric(%q) = %v; want %v", tt.input, result, tt.expected)
		}
	}
}

func TestContains(t *testing.T) {
	tests := []struct {
		s, substr string
		expected  bool
	}{
		{"hello world", "world", true},
		{"hello", "bye", false},
		{"", "", true},
		{"test", "", true},
		{"abcdef", "bcd", true},
		{"abcdef", "xyz", false},
		{"", "a", false},
		{"Hello", "hello", false}, // case sensitive
	}

	for _, tt := range tests {
		result := Contains(tt.s, tt.substr)
		if result != tt.expected {
			t.Errorf("Contains(%q, %q) = %v; want %v", tt.s, tt.substr, result, tt.expected)
		}
	}
}

func TestRemoveSpaces(t *testing.T) {
	tests := []struct {
		input, expected string
	}{
		{"hello world", "helloworld"},
		{"  test  ", "test"},
		{"", ""},
		{"nospaces", "nospaces"},
		{"a b c d e", "abcde"},
		{"   ", ""},
		{"h e l l o", "hello"},
	}

	for _, tt := range tests {
		result := RemoveSpaces(tt.input)
		if result != tt.expected {
			t.Errorf("RemoveSpaces(%q) = %q; want %q", tt.input, result, tt.expected)
		}
	}
}

func TestWordCount(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"hello world", 2},
		{"one", 1},
		{"", 0},
		{"  multiple   spaces  ", 2},
		{"one two three four", 4},
		{"   ", 0},
		{"a b c d e f", 6},
	}

	for _, tt := range tests {
		result := WordCount(tt.input)
		if result != tt.expected {
			t.Errorf("WordCount(%q) = %d; want %d", tt.input, result, tt.expected)
		}
	}
}

func TestTrimString(t *testing.T) {
	tests := []struct {
		input, expected string
	}{
		{"  hello  ", "hello"},
		{"test", "test"},
		{"", ""},
		{"  ", ""},
		{"\t\ntest\n\t", "test"},
		{"   leading", "leading"},
		{"trailing   ", "trailing"},
		{"\t\t\t", ""},
	}

	for _, tt := range tests {
		result := TrimString(tt.input)
		if result != tt.expected {
			t.Errorf("TrimString(%q) = %q; want %q", tt.input, result, tt.expected)
		}
	}
}
