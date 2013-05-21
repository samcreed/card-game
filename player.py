
import game
import re

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bank = 0
        self.hand = []

    # resets a player's hand for the start of a new round
    def resetHand(self):
        self.hand = game.newHand()

    # discards a card that has been played
    def discard(self, card):
        self.hand.remove(card)

    # determine next move for this player; currently this is human client
    def getMove(self):

        validMove = False
        card = ''

        while not validMove:
            print "\n{}'s hand: {}".format(self.name, ", ".join(self.hand))

            move = raw_input("{}'s move: ".format(self.name))
            match = re.search(r"(\w+)", move, re.I | re.M)

            if match:
                card = match.group(1)

                if card in self.hand:
                    validMove = True
                else:
                    print "Sorry, you don't have that in your hand."
            else:
                print "Sorry, I didn't understand that."

        return card
