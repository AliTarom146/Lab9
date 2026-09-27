"""Match Coins Game - Player Class

Author: Ali Tarom
Purpose: Represents a player with a name, wallet, and Coin object.
Starter/Resources: Python Crash Course, Chapters 1-9
Date: September 2026
"""

from coin import Coin


class Player:
    """Represents a player in the Match Coins game."""

    def __init__(self, name):
        """Initialize the player's name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Tell the player's coin to toss itself."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the player's current number of coins."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name