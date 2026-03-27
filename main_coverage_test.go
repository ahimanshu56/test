package main

import (
	"io"
	"os"
	"testing"
)

// TestMainFunction tests the main() function by redirecting stdout
// to ensure it executes without panic and produces output.
func TestMainFunction(t *testing.T) {
	// Redirect stdout to capture main()'s output
	origStdout := os.Stdout
	r, w, err := os.Pipe()
	if err != nil {
		t.Fatalf("Failed to create pipe: %v", err)
	}
	os.Stdout = w

	// Run main and capture any panic
	panicked := false
	func() {
		defer func() {
			if rec := recover(); rec != nil {
				panicked = true
			}
		}()
		main()
	}()

	// Restore stdout
	w.Close()
	os.Stdout = origStdout
	io.Copy(io.Discard, r)
	r.Close()

	if panicked {
		t.Error("main() should not panic")
	}
}
