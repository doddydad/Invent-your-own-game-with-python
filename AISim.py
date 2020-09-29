# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:13:14 2020

@author: Andrew
"""

# Othello


import random

HEIGHT = 8
WIDTH = 8

computer1Tile, computer2Tile = ["X", "O"]


def giveInstructions():
    # How to play for the player
    # Not used for Ai v AI
    drawBoard(getNewBoard())
    print(
        """In this game you'll be playing on a board like the one above
you will pick  a piece to play with and place pieces to
capture your opponents. You enter the place you would like
to play by entering the co-ordinates of the position along
then down. You capture a line of their pieces if the one
you place means their lines has one of your pieces at each
end. You must place your pieces each turn such that they
capture at least one piece. The game ends when either player
can not make a legal move. The winner is the player who at the
end of the game has most pieces on the board.

You can quit at any time, and asking for hints will mark
legal moves for you with a \".\"
""")


def drawBoard(board):
    # Draws an already created board
    # Not used in AI v AI
    print("   1 2 3 4 5 6 7 8")
    print("  +---------------+")

    # Writes in each tile
    for y in range(HEIGHT):
        print(" %s|" % (y+1), end="")
        for x in range(WIDTH):
            if x != 7:
                print(board[x][y], end=" ")
            elif x == 7:
                print(board[x][y], end="")
        print("|%s\n" % (y+1), end="")

    print("  +---------------+")
    print("   1 2 3 4 5 6 7 8")


def getNewBoard():
    # Creates a fresh empty board
    board = []
    for i in range(HEIGHT):
        board.append([" ", " ", " ", " ", " ", " ", " ", " "])
    board[3][4] = board[4][3] = "X"
    board[3][3] = board[4][4] = "O"
    return board


def isOnBoard(x, y):
    # Check the move is on the board
    if x in range(WIDTH) and y in range(HEIGHT):
        return True
    return False


def isValidMove(board, tile, xstart, ystart):
    # Return False if the players move is invalid, otherise return
    # where they'll capture

    # Checks it would be possible to place a piece here
    if board[xstart][ystart] != " " or not isOnBoard(xstart, ystart):
        return False

    if tile == "X":
        otherTile = "O"
    else:
        otherTile = "X"

    captures = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1],
                                   [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        # We've already checked the placement is ok
        x, y = xstart, ystart
        x += xdirection
        y += ydirection

        # We check it goes over the other player's tiles
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection

            # Record the captures in this direction
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    captures.append([x, y])

    # No captures means invalid move remember
    if len(captures) == 0:
        return False
    return captures


def boardWithValidMoves(board, tile):
    # Show the board with hint spots showing all valid moves
    # Not used in AI v AI
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(board, tile):
        boardCopy[x][y] = "."
    return boardCopy


def getValidMoves(board, tile):
    # Retuns a list of valid moves for the player with the given tile
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y):
                validMoves.append([x, y])
    return validMoves


def getBoardCopy(board):
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy


def getScoreOnBoard(board):
    # Totals the score by tile
    xscore = 0
    oscore = 0

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == "X":
                xscore += 1
            if board[x][y] == "O":
                oscore += 1

    return {"X": xscore, "O": oscore}


def enterPlayerChoice():
    # Let the player choose which tile they want
    # Not used in Ai v AI
    playerTile = ""
    print("Would you like the X or O tile?(type in your answer): ")
    while playerTile not in ("X", "O"):
        playerTile = input().upper()

    if playerTile == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def makeMove(board, tile, x, y):
    # Place the tile at [x, y] and flip the pieces.
    captures = isValidMove(board, tile, x, y)

    if captures is False:
        return False

    board[x][y] = tile
    for [x, y] in captures:
        board[x][y] = tile
    return True


def isOnCorner(x, y):
    # Checks if coordinates are in a corner
    if [x, y] in ([0, 0], [0, HEIGHT - 1], [WIDTH - 1, HEIGHT - 1],
                  [WIDTH - 1, 0]):
        return True
    return False


def getDumbMove(board, tile):
    # Makes a horrible move
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves)
    worstScore = 64

    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, tile, x, y)
        score = getScoreOnBoard(boardCopy)[tile]
        if score < worstScore:
            worstMove = [x, y]
            worstScore = score

    return worstMove


def getRandomMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    return random.choice(possibleMoves)


def whoGoesFirst():
    # Randomly choose who goes first
    if random.randint(0, 1) == 0:
        return computer1Tile
    else:
        return computer2Tile


def getSmartMove(board, tile):
    # Determine where to move by corners > best score
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestscore = 0
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, tile, x, y)
        score = getScoreOnBoard(boardCopy)[tile]
        if score > bestscore:
            bestmove = [x, y]
            bestscore = score

    return bestmove


def printScore(board, playerTile, computerTile):
    scores = getScoreOnBoard(board)
    print("You: %s points. Computer: %s points" % (scores[playerTile],
                                                   scores[computerTile]))


def playGame(playerTile, computerTile):
    # Playing the game and taking turns
    turn = whoGoesFirst()

    board = getNewBoard()

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        # Check stalemate condition
        if computerValidMoves == [] or playerValidMoves == []:
            return board

        elif turn == computer1Tile:
            if playerValidMoves != []:
                move = getSmartMove(board, playerTile)
                makeMove(board, playerTile, move[0], move[1])
            turn = computer2Tile

        elif turn == computer2Tile:
            if computerValidMoves != []:
                move = getDumbMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = computer1Tile


def main(NUM_GAMES):
    xWins = oWins = ties = 0

    computer1Tile, computer2Tile = ["X", "O"]

    for i in range(NUM_GAMES):
        finalBoard = playGame(computer1Tile, computer2Tile)

        # Wrap up the end of the game
        scores = getScoreOnBoard(finalBoard)
        print("#%s: X scored %s points and O scored %s points!"
              % (i + 1, scores["X"], scores["O"]))

        if scores[computer1Tile] > scores[computer2Tile]:
            xWins += 1

        elif scores[computer2Tile] > scores[computer1Tile]:
            oWins += 1

        else:
            ties += 1

    print("x wins: %s (%s%%)" % (xWins, round(xWins / NUM_GAMES * 100, 1)))
    print("o wins: %s (%s%%)" % (oWins, round(oWins / NUM_GAMES * 100, 1)))
    print("ties: %s (%s%%)" % (ties, round(ties / NUM_GAMES * 100, 1)))


main(250)
