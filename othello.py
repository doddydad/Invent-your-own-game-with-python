# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:13:14 2020

@author: Andrew
"""

# Othello

import sys
import random

HEIGHT = 8
WIDTH = 8


def drawBoard(board):
    # Draws an already created board
    print("   12345678")
    print("  +--------+")

    # Writes in each tile
    for y in range(HEIGHT):
        print(" %s|" % (y+1), end="")
        for x in range(WIDTH):
            print(board[x][y], end="")
        print("|%s\n" % (y+1), end="")

    print("  +--------+")
    print("   12345678")


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
    # Return false if player's move is invalid
    # If valid return a list of spaces that will be captured.

    if board[xstart][ystart] != " ":
        return False

    captures = []
    if tile == "X":
        otherTile = "O"
    else:
        otherTile = "X"

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1],
                                   [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        # Checks each direction from the potential move
        x = xstart
        y = ystart

        # Record captures in te current direction only
        potentialCaptures = []

        while isOnBoard(x, y) and board[x][y] != " ":

            # Adds tiles to be captured if the line is surrounded
            if board[x][y] == otherTile:
                print("lol")
                potentialCaptures.append([x, y])

            # This records what will be captured
            if board[x][y] == tile and potentialCaptures != []:
                print(potentialCaptures)
                for [x, y] in potentialCaptures:
                    captures.append([x, y])
                    break

            x += xdirection
            y += ydirection

    if captures != []:
        return captures
    return False


def boardWithValidMoves(board, tile):
    # Show the board with hint spots showing all valid moves
    boardCopy = board
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
    playerTile = ""
    print("Would you like the X or O tile?(type in your answer): ")
    while playerTile not in ("X", "O"):
        playerTile = input().upper()
    return playerTile


def makeMove(board, tile, x, y):
    # Place the tile at [xstart, ystart] and flip the pieces.
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


def getPlayerMove(board, playerTile):
    # Takes the players move or command for hints or to quit
    while True:
        print("Please enter your move as XY, or ask for hints or to quit: ")
        x = ""
        y = ""
        playerMove = input().lower()

        if playerMove.startswith("q"):
            print("Thanks for playing")
            sys.exit()

        elif playerMove.startswith("h"):
            drawBoard(boardWithValidMoves(board, playerTile))

        try:
            x = int(playerMove[0]) - 1
            y = int(playerMove[1]) - 1
        except IndexError:
            True
        except ValueError:
            playerMove = playerMove

        if x in range(8) and y in range(8):
            if isValidMove(board, playerTile, x, y) is True:
                break

    return [x, y]

board = getNewBoard()
drawBoard(board)
getPlayerMove(board, "X")