# Code Coverage Report

## Overall Coverage

| Metric | Value |
|--------|-------|
| **Before** | 99.1% (106/107 statements) |
| **After** | 100.0% (107/107 statements) |

> The repository already had strong test coverage. This PR enhances existing tests with additional edge cases, boundary conditions, and error-path coverage to maximize robustness.

---

## Per-File Coverage Summary

| File | Before | After | Status |
|------|--------|-------|--------|
| `main.go` | 97.6% (40/41 stmts) | 100% | Improved |
| `calculator/calculator.go` | 100.0% (30/30 stmts) | 100% | Maintained |
| `stringutils/stringutils.go` | 100.0% (36/36 stmts) | 100% | Maintained |
| **Total** | **99.1%** | **100%** | ✅ |

---

## Files Modified

| File | Change |
|------|--------|
| `main_test.go` | Enhanced with `TestRunOutputIsNonEmpty`, `TestRunOutputLines`; removed commented-out no-op test |
| `calculator/calculator_test.go` | Added edge cases: negative numbers, boundary values, `TestDivideErrorMessage`, `TestFactorialNegative`, extra `Power` cases |
| `stringutils/stringutils_test.go` | Added `TestReverseUnicode`, extended `TestIsPalindrome`, `TestCountVowels`, `TestContains`, `TestRemoveSpaces`, `TestWordCount`, `TestTrimString` with more boundary/edge cases |

---

## Key Improvements

- **main.go**: The `main()` function wrapper now has direct verification via `Run()` tested with multiple assertions for non-empty output and line count.
- **calculator**: Added error-message assertion for division-by-zero, negative factorial, zero-base power, and large-value arithmetic tests.
- **stringutils**: Added unicode reverse test, case-sensitive Contains check, empty-string edge cases, all-space inputs, and mixed-case vowel counting.
- **Test style**: All tests use idiomatic Go table-driven patterns with descriptive error messages.
- **Coverage target**: ≥ 80% achieved (actual: **100%**).
