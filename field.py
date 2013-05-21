
import random

class Field:

    def __init__(self):
        self.pot = 0
        self.players = []
        self.deck = []

    # checks to see if the score cap has been reached; if so, return the winner
    def capReached(self):
        winner = None

        for player in self.players:
            score = player.score
            if score >= SCORE_CAP:
                if winner and score > winner.score:
                    max = player
                
        return winner

    # displays the drawn card to all players
    def showTurnStart(self, card):
        print "NEW TURN."
        print "The card %s was drawn from the deck. Pot = %d".format(card, self.pot)

    # show end turn results
    def showTurnEnd(self, moves, winner):
        for player in moves:
            print "Player %s plays %s.".format(player, moves[player])

        if winner:
            print "Player %s wins the turn!".format(winner.name)
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

            if score > winner.score:
                winner = player
            elif score == winner.score:
                if winner is not player: # need to check, elsewise P0 would never win
                    winner = None

        # assign points if there is a winner
        if winner:
            winner.score += self.pot
            self.pot = 0

        # discard the used player cards
        for player in self.players:
            player.discard(moves[player])

        # end turn
        self.showTurnEnd()


    # show starting round results
    def showRoundStart(self):
        print "NEW ROUND."

    # show end round results
    def showRoundEnd(self):
        print "END ROUND."
        print "Current Scores:"

        for player in self.players:
            print "%s, %s".format(player.name, player.score)

    # event handler for a new round
    def newRound(self):
        # start round
        self.deck = game.newHand()
        random.shuffle(self.deck)
        self.showRoundStart()

        while self.deck: # still has cards
            self.newTurn()

        # end round
        self.showRoundEnd()

    # show end game results
    def showGameStart(self):
        print "NEW GAME."

    # show end game results
    def showGameEnd(self, winner):
        print "END GAME!"
        print "%s is the winner!!".format(winner)
        pass

    # event handler for a new game
    def newGame(self):
        self.players = game.createPlayers()
        self.showGameStart()

        winner = None
        while not winner:
            self.newRound()
            winner = self.capReached()
        
        self.showGameEnd(winner)
