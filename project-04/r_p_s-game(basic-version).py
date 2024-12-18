import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

    # List of possible moves
    choices = ['rock', 'paper', 'scissors']

    while True:
        # Get user input
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(choices)
        print(f"The computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
play_game()