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

    play_again = "y"

    while play_again == "y" or play_again == "Y":
        print()
        print("Tossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match!", player1.get_name(), "wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match!", player2.get_name(), "wins a coin.")

        print()
        print(player1.get_name(), "has", player1.get_wallet(), "coins.")
        print(player2.get_name(), "has", player2.get_wallet(), "coins.")

        play_again = input("Do you want to toss the coins? (y/n): ")

    print()
    print("--- Final Score ---")
    print(player1.get_name() + ":", player1.get_wallet())
    print(player2.get_name() + ":", player2.get_wallet())

    if player1.get_wallet() > player2.get_wallet():
        print(player1.get_name(), "has more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(player2.get_name(), "has more coins!")
    else:
        print("It's a draw!")


main()

