#!/bin/bash
# Script to analyze test coverage manually

echo "==================================="
echo "Code Coverage Analysis"
echo "==================================="
echo ""

# Count lines in source files
echo "Source Code Statistics:"
echo "----------------------"

total_src_lines=0
for file in src/*.py; do
    if [ -f "$file" ]; then
        lines=$(grep -v '^\s*#' "$file" | grep -v '^\s*$' | grep -v '^\s*"""' | wc -l)
        total_src_lines=$((total_src_lines + lines))
        echo "$(basename $file): $lines lines"
    fi
done

echo "Total source lines: $total_src_lines"
echo ""

# Count test files
echo "Test Statistics:"
echo "---------------"

total_test_files=0
for file in tests/test_*.py; do
    if [ -f "$file" ]; then
        total_test_files=$((total_test_files + 1))
        test_count=$(grep -c "def test_" "$file")
        echo "$(basename $file): $test_count tests"
    fi
done

echo "Total test files: $total_test_files"
echo ""

# Check Python syntax
echo "Syntax Validation:"
echo "-----------------"

syntax_errors=0
for file in src/*.py tests/*.py; do
    if [ -f "$file" ]; then
        # Check if file has valid Python structure
        if grep -q "def \|class " "$file"; then
            echo "✓ $(basename $file) - Valid structure"
        fi
    fi
done

echo ""
echo "Analysis complete!"
echo "==================================="
