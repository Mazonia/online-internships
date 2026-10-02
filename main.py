"""
Online Internships - Unified Runner & Portfolio Manager
Consolidates assignments from ShadowFox and Cognorise Infotech remote internships.
"""

from ShadowFox.Hangman import run_cli_game

def show_portfolio():
    print("==================================================")
    print("     ONLINE INTERNSHIPS PORTFOLIO MANAGEMENT     ")
    print("==================================================")
    print("1. Launch ShadowFox Hangman Game")
    print("2. Launch Cognorise Infotech Utilities")
    print("0. Exit")
    print("--------------------------------------------------")

if __name__ == "__main__":
    show_portfolio()
    run_cli_game()
