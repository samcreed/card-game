
import random
import game

class Field:

    def __init__(self):
        self.pot = 0
        self.players = []
        self.deck = []

    # checks to see if the score cap has been reached; if so, return the winner
    def winnerFound(self):
        winner = self.players[0]

        for player in self.players:
            if player.bank > winner.bank:
                winner = player
        
        if winner.bank < game.SCORE_CAP / len(self.players):
            winner = None

        return winner

    # displays the drawn card to all players
    def showTurnStart(self, card):
        print "\nNEW TURN."
        print "The card {} was drawn from the deck. Pot = {}".format(card, self.pot)

    # show end turn results
    def showTurnEnd(self, moves, winner):
        for player in moves:
            print "{} plays {}.".format(player.name, moves[player])

        if winner:
            print "{} wins the turn!".format(winner.name)
        else:
            print "Draw! Current pot is added to next round."

    # event handler for a new turn
    def newTurn(self):
        # start turn
        card = self.deck.pop()
        self.pot += game.score(card)
        self.showTurnStart(card)

        # get the player's moves
        moves = {}
        for player in self.players:
            moves[player] = player.getMove()

        # determine winner
        winner = self.players[0]
        for player in self.players:
            score = game.score(moves[player])
            player.score = score

            if score > winner.score:
                winner = player

        # deal with tie-breakers
        for player in self.players:
            if player.name != winner.name and winner.score == player.score:
                winner = None
                break

        # assign points if there is a winner
        if winner:
            winner.bank += self.pot
            self.pot = 0

        # discard the used player cards
        for player in self.players:
            player.discard(moves[player])

        # end turn
        self.showTurnEnd(moves, winner)

    # show starting round results
    def showRoundStart(self):
        print "\nNEW ROUND."
        print "Pot = 0"

    # show end round results
    def showRoundEnd(self):
        print "END ROUND."
        print "Current Scores:"

        for player in self.players:
            print "{}, {}".format(player.name, player.bank)

    # event handler for a new round
    def newRound(self):
        # start round
        self.pot = 0

        self.deck = game.newHand()
        random.shuffle(self.deck)
        self.showRoundStart()

        for player in self.players:
            player.resetHand()

        while self.deck: # still has cards
            self.newTurn()

        # end round
        self.showRoundEnd()

    # show end game results
    def showGameStart(self):
        print "NEW GAME."

    # show end game results
    def showGameEnd(self, winner):
        print "\nEND GAME!"
        print "{} is the winner!!".format(winner.name)

    # event handler for a new game
    def newGame(self):
        self.showGameStart()
        self.players = game.getPlayers()

        winner = None
        while not winner:
            self.newRound()
            winner = self.winnerFound()
        
        self.showGameEnd(winner)
