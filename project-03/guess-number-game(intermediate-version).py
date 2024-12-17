import random

def computer_guess():
    print("Welcome to the 'Guess the Number' game!")
    print("Now set the range of number")

    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    print(f"Think of a number between {low} and {high}, and I'll try to guess it.")
    print("After each guess, tell me if my guess is too high (H), too low (L), or correct (C).")

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