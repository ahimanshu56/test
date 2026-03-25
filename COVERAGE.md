# Code Coverage Report

## Overall Coverage: 99.1% → 100.0%

The repository had near-complete coverage before this run. The single uncovered statement was the `main()` entry-point in `main.go`, which was trivially tested by redirecting `os.Stdout` via a pipe and calling `main()` directly.

---

## Summary Table

| File | Before | After | Change |
|------|--------|-------|--------|
| `main.go` | 97.6% | 100.0% | +2.4% |
| `calculator/calculator.go` | 100.0% | 100.0% | — |
| `stringutils/stringutils.go` | 100.0% | 100.0% | — |
| **Total** | **99.1%** | **100.0%** | **+0.9%** |

---

## Files Modified

| File | Description |
|------|-------------|
| `main_test.go` | Added `TestMainFunction` to exercise the `main()` entry point |

---

## Key Improvements

- **`main.go` — `main()` function**: Was 0% covered (commented-out call in existing `TestMain`). Added `TestMainFunction` which:
  - Redirects `os.Stdout` to an `os.Pipe()` before calling `main()`
  - Restores `os.Stdout` after the call
  - Reads captured output and asserts expected content is present
  - Uses `defer`+`recover` to catch any panics

---

## Per-Function Coverage (After)

| Function | Coverage |
|----------|----------|
| `calculator.Add` | 100% |
| `calculator.Subtract` | 100% |
| `calculator.Multiply` | 100% |
| `calculator.Divide` | 100% |
| `calculator.IsEven` | 100% |
| `calculator.Max` | 100% |
| `calculator.Min` | 100% |
| `calculator.Abs` | 100% |
| `calculator.Power` | 100% |
| `calculator.Factorial` | 100% |
| `main.Run` | 100% |
| `main.main` | 100% |
| `stringutils.Reverse` | 100% |
| `stringutils.IsPalindrome` | 100% |
| `stringutils.Capitalize` | 100% |
| `stringutils.CountVowels` | 100% |
| `stringutils.IsAlpha` | 100% |
| `stringutils.IsNumeric` | 100% |
| `stringutils.Contains` | 100% |
| `stringutils.RemoveSpaces` | 100% |
| `stringutils.WordCount` | 100% |
| `stringutils.TrimString` | 100% |

---

## Test Strategy

- **Existing tests** were comprehensive table-driven tests covering happy paths, edge cases, boundary conditions, and error paths — all retained unchanged.
- **New test** (`TestMainFunction`) uses `os.Pipe` redirection to exercise the `main()` OS entry point without modifying production code.
