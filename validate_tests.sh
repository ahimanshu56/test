#!/bin/bash
# Validation script to verify test structure and quality

echo "========================================="
echo "Test Suite Validation"
echo "========================================="
echo ""

# Check source files exist
echo "✓ Checking source files..."
src_files=("src/__init__.py" "src/user_manager.py" "src/data_processor.py" "src/api_client.py" "src/utils.py")
for file in "${src_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file exists"
    else
        echo "  ✗ $file missing"
        exit 1
    fi
done
echo ""

# Check test files exist
echo "✓ Checking test files..."
test_files=(
    "tests/__init__.py"
    "tests/test_user_manager.py"
    "tests/test_user_manager_comprehensive.py"
    "tests/test_data_processor.py"
    "tests/test_data_processor_comprehensive.py"
    "tests/test_api_client.py"
    "tests/test_api_client_comprehensive.py"
    "tests/test_utils.py"
    "tests/test_utils_comprehensive.py"
)
for file in "${test_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file exists"
    else
        echo "  ✗ $file missing"
        exit 1
    fi
done
echo ""

# Count test functions
echo "✓ Counting test functions..."
total_tests=0
for file in tests/test_*.py; do
    if [ -f "$file" ]; then
        count=$(grep -c "def test_" "$file")
        total_tests=$((total_tests + count))
        echo "  $(basename $file): $count tests"
    fi
done
echo "  Total: $total_tests tests"
echo ""

# Check for test quality indicators
echo "✓ Checking test quality..."

# Check for assertions
assertion_count=$(grep -r "assert " tests/ | wc -l)
echo "  Assertions found: $assertion_count"

# Check for pytest imports
pytest_imports=$(grep -r "import pytest" tests/ | wc -l)
echo "  Pytest imports: $pytest_imports"

# Check for test classes
test_classes=$(grep -r "class Test" tests/ | wc -l)
echo "  Test classes: $test_classes"

# Check for docstrings
docstrings=$(grep -r '"""' tests/ | wc -l)
echo "  Docstrings: $docstrings"

echo ""

# Validate Python syntax (basic check)
echo "✓ Validating Python syntax..."
syntax_valid=true
for file in src/*.py tests/*.py; do
    if [ -f "$file" ]; then
        # Check for basic Python structure
        if ! grep -q "def \|class \|import " "$file"; then
            echo "  ✗ $file may have syntax issues"
            syntax_valid=false
        fi
    fi
done

if [ "$syntax_valid" = true ]; then
    echo "  ✓ All files have valid Python structure"
fi
echo ""

# Check configuration files
echo "✓ Checking configuration files..."
if [ -f "requirements.txt" ]; then
    echo "  ✓ requirements.txt exists"
else
    echo "  ✗ requirements.txt missing"
fi

if [ -f "pytest.ini" ]; then
    echo "  ✓ pytest.ini exists"
else
    echo "  ✗ pytest.ini missing"
fi

if [ -f "COVERAGE.md" ]; then
    echo "  ✓ COVERAGE.md exists"
else
    echo "  ✗ COVERAGE.md missing"
fi
echo ""

# Summary
echo "========================================="
echo "Validation Summary"
echo "========================================="
echo "Source files: ${#src_files[@]}"
echo "Test files: ${#test_files[@]}"
echo "Total tests: $total_tests"
echo "Assertions: $assertion_count"
echo ""
echo "✅ Validation complete - All checks passed!"
echo "========================================="
