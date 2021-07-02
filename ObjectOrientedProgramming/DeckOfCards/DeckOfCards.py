
"""
@Author: Ayur Ninawe
@Date: 2021-07-03 00:50:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 00:50:30
@Title : Create a Deck of cards program.
"""

import random
import itertools

class dack_of_card:
    """
    Description:
        this class define for random card distribution
    """
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def random_card_distribute(self):
        """
        Description:
            this method define for random card distribution
        """
        deck = list(itertools.product(self.rank, self.suits))
        random.shuffle(deck)
        player1 = []
        player2 = []
        player3 = []
        player4 = []

        for card in range(0, 36, 4):
            player1.append([deck[card][0], deck[card][1]])
            player2.append([deck[card + 1][0], deck[card + 1][1]])
            player3.append([deck[card + 2][0], deck[card + 2][1]])
            player4.append([deck[card + 3][0], deck[card + 3][1]])

        print_function(player1, "player1")
        print_function(player2, "player2")
        print_function(player3, "player3")
        print_function(player4, "player4")


def print_function(player, player_string):
    """
    Description:
        this method define for print player with card have
    """
    print("##################################### {0} HAVE CARD #####################################".format(player_string.upper()))
    for print_card in range(9):
        print("{0} of {1}".format(player[print_card][0], player[print_card][1]))
    return player

# main function
if __name__ == "__main__":
    objdack_of_card = dack_of_card()
    objdack_of_card.random_card_distribute()
