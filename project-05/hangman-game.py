import random

def hangman():
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    # List of words to choose from
    words = ['python', 'hangman', 'developer', 'programming', 'debugging', 'tutorial']
    word = random.choice(words).lower()  # Select a random word

    # Initialize game variables
    guessed_word = ['_'] * len(word)  # Display the word as underscores
    attempts = 6  # Number of incorrect guesses allowed
    guessed_letters = []  # Keep track of letters already guessed

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the guessed word
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"'{guess}' is not in the word. You lose an attempt.")
            attempts -= 1

        # Check win condition
        if '_' not in guessed_word:
            print("\nCongratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        # Player loses
        print("\nGame Over! You've run out of attempts.")
        print(f"The word was: {word}")

    print("Thanks for playing!")

# Run the game
hangman()
