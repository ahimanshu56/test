# Code Coverage Report

## Overall Coverage

| Metric | Value |
|--------|-------|
| **Before** | 99.1% (statements) |
| **After** | 100.0% (statements) |

---

## Package-Level Coverage

| Package | Before | After |
|---------|--------|-------|
| `github.com/test/code-coverage` (main) | 97.6% | 100.0% |
| `github.com/test/code-coverage/calculator` | 100.0% | 100.0% |
| `github.com/test/code-coverage/stringutils` | 100.0% | 100.0% |

---

## Files Modified / Created

| File | Change | Before | After |
|------|--------|--------|-------|
| `main_test.go` | Modified | 97.6% | 100.0% |

---

## Per-Function Coverage (After)

| Function | File | Coverage |
|----------|------|----------|
| `main` | `main.go` | 100.0% |
| `Run` | `main.go` | 100.0% |
| `Add` | `calculator/calculator.go` | 100.0% |
| `Subtract` | `calculator/calculator.go` | 100.0% |
| `Multiply` | `calculator/calculator.go` | 100.0% |
| `Divide` | `calculator/calculator.go` | 100.0% |
| `IsEven` | `calculator/calculator.go` | 100.0% |
| `Max` | `calculator/calculator.go` | 100.0% |
| `Min` | `calculator/calculator.go` | 100.0% |
| `Abs` | `calculator/calculator.go` | 100.0% |
| `Power` | `calculator/calculator.go` | 100.0% |
| `Factorial` | `calculator/calculator.go` | 100.0% |
| `Reverse` | `stringutils/stringutils.go` | 100.0% |
| `IsPalindrome` | `stringutils/stringutils.go` | 100.0% |
| `Capitalize` | `stringutils/stringutils.go` | 100.0% |
| `CountVowels` | `stringutils/stringutils.go` | 100.0% |
| `IsAlpha` | `stringutils/stringutils.go` | 100.0% |
| `IsNumeric` | `stringutils/stringutils.go` | 100.0% |
| `Contains` | `stringutils/stringutils.go` | 100.0% |
| `RemoveSpaces` | `stringutils/stringutils.go` | 100.0% |
| `WordCount` | `stringutils/stringutils.go` | 100.0% |
| `TrimString` | `stringutils/stringutils.go` | 100.0% |

---

## Key Improvements

- **`main()` function** in `main.go` was the only uncovered code (0% → 100%).
- Added `TestMainFunction` to `main_test.go` which:
  - Redirects `os.Stdout` via `os.Pipe()` to capture output.
  - Calls `main()` directly to exercise the entry point.
  - Verifies expected output strings are present.
- All 22 functions across 3 packages now have **100% statement coverage**.
- Target of ≥ 80% coverage exceeded — achieved **100%**.
