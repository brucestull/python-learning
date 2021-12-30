#******************************#
# Project: Codewars is_pangram()
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
#          Find It
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 30, 2021
#******************************#

# import string

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
# the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# Define the function.
import string


def is_pangram(input_string):
    '''This function returns True if input string is a pangram, otherwise returns False.'''
    # How can we sort input_string? No need to sort since we are using a dictionary below.

    # Convert to lower case.
    input_string_lowered = input_string.lower()
    # Remove numbers and punctuation from the string.
    working_string = ''
    for character in input_string_lowered:
        if character in string.ascii_lowercase:
            working_string += character

    # Build a dictionary which uses the letters of the alphabet as keys
    # and the number of times the letter occurs as the value.
    dictionary_of_letters = {}
    for character in string.ascii_lowercase:
        dictionary_of_letters[character] = working_string.count(character)

    # Loop through the dictionary:
    for element in dictionary_of_letters:
        # If any character occurs less than 1 time:
        if dictionary_of_letters[element] < 1:
            # We now know the sequence is not a pangram, so set result to False.
            result = False
            # Break out of the loop since there is no need to check the rest of the elements.
            break
        # Else, the character occurs one or more times, the sequence may be a pangram, so continue to check the rest of the elements.
        else:
            result = True
            # This 'continue' is not necessary, but I've placed it here to help me remember what's going on.
            continue
    return result

test = "The quick brown fox jumps over the lazy dog"

print(test)
print(is_pangram(test))

test = test.replace('d','')

print(test)
print(is_pangram(test))
# is_pangram(test)