package main

import (
	"testing"
)

func TestNewUserService(t *testing.T) {
	service := NewUserService()
	if service == nil {
		t.Error("NewUserService() returned nil")
	}
	if service.users == nil {
		t.Error("users map not initialized")
	}
}

func TestCreateUser(t *testing.T) {
	service := NewUserService()

	// Valid user creation
	user, err := service.CreateUser("test@example.com", "Test User", 25)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if user.Email != "test@example.com" {
		t.Errorf("Expected email 'test@example.com', got '%s'", user.Email)
	}
	if user.Name != "Test User" {
		t.Errorf("Expected name 'Test User', got '%s'", user.Name)
	}
	if user.Age != 25 {
		t.Errorf("Expected age 25, got %d", user.Age)
	}
	if !user.IsActive {
		t.Error("Expected user to be active")
	}

	// Test empty email
	_, err = service.CreateUser("", "Test", 25)
	if err == nil {
		t.Error("Expected error for empty email")
	}

	// Test empty name
	_, err = service.CreateUser("test@example.com", "", 25)
	if err == nil {
		t.Error("Expected error for empty name")
	}

	// Test invalid age (negative)
	_, err = service.CreateUser("test@example.com", "Test", -1)
	if err == nil {
		t.Error("Expected error for negative age")
	}

	// Test invalid age (too high)
	_, err = service.CreateUser("test@example.com", "Test", 151)
	if err == nil {
		t.Error("Expected error for age > 150")
	}

	// Test invalid email format
	_, err = service.CreateUser("invalid-email", "Test", 25)
	if err == nil {
		t.Error("Expected error for invalid email format")
	}

	// Test boundary ages
	_, err = service.CreateUser("test@example.com", "Test", 0)
	if err != nil {
		t.Errorf("Age 0 should be valid: %v", err)
	}

	_, err = service.CreateUser("test2@example.com", "Test", 150)
	if err != nil {
		t.Errorf("Age 150 should be valid: %v", err)
	}
}

func TestGetUserByID(t *testing.T) {
	service := NewUserService()
	user, _ := service.CreateUser("test@example.com", "Test User", 25)

	// Valid get
	found, err := service.GetUserByID(user.ID)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if found.ID != user.ID {
		t.Errorf("Expected user ID '%s', got '%s'", user.ID, found.ID)
	}

	// Non-existent user
	_, err = service.GetUserByID("nonexistent")
	if err == nil {
		t.Error("Expected error for non-existent user")
	}
}

func TestUpdateUser(t *testing.T) {
	service := NewUserService()
	user, _ := service.CreateUser("test@example.com", "Test User", 25)

	// Valid update
	updated, err := service.UpdateUser(user.ID, "new@example.com", "New Name", 30, false)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if updated.Email != "new@example.com" {
		t.Errorf("Expected email 'new@example.com', got '%s'", updated.Email)
	}
	if updated.Name != "New Name" {
		t.Errorf("Expected name 'New Name', got '%s'", updated.Name)
	}
	if updated.Age != 30 {
		t.Errorf("Expected age 30, got %d", updated.Age)
	}
	if updated.IsActive {
		t.Error("Expected user to be inactive")
	}

	// Update non-existent user
	_, err = service.UpdateUser("nonexistent", "test@example.com", "Test", 25, true)
	if err == nil {
		t.Error("Expected error for non-existent user")
	}

	// Invalid age
	_, err = service.UpdateUser(user.ID, "test@example.com", "Test", -1, true)
	if err == nil {
		t.Error("Expected error for negative age")
	}

	_, err = service.UpdateUser(user.ID, "test@example.com", "Test", 151, true)
	if err == nil {
		t.Error("Expected error for age > 150")
	}

	// Invalid email
	_, err = service.UpdateUser(user.ID, "invalid-email", "Test", 25, true)
	if err == nil {
		t.Error("Expected error for invalid email")
	}

	// Empty email should keep existing
	updated, err = service.UpdateUser(user.ID, "", "Another Name", 35, true)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if updated.Email != "new@example.com" {
		t.Error("Email should not change when empty string provided")
	}

	// Empty name should keep existing
	updated, err = service.UpdateUser(user.ID, "test3@example.com", "", 40, true)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if updated.Name != "Another Name" {
		t.Error("Name should not change when empty string provided")
	}
}

func TestDeleteUser(t *testing.T) {
	service := NewUserService()
	user, _ := service.CreateUser("test@example.com", "Test User", 25)

	// Valid delete
	err := service.DeleteUser(user.ID)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}

	// Verify user is deleted
	_, err = service.GetUserByID(user.ID)
	if err == nil {
		t.Error("User should be deleted")
	}

	// Delete non-existent user
	err = service.DeleteUser("nonexistent")
	if err == nil {
		t.Error("Expected error for non-existent user")
	}
}

