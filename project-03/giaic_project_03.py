# -*- coding: utf-8 -*-
"""GIAIC-Project-03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sms5KHWCYFwt6Oo_A8SNffNwBI5Xy3kt
"""

import random

def computer_guess():
    print("Welcome to the 'Guess the Number' game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, tell me if my guess is too high (H), too low (L), or correct (C).")

    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    feedback = ''
    attempts = 0

    while feedback != 'C':
        # Computer makes a guess
        if low != high:
            guess = (low + high) // 2  # Random guess within the range
        else:
            guess = low  # Only one number left to guess

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

