"""
Number guessing game.

The computer selects a random number and the user
tries to guess it with hints provided.
"""

import random


def get_user_guess() -> int:
    """
    Prompt the user for a numeric guess.

    :return: User's guessed number
    """
    while True:
        try:
            return int(input("Enter your guess (1–100): "))
        except ValueError:
            print("Please enter a valid number.")


def play_game() -> None:
    """
    Run the guessing game logic.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎲 I have selected a number between 1 and 100.")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break


def main() -> None:
    """
    Main entry point.
    """
    play_game()


if __name__ == "__main__":
    main()
