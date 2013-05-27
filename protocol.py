
# client-server protocol codes

# client to server; request to join a game (follow by credentials, TCP)
REQUEST_JOIN = 64368934

# server to client; recieve player to game
RECIEVE_JOIN = 62362325

# server to client; display new details of game player hasn't recieved yet (output to screen, UDP)
GAME_DETAILS = 56856455

# server to client; ask player for move (TCP)
REQUEST_MOVE = 54754321

# client to server; ask player for move (TCP)
RECIEVE_MOVE = 56845800
