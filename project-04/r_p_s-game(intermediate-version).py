import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Let's play!")

    # List of possible moves and their corresponding emojis
    choices = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    user_score = 0
    computer_score = 0

    # Ask the user for the number of rounds
    while True:
        try:
            total_rounds = int(input("\nHow many rounds would you like to play? "))
            if total_rounds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Game loop for the given number of rounds
    for round_num in range(1, total_rounds + 1):
        print(f"\nRound {round_num} of {total_rounds}")
        print(f"Your Score: {user_score} | Computer Score: {computer_score}")

        # Get user choice
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(list(choices.keys()))
        print(f"You chose: {choices[user_choice]}")
        print(f"The computer chose: {choices[computer_choice]}")

        # Determine the winner of the round
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("The computer wins this round!")
            computer_score += 1

    # Display the final results
    print("\nGame Over!")
    print(f"Final Score: You - {user_score} | Computer - {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations! You won the game! 🎉")
    elif user_score < computer_score:
        print("The computer wins the game! Better luck next time!")
    else:
        print("It's a tie! Great match!")

    print("Thanks for playing!")

# Run the enhanced game
play_game()