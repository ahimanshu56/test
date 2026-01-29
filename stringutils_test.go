package main

import "testing"

func TestCapitalize(t *testing.T) {
	tests := []struct {
		input    string
		expected string
	}{
		{"hello", "Hello"},
		{"HELLO", "Hello"},
		{"hELLO", "Hello"},
		{"", ""},
		{"a", "A"},
	}

	for _, tt := range tests {
		result := Capitalize(tt.input)
		if result != tt.expected {
			t.Errorf("Capitalize(%q) = %q, want %q", tt.input, result, tt.expected)
		}
	}
}

func TestTruncate(t *testing.T) {
	tests := []struct {
		input     string
		maxLength int
		expected  string
	}{
		{"hello world", 8, "hello..."},
		{"hello", 10, "hello"},
		{"hello", 5, "hello"},
		{"", 5, ""},
		{"hello world", 3, "..."},
		{"test", 2, "..."},
		{"a", 1, "a"},
	}

	for _, tt := range tests {
		result := Truncate(tt.input, tt.maxLength)
		if result != tt.expected {
			t.Errorf("Truncate(%q, %d) = %q, want %q", tt.input, tt.maxLength, result, tt.expected)
		}
	}
}

func TestSlugify(t *testing.T) {
	tests := []struct {
		input    string
		expected string
	}{
		{"Hello World", "hello-world"},
		{"Hello  World", "hello-world"},
		{"Hello_World", "hello-world"},
		{"Hello-World", "hello-world"},
		{"Hello@World!", "helloworld"},
		{"  Hello World  ", "hello-world"},
		{"---test---", "test"},
		{"", ""},
	}

	for _, tt := range tests {
		result := Slugify(tt.input)
		if result != tt.expected {
			t.Errorf("Slugify(%q) = %q, want %q", tt.input, result, tt.expected)
		}
	}
}

func TestIsEmail(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"test@example.com", true},
		{"user@domain.co.uk", true},
		{"invalid", false},
		{"@example.com", false},
		{"test@", false},
		{"test@.com", false},
		{"", false},
		{"test @example.com", false},
	}

	for _, tt := range tests {
		result := IsEmail(tt.input)
		if result != tt.expected {
			t.Errorf("IsEmail(%q) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestCountWords(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"hello world", 2},
		{"one", 1},
		{"", 0},
		{"  ", 0},
		{"one two three", 3},
		{"  hello   world  ", 2},
	}

	for _, tt := range tests {
		result := CountWords(tt.input)
		if result != tt.expected {
			t.Errorf("CountWords(%q) = %d, want %d", tt.input, result, tt.expected)
		}
	}
}

func TestReverseString(t *testing.T) {
	tests := []struct {
		input    string
		expected string
	}{
		{"hello", "olleh"},
		{"", ""},
		{"a", "a"},
		{"12345", "54321"},
		{"racecar", "racecar"},
	}

	for _, tt := range tests {
		result := ReverseString(tt.input)
		if result != tt.expected {
			t.Errorf("ReverseString(%q) = %q, want %q", tt.input, result, tt.expected)
		}
	}
}

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"racecar", true},
		{"hello", false},
		{"A man a plan a canal Panama", true},
		{"", true},
		{"a", true},
		{"Madam", true},
		{"test", false},
		{"12321", true},
		{"12345", false},
	}

	for _, tt := range tests {
		result := IsPalindrome(tt.input)
		if result != tt.expected {
			t.Errorf("IsPalindrome(%q) = %v, want %v", tt.input, result, tt.expected)
		}
	}
}

func TestContains(t *testing.T) {
	tests := []struct {
		str      string
		substr   string
		expected bool
	}{
		{"hello world", "world", true},
		{"hello world", "test", false},
		{"", "", true},
		{"test", "", true},
		{"", "test", false},
	}

	for _, tt := range tests {
		result := Contains(tt.str, tt.substr)
		if result != tt.expected {
			t.Errorf("Contains(%q, %q) = %v, want %v", tt.str, tt.substr, result, tt.expected)
		}
	}
}

func TestRepeat(t *testing.T) {
	tests := []struct {
		str      string
		n        int
		expected string
	}{
		{"a", 3, "aaa"},
		{"ab", 2, "abab"},
		{"test", 0, ""},
		{"x", -1, ""},
		{"", 5, ""},
	}

	for _, tt := range tests {
		result := Repeat(tt.str, tt.n)
		if result != tt.expected {
			t.Errorf("Repeat(%q, %d) = %q, want %q", tt.str, tt.n, result, tt.expected)
		}
	}
}
