package main

import (
	"fmt"
	"io"
	"os"

	"github.com/test/code-coverage/calculator"
	"github.com/test/code-coverage/stringutils"
)

// Run contains the main logic for easier testing
func Run(w io.Writer) {
	// Calculator operations
	sum := calculator.Add(10, 5)
	diff := calculator.Subtract(10, 5)
	product := calculator.Multiply(10, 5)
	quotient, _ := calculator.Divide(10, 5)
	max := calculator.Max(10, 5)
	min := calculator.Min(10, 5)
	abs := calculator.Abs(-10)
	power := calculator.Power(2, 3)
	factorial := calculator.Factorial(5)
	isEven := calculator.IsEven(4)

	fmt.Fprintf(w, "Sum: %d\n", sum)
	fmt.Fprintf(w, "Difference: %d\n", diff)
	fmt.Fprintf(w, "Product: %d\n", product)
	fmt.Fprintf(w, "Quotient: %d\n", quotient)
	fmt.Fprintf(w, "Max: %d\n", max)
	fmt.Fprintf(w, "Min: %d\n", min)
	fmt.Fprintf(w, "Abs: %d\n", abs)
	fmt.Fprintf(w, "Power: %d\n", power)
	fmt.Fprintf(w, "Factorial: %d\n", factorial)
	fmt.Fprintf(w, "IsEven: %v\n", isEven)

	// String operations
	reversed := stringutils.Reverse("hello")
	isPalin := stringutils.IsPalindrome("racecar")
	capitalized := stringutils.Capitalize("hello world")
	vowels := stringutils.CountVowels("hello")
	isAlpha := stringutils.IsAlpha("hello")
	isNumeric := stringutils.IsNumeric("12345")
	contains := stringutils.Contains("hello world", "world")
	noSpaces := stringutils.RemoveSpaces("hello world")
	wordCount := stringutils.WordCount("hello world test")
	trimmed := stringutils.TrimString("  hello  ")

	fmt.Fprintf(w, "Reversed: %s\n", reversed)
	fmt.Fprintf(w, "Is palindrome: %v\n", isPalin)
	fmt.Fprintf(w, "Capitalized: %s\n", capitalized)
	fmt.Fprintf(w, "Vowels: %d\n", vowels)
	fmt.Fprintf(w, "IsAlpha: %v\n", isAlpha)
	fmt.Fprintf(w, "IsNumeric: %v\n", isNumeric)
	fmt.Fprintf(w, "Contains: %v\n", contains)
	fmt.Fprintf(w, "No spaces: %s\n", noSpaces)
	fmt.Fprintf(w, "Word count: %d\n", wordCount)
	fmt.Fprintf(w, "Trimmed: %s\n", trimmed)
}

func main() {
	Run(os.Stdout)
}
