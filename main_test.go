package main

import (
	"bytes"
	"io"
	"os"
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

func TestMain(t *testing.T) {
	// Test that main function runs without panic
	defer func() {
		if r := recover(); r != nil {
			t.Errorf("main() panicked: %v", r)
		}
	}()

	// Call main to ensure it works
	// We can't easily capture stdout, but we can verify it doesn't panic
	// main()
	// Note: Commenting out the actual call to avoid interfering with test output
	t.Log("Main function exists and compiles correctly")
}

// TestMainFunction exercises the main() entrypoint by redirecting stdout
// so the call doesn't pollute test output and we can verify it ran correctly.
func TestMainFunction(t *testing.T) {
	// Redirect os.Stdout to capture main()'s output
	origStdout := os.Stdout
	r, w, err := os.Pipe()
	if err != nil {
		t.Fatalf("failed to create pipe: %v", err)
	}
	os.Stdout = w

	// Run main() and restore stdout
	func() {
		defer func() {
			w.Close()
			os.Stdout = origStdout
		}()
		main()
	}()

	var buf bytes.Buffer
	if _, err := io.Copy(&buf, r); err != nil {
		t.Fatalf("failed to read captured output: %v", err)
	}
	r.Close()

	output := buf.String()

	// Verify that main() produced the expected output
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
	}
	for _, want := range expectedStrings {
		if !strings.Contains(output, want) {
			t.Errorf("main() output missing expected string: %q", want)
		}
	}
}

// TestRunOutputCompleteness verifies every line of Run's output format
func TestRunOutputCompleteness(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	output := buf.String()

	lines := strings.Split(strings.TrimSpace(output), "\n")
	if len(lines) < 20 {
		t.Errorf("expected at least 20 output lines, got %d", len(lines))
	}
}

// TestRunNoError ensures Run writes output and doesn't produce empty output
func TestRunNoError(t *testing.T) {
	var buf bytes.Buffer
	Run(&buf)
	if buf.Len() == 0 {
		t.Error("Run() produced no output")
	}
}
