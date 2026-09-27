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