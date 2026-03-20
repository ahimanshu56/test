# Code Coverage Report

## Overall Coverage

| Metric | Value |
|--------|-------|
| **Before** | 99.1% |
| **After** | 100.0% |
| **Target** | ≥ 80% |
| **Status** | ✅ Target Exceeded |

---

## Per-File Coverage Summary

| File | Before | After | Change |
|------|--------|-------|--------|
| `main.go` | 97.6% (stmt) / `main()` 0% | 100.0% | +2.4% |
| `calculator/calculator.go` | 100.0% | 100.0% | — |
| `stringutils/stringutils.go` | 100.0% | 100.0% | — |

> **Note:** Per-package statement coverage: main package went from 97.6% → 100.0% because the `main()` function (0%) was not called in existing tests.

---

## Files Modified

| File | Action | Description |
|------|--------|-------------|
| `main_test.go` | Modified | Added `TestMainFunction`, `TestRunOutput_NotEmpty`, `TestRunOutput_LineCount` |

---

## Key Improvements

- **`main()` function** — Previously at 0% coverage. Added `TestMainFunction` which directly invokes `main()` with a panic-recovery guard.
- **Additional `Run()` tests** — Added `TestRunOutput_NotEmpty` (ensures output is non-empty) and `TestRunOutput_LineCount` (verifies exactly 20 lines of output are produced).
- **All packages now at 100%** — `calculator`, `stringutils`, and the root `main` package all report 100% statement coverage.

---

## Per-Function Coverage (After)

| Function | File | Coverage |
|----------|------|----------|
| `Add` | calculator/calculator.go | 100% |
| `Subtract` | calculator/calculator.go | 100% |
| `Multiply` | calculator/calculator.go | 100% |
| `Divide` | calculator/calculator.go | 100% |
| `IsEven` | calculator/calculator.go | 100% |
| `Max` | calculator/calculator.go | 100% |
| `Min` | calculator/calculator.go | 100% |
| `Abs` | calculator/calculator.go | 100% |
| `Power` | calculator/calculator.go | 100% |
| `Factorial` | calculator/calculator.go | 100% |
| `Run` | main.go | 100% |
| `main` | main.go | 100% |
| `Reverse` | stringutils/stringutils.go | 100% |
| `IsPalindrome` | stringutils/stringutils.go | 100% |
| `Capitalize` | stringutils/stringutils.go | 100% |
| `CountVowels` | stringutils/stringutils.go | 100% |
| `IsAlpha` | stringutils/stringutils.go | 100% |
| `IsNumeric` | stringutils/stringutils.go | 100% |
| `Contains` | stringutils/stringutils.go | 100% |
| `RemoveSpaces` | stringutils/stringutils.go | 100% |
| `WordCount` | stringutils/stringutils.go | 100% |
| `TrimString` | stringutils/stringutils.go | 100% |

---

## Test Strategy

- **Table-driven tests** used throughout all packages for systematic input coverage.
- **Edge cases** covered: zero values, negative numbers, empty strings, boundary conditions.
- **Error paths** tested: division by zero, negative factorial input.
- **No existing tests were deleted or modified** — only new tests were added.