func TestGetAllUsers(t *testing.T) {
	service := NewUserService()

	// Empty service
	users := service.GetAllUsers()
	if len(users) != 0 {
		t.Errorf("Expected 0 users, got %d", len(users))
	}

	// Add users
	service.CreateUser("test1@example.com", "User 1", 25)
	service.CreateUser("test2@example.com", "User 2", 30)
	service.CreateUser("test3@example.com", "User 3", 35)

	users = service.GetAllUsers()
	if len(users) != 3 {
		t.Errorf("Expected 3 users, got %d", len(users))
	}
}

func TestGetActiveUsers(t *testing.T) {
	service := NewUserService()

	user1, _ := service.CreateUser("test1@example.com", "User 1", 25)
	user2, _ := service.CreateUser("test2@example.com", "User 2", 30)
	service.CreateUser("test3@example.com", "User 3", 35)

	// Deactivate one user
	service.UpdateUser(user2.ID, "", "", 30, false)

	activeUsers := service.GetActiveUsers()
	if len(activeUsers) != 2 {
		t.Errorf("Expected 2 active users, got %d", len(activeUsers))
	}

	// Verify the inactive user is not in the list
	for _, user := range activeUsers {
		if user.ID == user2.ID {
			t.Error("Inactive user should not be in active users list")
		}
	}

	// Deactivate another
	service.UpdateUser(user1.ID, "", "", 25, false)
	activeUsers = service.GetActiveUsers()
	if len(activeUsers) != 1 {
		t.Errorf("Expected 1 active user, got %d", len(activeUsers))
	}
}

func TestGetUsersByAgeRange(t *testing.T) {
	service := NewUserService()

	service.CreateUser("test1@example.com", "User 1", 20)
	service.CreateUser("test2@example.com", "User 2", 30)
	service.CreateUser("test3@example.com", "User 3", 40)
	service.CreateUser("test4@example.com", "User 4", 50)

	// Test range
	users := service.GetUsersByAgeRange(25, 45)
	if len(users) != 2 {
		t.Errorf("Expected 2 users in range 25-45, got %d", len(users))
	}

	// Test exact boundaries
	users = service.GetUsersByAgeRange(30, 40)
	if len(users) != 2 {
		t.Errorf("Expected 2 users in range 30-40, got %d", len(users))
	}

	// Test no matches
	users = service.GetUsersByAgeRange(60, 70)
	if len(users) != 0 {
		t.Errorf("Expected 0 users in range 60-70, got %d", len(users))
	}

	// Test all users
	users = service.GetUsersByAgeRange(0, 150)
	if len(users) != 4 {
		t.Errorf("Expected 4 users in range 0-150, got %d", len(users))
	}
}

func TestSearchUsersByName(t *testing.T) {
	service := NewUserService()

	service.CreateUser("test1@example.com", "John Doe", 25)
	service.CreateUser("test2@example.com", "Jane Smith", 30)
	service.CreateUser("test3@example.com", "John Smith", 35)
	service.CreateUser("test4@example.com", "Bob Johnson", 40)

	// Search for "John"
	users := service.SearchUsersByName("John")
	if len(users) != 3 {
		t.Errorf("Expected 3 users with 'John', got %d", len(users))
	}

	// Search for "Smith"
	users = service.SearchUsersByName("Smith")
	if len(users) != 2 {
		t.Errorf("Expected 2 users with 'Smith', got %d", len(users))
	}

	// Search for non-existent
	users = service.SearchUsersByName("Nonexistent")
	if len(users) != 0 {
		t.Errorf("Expected 0 users with 'Nonexistent', got %d", len(users))
	}

	// Empty search
	users = service.SearchUsersByName("")
	if len(users) != 4 {
		t.Errorf("Expected 4 users with empty search, got %d", len(users))
	}
}

func TestCountUsers(t *testing.T) {
	service := NewUserService()

	// Empty service
	count := service.CountUsers()
	if count != 0 {
		t.Errorf("Expected 0 users, got %d", count)
	}

	// Add users
	service.CreateUser("test1@example.com", "User 1", 25)
	count = service.CountUsers()
	if count != 1 {
		t.Errorf("Expected 1 user, got %d", count)
	}

	service.CreateUser("test2@example.com", "User 2", 30)
	service.CreateUser("test3@example.com", "User 3", 35)
	count = service.CountUsers()
	if count != 3 {
		t.Errorf("Expected 3 users, got %d", count)
	}

	// Delete a user
	users := service.GetAllUsers()
	service.DeleteUser(users[0].ID)
	count = service.CountUsers()
	if count != 2 {
		t.Errorf("Expected 2 users after deletion, got %d", count)
	}
}
