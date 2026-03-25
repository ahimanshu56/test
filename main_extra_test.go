package main

import (
	"os"
	"testing"
)

// TestMainFunction tests that the main() function executes without panicking.
// It temporarily redirects stdout so the output does not pollute test output.
func TestMainFunction(t *testing.T) {
	// Redirect stdout to /dev/null so main()'s output is suppressed.
	origStdout := os.Stdout
	devNull, err := os.Open(os.DevNull)
	if err != nil {
		t.Fatalf("failed to open /dev/null: %v", err)
	}
	os.Stdout = devNull
	defer func() {
		os.Stdout = origStdout
		devNull.Close()
	}()

	// Verify main() runs without panicking.
	defer func() {
		if r := recover(); r != nil {
			t.Errorf("main() panicked: %v", r)
		}
	}()

	main()
}
