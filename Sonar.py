# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:48:22 2020

@author: Andrew
"""

# Sonar Treasure Hunt

import random
import sys


def getNewBoard():
    # Create 50x15 board
    board = []
    # Width
    for x in range(50):
        board.append([])
        # the random symbols should make it look better but...
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append("~")
            else:
                board[x].append("\'")
    return board


def drawBoard(board):
    # Visualises the board for the player
    tensDigitLine = "   "
    for i in range(1, 5):
        tensDigitLine += (" " * 9) + str(i)

    # Prints the frame of the board
    # Needs to be manually adjusted if the width changes.
    print(tensDigitLine)
    print("   " + "0123456789" * 5)
    print()

    # Evens out first 9 rows and the others
    for row in range(15):
        if row < 10:
            extraSpace = " "
        else:
            extraSpace = ""

        # Creates the exact string we add
        boardRow = ""
        for column in range(50):
            boardRow += board[column][row]

        print("%s%s %s %s" % (extraSpace, row, boardRow, row))

    print()
    print("   " + ("0123456789" * 5))
    print(tensDigitLine)


def getRandomChests(numChests):
    # Creates a list of chest locations
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 49), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests


def isOnBoard(x, y):
    # Checks if a move is legal
    return x in range(50) and y in range(15)


def makeMove(board, chests, x, y):
    # Makes the move
    smallestDistance = 80
    for cx, cy in chests:
        # you can use actual distance, but it tends to be less helpful
        # To do so, use pythag then round to one digit.
        distance = abs(cx-x) + abs(cy-y)
        if distance < smallestDistance:
            smallestDistance = distance

    if smallestDistance == 0:
        board[x][y] = "X"
        chests.remove([x, y])
        return "You have found a sunken treasure"

    elif smallestDistance < 10:
        board[x][y] = str(smallestDistance)
        return "Treasure detected at a distance of %s from the sonar" % (smallestDistance)

    else:
        board[x][y] = "O"
        return "Sonar didn't detect anything, so treasure chests out of range."


def enterPlayerMove(previousMoves):
    # Lets the player enter a move
    x = -1
    y = -1

    print("Where do you want to drop the sonar device. (type quit to exit)")

    while True:
        x = input("x (0-49): ")
        y = input("y (0-14): ")

        if x.lower() == "quit" or y.lower() == "quit":
            print("Thanks for playing")
            sys.exit()

        try:
            y = int(y)
            x = int(x)
        except ValueError:
            print("Please enter an integer")

        if isOnBoard(x, y):
            if [x, y] not in previousMoves:
                return [x, y]
            else:
                print("You've already tried that move!")


def showInstructions():
    print("""
          You are the caption of a ship looking for treasure, your current
          mission is to find 3 sunked treasure ships at the bottom of the
          ocean, your sonar only finds distance between it and the chest not
          direction.

          Enter coordinates to drop a sonar beacon, it will show an \"X\" if
          it\'s on top of the chest, an \"O\" if it\'s got no chests in range
          and a numeral up to 9 to show the distance to the nearest chest.
          """)
    print("Press enter to continue")
    input()


def main():
    # The actual game
    print("Would you like to view the instructions? (yes/no)")
    if input().lower().startswith("y"):
        showInstructions()

    while True:
        # Game setup
        previousMoves = []
        sonarDevices = 20
        theBoard = getNewBoard()
        theChests = getRandomChests(3)
        drawBoard(theBoard)

        while sonarDevices > 0:
            # Update player on their progress
            print("You have %s sonar devices remaining and %s chest(s) to find"
                  % (sonarDevices, len(theChests)))

            [x, y] = enterPlayerMove(previousMoves)
            previousMoves.append([x, y])

            moveResult = makeMove(theBoard, theChests, x, y)
            if moveResult is False:
                continue

            if moveResult == "You have found a sunken treasure":
                # Update beacons after a chest is found
                for [x, y] in previousMoves:
                    if theBoard[x][y] != "X":
                        makeMove(theBoard, theChests, x, y)

                if len(theChests) == 0:
                    print("You won!")
                    again = input("Would you like to play again?(yes/no): ")
                    if again.lower().startswith("y"):
                        break
                    else:
                        sys.exit()

            drawBoard(theBoard)
            print(moveResult)

            sonarDevices -= 1
            if sonarDevices == 0:
                print("""We've run out of sonar devices before completing
mission, in other words, we lost""")
                again = input("Would you like to play again?(yes/no): ")
                if again.lower().startswith("y"):
                    break
                else:
                    sys.exit()


main()
