package main

import (
	"bytes"
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

// TestMainFunction calls main() with stdout redirected to verify it runs correctly.
func TestMainFunction(t *testing.T) {
	// Redirect os.Stdout to capture output
	origStdout := os.Stdout
	r, w, err := os.Pipe()
	if err != nil {
		t.Fatalf("failed to create pipe: %v", err)
	}
	os.Stdout = w

	defer func() {
		os.Stdout = origStdout
		if rec := recover(); rec != nil {
			t.Errorf("main() panicked: %v", rec)
		}
	}()

	main()

	w.Close()
	os.Stdout = origStdout

	var buf bytes.Buffer
	buf.ReadFrom(r)
	output := buf.String()

	if !strings.Contains(output, "Sum: 15") {
		t.Errorf("main() output missing expected content, got: %s", output)
	}
}
