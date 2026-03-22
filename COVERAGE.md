# Code Coverage Report

## Overall Coverage

| Metric | Value |
|--------|-------|
| **Before** | 99.1% (statements) |
| **After** | **100.0%** (statements) |

> The `main()` entrypoint function was previously at 0% coverage; all other functions were already at 100%.

---

## Per-File Coverage Summary

| File | Before | After | Status |
|------|--------|-------|--------|
| `main.go` (`Run`) | 100.0% | 100.0% | ✅ |
| `main.go` (`main`) | 0.0% | **100.0%** | ✅ Improved |
| `calculator/calculator.go` | 100.0% | 100.0% | ✅ |
| `stringutils/stringutils.go` | 100.0% | 100.0% | ✅ |

---

## Files Created / Modified

| File | Type | Description |
|------|------|-------------|
| `main_test.go` | Modified | Added `TestMainFunction`, `TestRunOutputCompleteness`, `TestRunNoError` |
| `calculator/calculator_extra_test.go` | Created | Comprehensive edge-case tests for all 10 calculator functions |
| `stringutils/stringutils_extra_test.go` | Created | Comprehensive edge-case tests for all 10 string utility functions |

---

## Key Improvements

- **`main()` covered**: Added `TestMainFunction` that redirects `os.Stdout` via `os.Pipe()` to invoke `main()` directly and verify its output — bringing the function from **0% → 100%**.
- **Edge cases for `calculator` package**: Added `calculator_extra_test.go` with table-driven tests covering boundary values (zero, negatives, large numbers, integer truncation, division-by-zero error messages).
- **Edge cases for `stringutils` package**: Added `stringutils_extra_test.go` with table-driven tests covering Unicode handling, empty strings, whitespace variants (tabs, newlines), case sensitivity, and boundary lengths.
- **Total test functions added**: 23 new test functions with 150+ individual test cases.
- **Overall result**: **99.1% → 100.0%** — all 22 functions in the codebase are fully covered.
