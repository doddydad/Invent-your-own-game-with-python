# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:18:06 2020

@author: Andrew
"""


def fibonacci_finder(starting_array):
    # Takes an array finds any fibonacci type sequences within it
    fib_sequences = []
    longest_sequence_length = 0

    # Create a list of the possible sequences
    for i in range(len(starting_array)):
        for j in range(i + 1, len(starting_array)):
            temp_list = [starting_array[i], starting_array[j]]
            while temp_list[-1] + temp_list[-2] in starting_array:
                temp_list.append(temp_list[-1] + temp_list[-2])
            if len(temp_list) > 2:
                fib_sequences.append(temp_list)

    # Now find the longest sequence
    for sequence in fib_sequences:
        sequence_length = len(sequence)

        # Adds to the list of sequences of max length
        if sequence_length == longest_sequence_length:
            longest_sequence.append(sequence)

        # changes the max length and creates the list of sequences that long
        if sequence_length > longest_sequence_length:
            longest_sequence_length = sequence_length
            longest_sequence = [sequence]

    if longest_sequence_length > 0:
        print(longest_sequence_length)
        print(longest_sequence)
        return longest_sequence_length

    return 0


fibonacci_finder([1, 3, 7, 11, 12, 14, 18, 25, 29, 31])
