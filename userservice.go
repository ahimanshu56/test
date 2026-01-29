package main

import (
	"errors"
	"fmt"
	"time"
)

// User represents a user in the system
type User struct {
	ID        string
	Email     string
	Name      string
	Age       int
	IsActive  bool
	CreatedAt time.Time
}

// UserService manages user operations
type UserService struct {
	users map[string]*User
	idCounter int
}

// NewUserService creates a new UserService
func NewUserService() *UserService {
	return &UserService{
		users: make(map[string]*User),
		idCounter: 1,
	}
}

// CreateUser creates a new user
func (s *UserService) CreateUser(email, name string, age int) (*User, error) {
	if email == "" || name == "" {
		return nil, errors.New("email and name are required")
	}
	if age < 0 || age > 150 {
		return nil, errors.New("invalid age")
	}
	if !IsEmail(email) {
		return nil, errors.New("invalid email format")
	}
	
	id := fmt.Sprintf("user_%d", s.idCounter)
	s.idCounter++
	
	user := &User{
		ID:        id,
		Email:     email,
		Name:      name,
		Age:       age,
		IsActive:  true,
		CreatedAt: time.Now(),
	}
	
	s.users[id] = user
	return user, nil
}

// GetUserByID retrieves a user by ID
func (s *UserService) GetUserByID(id string) (*User, error) {
	user, exists := s.users[id]
	if !exists {
		return nil, errors.New("user not found")
	}
	return user, nil
}

// UpdateUser updates user information
func (s *UserService) UpdateUser(id string, email, name string, age int, isActive bool) (*User, error) {
	user, exists := s.users[id]
	if !exists {
		return nil, errors.New("user not found")
	}
	
	if age < 0 || age > 150 {
		return nil, errors.New("invalid age")
	}
	if email != "" && !IsEmail(email) {
		return nil, errors.New("invalid email format")
	}
	
	if email != "" {
		user.Email = email
	}
	if name != "" {
		user.Name = name
	}
	user.Age = age
	user.IsActive = isActive
	
	return user, nil
}

// DeleteUser removes a user
func (s *UserService) DeleteUser(id string) error {
	if _, exists := s.users[id]; !exists {
		return errors.New("user not found")
	}
	delete(s.users, id)
	return nil
}

// GetAllUsers returns all users
func (s *UserService) GetAllUsers() []*User {
	users := make([]*User, 0, len(s.users))
	for _, user := range s.users {
		users = append(users, user)
	}
	return users
}

// GetActiveUsers returns only active users
func (s *UserService) GetActiveUsers() []*User {
	users := []*User{}
	for _, user := range s.users {
		if user.IsActive {
			users = append(users, user)
		}
	}
	return users
}

// GetUsersByAgeRange returns users within an age range
func (s *UserService) GetUsersByAgeRange(minAge, maxAge int) []*User {
	users := []*User{}
	for _, user := range s.users {
		if user.Age >= minAge && user.Age <= maxAge {
			users = append(users, user)
		}
	}
	return users
}

// SearchUsersByName searches users by name
func (s *UserService) SearchUsersByName(query string) []*User {
	users := []*User{}
	for _, user := range s.users {
		if Contains(user.Name, query) {
			users = append(users, user)
		}
	}
	return users
}

// CountUsers returns the total number of users
func (s *UserService) CountUsers() int {
	return len(s.users)
}
