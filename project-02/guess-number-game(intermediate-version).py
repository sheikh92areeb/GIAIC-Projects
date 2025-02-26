import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")

    while True:
        # Ask for difficulty level
        print("\nChoose a difficulty level:")
        print("1. Easy (1 to 50)")
        print("2. Medium (1 to 100)")
        print("3. Hard (1 to 200)")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                max_number = 50
            elif choice == 2:
                max_number = 100
            elif choice == 3:
                max_number = 200
            else:
                print("Invalid choice. Defaulting to Medium difficulty.")
                max_number = 100
        except ValueError:
            print("Invalid input. Defaulting to Medium difficulty.")
            max_number = 100

        # Generate the random number
        number_to_guess = random.randint(1, max_number)
        attempts = 0
        guessed_correctly = False

        print(f"\nThe computer has chosen a number between 1 and {max_number}. Can you guess it?")

        # Game loop
        while not guessed_correctly:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    guessed_correctly = True
            except ValueError:
                print("Please enter a valid number.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
guess_the_number()
