.PHONY: test coverage coverage-html run clean

# Run all tests
test:
	go test ./...

# Run tests with coverage summary
coverage:
	go test -cover ./...

# Generate detailed coverage report
coverage-report:
	go test -coverprofile=coverage.out ./...
	go tool cover -func=coverage.out

# Generate HTML coverage report
coverage-html:
	go test -coverprofile=coverage.out ./...
	go tool cover -html=coverage.out -o coverage.html
	@echo "Coverage report generated: coverage.html"

# Run the application
run:
	go run main.go

# Clean generated files
clean:
	rm -f coverage.out coverage.html

# Show coverage statistics
stats:
	@echo "=== Coverage Statistics ==="
	@go test -coverprofile=coverage.out ./... 2>&1 | grep coverage
	@echo ""
	@echo "=== Overall Coverage ==="
	@go tool cover -func=coverage.out | grep total

