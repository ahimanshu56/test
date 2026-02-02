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

func TestMainFunction(t *testing.T) {
	// Test that main function runs without panic
	// We redirect stdout temporarily to avoid polluting test output
	oldStdout := os.Stdout
	_, w, _ := os.Pipe()
	os.Stdout = w

	defer func() {
		w.Close()
		os.Stdout = oldStdout
		if r := recover(); r != nil {
			t.Errorf("main() panicked: %v", r)
		}
	}()

	// Call main in a goroutine to capture its output
	done := make(chan bool)
	go func() {
		defer func() {
			if r := recover(); r != nil {
				t.Errorf("main() panicked: %v", r)
			}
			done <- true
		}()
		main()
	}()

	<-done
}
