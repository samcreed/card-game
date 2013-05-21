
import game
import re

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    # resets a player's hand for the start of a new round
    def resetHand(self):
        self.hand = game.newHand()

    def playCard(self, card):
        self.hand.remove(card)

    def hasCard(self, card):
        return card in self.hand

    def getScore(self):
        return self.score

    # determine next move for this player
    def getMove(self):

        validMove = False
        card = ''

        while not validMove:
            move = input('enter next move: ')
            match = re.match(r"play (\w+)", move, RE.I | RE.M)

            if match:
                card = match.group(0)

                if self.hasCard(card):
                    validMove = True

        return card


