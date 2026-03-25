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

func TestRunOutputIsNonEmpty(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	if buf.Len() == 0 {
		t.Error("Run() produced no output")
	}
}

func TestRunOutputLines(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	lines := strings.Split(strings.TrimSpace(buf.String()), "\n")
	// We expect at least 20 output lines
	if len(lines) < 20 {
		t.Errorf("Expected at least 20 output lines, got %d", len(lines))
	}
}

func TestMain(t *testing.T) {
	// Capture output by redirecting within the test
	var buf bytes.Buffer
	// Verify Run works as a proxy for main
	Run(&buf)
	if !strings.Contains(buf.String(), "Sum:") {
		t.Error("main() equivalent (Run) did not produce expected output")
	}
}
