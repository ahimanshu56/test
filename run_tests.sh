#!/bin/bash

# Test Runner Script
# This script runs the comprehensive test suite and generates coverage reports

echo "========================================="
echo "Running Comprehensive Test Suite"
echo "========================================="
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "Installing test dependencies..."
    pip install -q pytest pytest-cov pytest-mock
fi

echo "Test Configuration:"
echo "  Framework: pytest 7.4.3"
echo "  Coverage Tool: pytest-cov 4.1.0"
echo "  Source Directory: src/"
echo "  Test Directory: tests/"
echo ""

echo "Running tests with coverage..."
echo ""

# Run tests with coverage
pytest tests/ \
    --cov=src \
    --cov-report=html \
    --cov-report=term \
    --cov-report=json \
    -v \
    --tb=short

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "✅ All Tests Passed Successfully!"
    echo "========================================="
    echo ""
    echo "Coverage reports generated:"
    echo "  - HTML: htmlcov/index.html"
    echo "  - JSON: coverage.json"
    echo "  - Terminal: (displayed above)"
    echo ""
    echo "To view HTML coverage report:"
    echo "  open htmlcov/index.html"
    echo ""
else
    echo ""
    echo "========================================="
    echo "❌ Some Tests Failed"
    echo "========================================="
    echo ""
    exit 1
fi
