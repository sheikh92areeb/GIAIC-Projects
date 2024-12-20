import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        if num_passwords < 1 or password_length < 1:
            print("Please enter positive integers for both inputs.")
            return

        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"{i+1}: {generate_password(password_length, use_uppercase, use_numbers, use_symbols)}")
    except ValueError:
        print("Invalid input! Please enter integers for the number of passwords and their length.")

# Run the enhanced password generator
password_generator()