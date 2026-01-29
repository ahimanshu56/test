package main

import "fmt"

func main() {
	fmt.Println("Coverage Demo Application")
	
	// Example usage
	userService := NewUserService()
	user, err := userService.CreateUser("test@example.com", "Test User", 25)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	
	fmt.Printf("Created user: %s (%s)\n", user.Name, user.Email)
}
