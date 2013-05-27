
import player
import field

SCORE_CAP = 300

# client-server protocol codes
class PROTOCOL:
    # client to server; request to join a game (follow by credentials, TCP)
    REQUEST_JOIN = 64368934

    # server to client; recieve player to game
    RECIEVE_JOIN = 62362325

    # server to client; display new details of game player hasn't recieved yet (output to screen, UDP)
    GAME_DETAILS = 56856455

    # server to client; ask player for name (TCP)
    REQUEST_NAME = 56569564

    # client to server; recieve player name (TCP)
    RECIEVE_NAME = 36233635

    # server to client; ask player for move (TCP)
    REQUEST_MOVE = 54754321

    # client to server; ask player for move (TCP)
    RECIEVE_MOVE = 56845800


# full hand of cards used by players 
CARDS = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A']

# point value for each card
CARD_SCORE = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

# returns a copy of the starting hand
def newHand():
    return list(CARDS)

def score(card):
    if card in CARDS:
        return CARD_SCORE[card]
    else:
        return 0

# creates the players for the game
def getPlayers():
    names = raw_input("Please enter the player names, seperated by spaces: ")
    names = names.split(',')

    players = []
    for name in names:
        players.append(player.Player(name.strip()))

    return players
