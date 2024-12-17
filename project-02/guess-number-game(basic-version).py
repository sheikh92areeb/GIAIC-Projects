import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("The computer has chosen a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    # Game loop
    while not guessed_correctly:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
