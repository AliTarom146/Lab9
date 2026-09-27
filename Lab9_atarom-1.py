"""Match Coins Game

Author: Ali Tarom
Purpose: Runs the Match Coins game using two Player objects.
Starter/Resources: Python Crash Course, Chapters 1-9
Date: September 2026
"""

from player import Player


def main():
    """Run the Match Coins game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")