#Break statement examples.

# Break statement example with for loop.
# The loop iterates through a list of names and stops when it finds a specific name.
names = ["Alice", "Bob", "Charlie", "David"]
name_to_find = "Charlie"

# Iterate through the list of names
for name in names:
    print(f"Checking name: {name}")
    if name == name_to_find:
        print(f"Found {name_to_find}! Exiting loop.")
        break  # Exit the loop when the name is found
print("Loop has ended.")

# Break statement example with while loop.
# The loop continues to prompt the user for input until they enter 'exit'.
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop when the user types 'exit'
    print(f"You entered: {user_input}")