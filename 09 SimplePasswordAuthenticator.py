# Simple Password Authenticator
# This script checks if the entered password matches the stored password.
Stored_Password = "Password123"

# User is prompted to enter their password
Input_Password = input("Enter your password: ")

# Check if the entered password matches the stored password
if Input_Password == Stored_Password:
    print("Access Granted")
else:
    print("Access Denied")