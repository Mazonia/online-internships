"""
ShadowFox Python Internship - Hangman Game Module
Object-Oriented Hangman implementation featuring word categories, visual stage renderer, and score tracking.
"""

import random
from typing import List, Set, Tuple

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

WORD_CATEGORIES = {
    "Programming": ["PYTHON", "JAVASCRIPT", "DEVELOPER", "ALGORITHM", "DATABASE", "CYBERSECURITY"],
    "Animals": ["ELEPHANT", "PENGUIN", "DOLPHIN", "CHAMELEON", "KANGAROO"],
    "Countries": ["GHANA", "CANADA", "JAPAN", "BRAZIL", "GERMANY"]
}

class HangmanGame:
    def __init__(self, category: str = "Programming", word: str = None):
        self.category = category if category in WORD_CATEGORIES else "Programming"
        self.secret_word = (word or random.choice(WORD_CATEGORIES[self.category])).upper()
        self.guessed_letters: Set[str] = set()
        self.max_attempts = len(HANGMAN_PICS) - 1
        self.wrong_attempts = 0

    def make_guess(self, letter: str) -> Tuple[bool, str]:
        """Process a letter guess. Returns (success, message)."""
        letter = letter.upper()
        if not letter.isalpha() or len(letter) != 1:
            return False, "Please enter a single valid letter A-Z."
        if letter in self.guessed_letters:
            return False, f"You already guessed '{letter}'."

        self.guessed_letters.add(letter)
        if letter in self.secret_word:
            return True, f"Great guess! '{letter}' is in the word."
        else:
            self.wrong_attempts += 1
            return False, f"Sorry, '{letter}' is not in the word."

    def get_masked_word(self) -> str:
        return " ".join(c if c in self.guessed_letters else "_" for c in self.secret_word)

    def is_won(self) -> bool:
        return all(c in self.guessed_letters for c in self.secret_word)

    def is_game_over(self) -> bool:
        return self.is_won() or self.wrong_attempts >= self.max_attempts

    def get_ascii_stage(self) -> str:
        return HANGMAN_PICS[self.wrong_attempts]

def run_cli_game():
    print("==================================================")
    print("       SHADOWFOX INTERNSHIP - HANGMAN GAME        ")
    print("==================================================")
    game = HangmanGame()
    print(f"Category: {game.category}")

    while not game.is_game_over():
        print(game.get_ascii_stage())
        print(f"Word: {game.get_masked_word()}")
        print(f"Guessed: {', '.join(sorted(game.guessed_letters))}")
        guess = input("Enter a letter: ")
        _, msg = game.make_guess(guess)
        print(msg)

    print(game.get_ascii_stage())
    if game.is_won():
        print(f"🎉 Congratulations! You guessed '{game.secret_word}' correctly!")
    else:
        print(f"💥 Game Over! The word was '{game.secret_word}'.")

if __name__ == '__main__':
    run_cli_game()
