
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

# returns the score value for the given card
def score(card):
    if card in CARDS:
        return CARD_SCORE[card]
    else:
        return 0
