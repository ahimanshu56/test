package main

import (
	"bytes"
	"strings"
	"testing"
)

func TestRun(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)

	output := buf.String()

	// Check that output contains expected strings
	expectedStrings := []string{
		"Sum: 15",
		"Difference: 5",
		"Product: 50",
		"Quotient: 2",
		"Max: 10",
		"Min: 5",
		"Abs: 10",
		"Power: 8",
		"Factorial: 120",
		"IsEven: true",
		"Reversed: olleh",
		"Is palindrome: true",
		"Capitalized: Hello World",
		"Vowels: 2",
		"IsAlpha: true",
		"IsNumeric: true",
		"Contains: true",
		"No spaces: helloworld",
		"Word count: 3",
		"Trimmed: hello",
	}

	for _, expected := range expectedStrings {
		if !strings.Contains(output, expected) {
			t.Errorf("Output missing expected string: %q", expected)
		}
	}
}

func TestMainFunction(t *testing.T) {
	// Test that main function runs without panic by calling it directly.
	// main() calls Run(os.Stdout) which we already test via TestRun.
	defer func() {
		if r := recover(); r != nil {
			t.Errorf("main() panicked: %v", r)
		}
	}()
	main()
}

func TestRunOutput_NotEmpty(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	if buf.Len() == 0 {
		t.Error("Run() produced no output")
	}
}

func TestRunOutput_LineCount(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	lines := strings.Split(strings.TrimSpace(buf.String()), "\n")
	// We expect exactly 20 output lines (10 calculator + 10 string util)
	if len(lines) != 20 {
		t.Errorf("Run() produced %d lines; want 20", len(lines))
	}
}
