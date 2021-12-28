#******************************#
# Project: CodeWars
#      alphabet position
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 13, 2021
#******************************#

import string

# # V.1
# #######################################################################
# def alphabet_position(text):
#     # Specify a variable for the string or lower case letters.
#     ############################# Can't use this since can't import inside function on codewars #####################
#     # # Need to import 'string' module.
#     # import string
#     # string_of_letters = string.ascii_lowercase
#     #################################################################################################################

#     string_of_letters = "abcdefghijklmnopqrstuvwxyz"

#     # # Return the position of a single character input 'text' letter.
#     # return string_of_letters.index(text) + 1

#     # # If there are no letters in 'text', return ''.
#     # for character in text:
#     #     if character not in string_of_letters:
#     #         no_letters_in_text = True
#     #     else:
#     #         no_letters_in_text = False

#     # Empty string returns ''.
#     if text == '':
#         return ''

#     # Use a loop to iterate over the input string and create a new string of concatenated position values with spaces between them.
#     result = ''
#     for letter in text:
#         # print(letter, end=', ')
#         letter = letter.lower()
#         # if letter in string_of_letters:
#         if letter in string_of_letters:

#         # if letter.isalpha():
#             result = result + ' ' + str(string_of_letters.index(letter) + 1)
#         else:
#             continue
    
#     # return result.removeprefix(' ') # Can't use 'string' methods.
#     return result.replace(' ', '', 1)

# #######################################################################

# # V.2
# #######################################################################
# def alphabet_position(text):
#     string_of_letters = string.ascii_lowercase

#     # Empty string returns ''.
#     if text == '':
#         return ''

#     # Use a loop to iterate over the input string and create a new string of concatenated position values with spaces between them.
#     result = ''
#     for letter in text:
#         letter = letter.lower()
#         # if letter in string_of_letters:
#         if letter in string_of_letters:
#             # # This concatenation will add an extra ' ' at beginning of string, this will be removed later.
#             result = result + ' ' + str(string_of_letters.index(letter) + 1)
#         else:
#             continue
#     # Remove the leading ' ' and return the string.
#     return result.lstrip()
# #######################################################################

# Someone else's solution: https://www.codewars.com/kata/reviews/546f92300e7b08fe6100001c/groups/54745f7041ad4018c2000b63
#######################################################################
def alphabet_position(text):
    return ' '.join(str(string.ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
#######################################################################


# string_of_letters = string.ascii_lowercase
string_of_letters = string.ascii_letters

# print(string_of_letters)

# for i in range(len(string_of_letters)):
#     print(f"{i + 1} : {string_of_letters[i]}", end=', ')

# Print the index of the letter 'j' in the string string_of_letters
# There must be a string method which returns this index number.
# s.index(x[, i[, j]])
    # index of the first occurrence of x in s (at or after index i and before index j)
# print(f"The letter 'j' is at index {string_of_letters.index('j')}.")

# For this Kata, the index has to be shifted +1 since 'a' is in 'position' '1'.
# print(f"The letter 'j' is at postion {string_of_letters.index('j') + 1}.")

# for index in range(len(string_of_letters)):
#     print(f"The letter {string_of_letters[index]} is at position {string_of_letters.index(string_of_letters[index]) + 1}")

# the_letter = 'e'
# print(f"The letter '{the_letter}' is at position {alphabet_position(the_letter)}")

# the_input_string = 'a$b c'
# the_input_string = 'a$b0c'
# the_input_string = '123 j&'
00

# print("abc".index('d'))
