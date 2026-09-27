"""Match Coins Game - Coin Class

Author: Ali Tarom
Purpose: Represents a single coin that can be tossed and show Heads or Tails.
Starter/Resources: Python Crash Course, Chapters 1-9
Date: September 2026
"""

import random


class Coin:
    """Represents a single coin that can be tossed."""

    def __init__(self):
        """Initialize the coin with a starting side."""
        self.__sideup = "Heads"

    def toss(self):
        """Toss the coin and randomly set it to Heads or Tails."""
        number = random.randint(0, 1)

        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup