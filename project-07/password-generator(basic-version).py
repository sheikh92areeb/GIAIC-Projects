import random
import string

def generate_password(length):
    """Generates a random password of the given length."""
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    """Main function to generate multiple passwords."""
    try:
        # Get user input
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the desired password length: "))

        # Check for valid input
        if num_passwords < 1 or password_length < 1:
            print("Please enter positive integers for both inputs.")
            return

        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"{i+1}: {generate_password(password_length)}")
    except ValueError:
        print("Invalid input! Please enter integers for the number of passwords and their length.")

# Run the password generator
password_generator()