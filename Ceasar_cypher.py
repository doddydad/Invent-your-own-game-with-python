# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:03:09 2020

@author: Andrew
"""

# Caesar cypher

#Please don't add upper cases, message is converted to lower case
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    # Finds out whether encryting or decrypting
    mode = ""
    while not mode.startswith(("d", "e", "b")):
        mode = input("Would you like to encrypt, decrypt or brute force a message?: ").lower()
    return mode[0]


def getMessage():
    # Yup
    print("Please enter your message here")
    return input().lower()


def getKey():
    # how much to change it by
    key = ""
    while key == "":
        print("Enter the key number: ")
        try:
            key = int(input())
        except ValueError:
            print("Please enter an integer")
    return key


def getTranslatedMessage(mode, message, key):
    # The only interesting function
    newMessage = ""

    # Decryption is just opposite of encryption
    if mode == "d":
        key = -key

    # This is where it actually shifts the message
    for letter in message:
        if letter in SYMBOLS:
            letterIndex = SYMBOLS.find(letter)
            letterIndex += key
            letterIndex = letterIndex % MAX_KEY_SIZE
            letter = SYMBOLS[letterIndex]
        newMessage += letter

    return newMessage


def main():
    mode = getMode()
    message = getMessage()

    # Non brute force
    if mode != "b":
        key = getKey()
        print("\nYour translated text is: ")
        print(getTranslatedMessage(mode, message, key))

    # Cycles through all possible keys. Technically should use frequency
    # analysis.
    if mode == "b":
        print("\nHere are all the possible shifts\n")
        i = 1
        for i in range(MAX_KEY_SIZE):
            print(getTranslatedMessage(mode, message, i))


main()
