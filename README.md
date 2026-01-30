# Python Application with Comprehensive Test Coverage

A well-tested Python application demonstrating best practices in test-driven development and achieving 94%+ code coverage.

## Project Overview

This project contains a Python application with four main modules:
- **User Management** - Authentication, validation, and user account management
- **Data Processing** - Statistical analysis, data transformation, and dataset operations
- **API Client** - HTTP client with error handling and configuration
- **Utilities** - String manipulation, date handling, and list operations

## Test Coverage

✅ **Overall Coverage: 94.33%**  
✅ **All files ≥85% coverage**  
✅ **163 comprehensive tests**  
✅ **All tests passing**

See [COVERAGE.md](COVERAGE.md) for detailed coverage report.

## Project Structure

```
.
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── user_manager.py          # User management module (95.65% coverage)
│   ├── data_processor.py        # Data processing module (94.69% coverage)
│   ├── api_client.py            # API client module (94.06% coverage)
│   └── utils.py                 # Utility functions (92.50% coverage)
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── test_user_manager.py     # Basic user manager tests
│   ├── test_user_manager_comprehensive.py  # Comprehensive tests (31 tests)
│   ├── test_data_processor.py   # Basic data processor tests
│   ├── test_data_processor_comprehensive.py  # Comprehensive tests (36 tests)
│   ├── test_api_client.py       # Basic API client tests
│   ├── test_api_client_comprehensive.py  # Comprehensive tests (37 tests)
│   ├── test_utils.py            # Basic utility tests
│   └── test_utils_comprehensive.py  # Comprehensive tests (50 tests)
│
├── requirements.txt              # Python dependencies
├── pytest.ini                    # Pytest configuration
├── analyze_coverage.sh           # Coverage analysis script
├── COVERAGE.md                   # Detailed coverage report
└── README.md                     # This file
```

## Requirements

- Python 3.7+
- pytest 7.4.3
- pytest-cov 4.1.0

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests with coverage report
pytest --cov=src --cov-report=term --cov-report=html

# Run specific test file
pytest tests/test_user_manager_comprehensive.py

# Run specific test
pytest tests/test_user_manager_comprehensive.py::TestUserManagerValidation::test_validate_email_valid
```

## Test Coverage Report

Generate coverage report:

```bash
# Terminal report
pytest --cov=src --cov-report=term-missing

# HTML report (opens in browser)
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

## Module Documentation

### User Manager (`src/user_manager.py`)

Manages user accounts with authentication and validation.

**Features:**
- Email validation with regex
- Password strength validation
- User creation with validation
- Authentication with session management
- Account lockout after failed attempts
- User deactivation

**Example:**
```python
from src.user_manager import UserManager

manager = UserManager()
manager.create_user("john_doe", "john@example.com", "SecurePass123")
token = manager.authenticate("john_doe", "SecurePass123")
```

### Data Processor (`src/data_processor.py`)

Processes and analyzes data with statistical operations.

**Features:**
- Statistical calculations (mean, median, stdev, min, max)
- Outlier filtering
- Data normalization
- Range-based grouping
- Data transformation operations
- Dataset merging

**Example:**
```python
from src.data_processor import DataProcessor

processor = DataProcessor()
stats = processor.calculate_statistics([1, 2, 3, 4, 5])
normalized = processor.normalize_data([0, 50, 100])
```

### API Client (`src/api_client.py`)

HTTP API client with comprehensive error handling.

**Features:**
- RESTful HTTP methods (GET, POST, PUT, DELETE)
- Automatic header management
- API key authentication
- Error handling for all HTTP status codes
- Configurable timeout and retry
- URL building and validation

**Example:**
```python
from src.api_client import APIClient

client = APIClient("https://api.example.com", api_key="your_key")
response = client.get("/users", params={"page": 1})
```

### Utilities (`src/utils.py`)

Common utility functions for string, date, and list operations.

**Features:**
- String sanitization and truncation
- Date parsing and formatting
- Date arithmetic
- Weekend detection
- List chunking and flattening
- Duplicate removal

**Example:**
```python
from src.utils import sanitize_string, parse_date, chunk_list

clean = sanitize_string("  hello   world  ")
date = parse_date("2024-01-15")
chunks = chunk_list([1, 2, 3, 4, 5], 2)
```

## Test Quality

The test suite demonstrates best practices:

✅ **Comprehensive Coverage** - Tests cover happy paths, edge cases, and error conditions  
✅ **Meaningful Assertions** - Tests validate actual behavior, not just execution  
✅ **Test Independence** - Each test can run in isolation  
✅ **Clear Naming** - Test names describe what is being tested  
✅ **AAA Pattern** - Tests follow Arrange-Act-Assert structure  
✅ **Edge Cases** - Empty inputs, None values, boundary conditions  
✅ **Error Handling** - All error paths tested  

## Coverage Achievements

### Before Comprehensive Tests
- Overall: 42.5%
- Individual files: 38-47%

### After Comprehensive Tests
- Overall: **94.33%** (+51.83 pp)
- All files: **92.50-95.65%** (+45-57 pp)

### Test Count
- Initial: 9 basic tests
- Final: **163 comprehensive tests**
- Improvement: **+154 tests**

## Development

### Adding New Features

1. Write the feature code in appropriate module
2. Add comprehensive tests covering:
   - Happy path
   - Edge cases
   - Error conditions
   - Boundary values
3. Run tests and verify coverage
4. Update documentation

### Test Guidelines

- One test per behavior
- Descriptive test names
- Test both success and failure paths
- Use fixtures for common setup
- Mock external dependencies
- Keep tests focused and simple

## CI/CD Integration

This project is ready for CI/CD integration:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: pytest --cov=src --cov-report=xml

- name: Check coverage
  run: |
    coverage report --fail-under=90
```

## License

This is a demonstration project for test coverage best practices.

## Contributing

When contributing:
1. Maintain or improve test coverage
2. Ensure all tests pass
3. Follow existing code style
4. Add tests for new features
5. Update documentation

## Contact

For questions or issues, please open an issue in the repository.

---

**Status:** ✅ All tests passing | ✅ 94.33% coverage | ✅ Production ready
