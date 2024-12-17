import random

def computer_guess():
    print("Welcome to the 'Guess the Number' game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, tell me if my guess is too high (H), too low (L), or correct (C).")

    low = 1
    high = 100
    feedback = ''
    attempts = 0

    while feedback != 'C':
        # Computer makes a guess
        if low != high:
            guess = random.randint(low, high)  # Random guess within the range
        else:
            guess = low

        attempts += 1
        print(f"My guess is {guess}.")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()

        # Adjust the range based on feedback
        if feedback == 'H':
            high = guess - 1  # Update upper bound
        elif feedback == 'L':
            low = guess + 1  # Update lower bound
        elif feedback != 'C':
            print("Invalid input. Please enter H, L, or C.")

    print(f"I guessed your number {guess} correctly in {attempts} attempts! Thanks for playing!")

# Run the game
computer_guess()