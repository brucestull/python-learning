#******************************#
# Project: CodeWars
#      alphabet position
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 13, 2021
#******************************#

import string
from typing import ValuesView

# #######################################################################

# Someone else's solution: https://www.codewars.com/kata/reviews/546f92300e7b08fe6100001c/groups/54745f7041ad4018c2000b63
def alphabet_position(text):
    # return f(g(h() + <value>) for <index of object> in <object> if <condition>)
    return ' '.join(str(string.ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
# #######################################################################

the_input_string = "The sunset sets at twelve o' clock."

letters = string.ascii_lowercase

print(f"The string '{the_input_string}' has positions:'{alphabet_position(the_input_string)}'")

test_string = "The test string."

# Added this line to make it easy to hide all the comments--which I use to learn--below. And skip down to BIG MOMENT.
viewable = True
if viewable:
    a_letter = "J"
    # print(f"\nConvert {a_letter} to lower case: {a_letter.lower()}\n")  # Convert J to lower case: j

    # Add 1 to the index since we want the position of the letter and not the zero-based index.
    # print(f"Get the index, and add 1, of letter {a_letter}: {string.ascii_lowercase.index(a_letter.lower()) + 1}")  # Get the index, and add 1, of letter J: 10

    # print(f"Convert int to string: {str(string.ascii_lowercase.index(a_letter.lower()) + 1)}")  # Convert int to string: 10

    # Convert the int to str so that we can concatenate the sequence.
    # Elements need to be strings in order to concatenate them. We are using the string method join().
    # print(' '.join(str(string.ascii_lowercase.index(n.lower()) + 1) for n in a_letter if n.isalpha()))  # 10

    # join() is useful since it only adds the prefix of the .join() in between each element.
    # print(' '.join(str(n) for n in range(5)))   # 0 1 2 3 4

    # print(' '.join(n for n in "string"))    # s t r i n g
    # print('*'.join(n for n in "string"))    # s*t*r*i*n*g

    # This takes each letter of the input string and adds them together, which results in same thing as input string.
    # print(''.join(n for n in "the string"))    # the string
    # print(''.join(n for n in "string") == 'string') # True

    # Remember, 'n for n in range(5)' returns a generator object, we need to specify what aspect/view we want to use/print.
    # Maybe this results in a tuple? The generator object is a tuple? Maybe that's why we are able to .join() the elements? We can .join() tuples?
    # print(n for n in range(5))  # <generator object <genexpr> at 0x0000019F1EF51A80>
    # print([n for n in range(5)])    # [0, 1, 2, 3, 4]

    # Try to .join() a tuple.
    # It seems we can join the elements of a tuple into a string.
    # print(' '.join(('a', 'b', 'c')))    # a b c

    # Can we define a tuple?
    # Yes.
    # the_tuple = ('b', 'i', 'g', ' ', 'c', 'a', 't')
    # print(the_tuple)    # ('b', 'i', 'g', ' ', 'c', 'a', 't')
    # print(''.join(the_tuple))   # big cat

    # What can we do with a tuple of int?
    int_tuple = (1, 2, 3, 4, 5)
    # print(int_tuple)    # (1, 2, 3, 4, 5)

    # We probably can't .join() a tuple of int.
    # print(' '.join(int_tuple))
    #     #   File "g:\My Drive\Python\PythonLearning\learn_single_line_for.py", line 72, in <module>
    #     # print(' '.join(int_tuple))
    #     # TypeError: sequence item 0: expected str instance, int found

    # Can we iterate over a tuple?
    # print(element for element in int_tuple) # <generator object <genexpr> at 0x0000017E71C41AF0>
    
    # print(str(element) for element in int_tuple)    # <generator object <genexpr> at 0x00000225AAAE1A80>

    # print([str(element) for element in int_tuple])  # ['1', '2', '3', '4', '5']
    # print(tuple(str(element) for element in int_tuple)) # ('1', '2', '3', '4', '5')

    # print(n) for n in range(5)  # Invalid syntax

    # What does list() do in this situation?
    # list() does the same thing as wrapping the elements in [].
    # print(n for n in range(5))
    # print(list(n for n in range(5)))
    # print([n for n in range(5)])
    #     # <generator object <genexpr> at 0x0000019558841A80>
    #     # [0, 1, 2, 3, 4]
    #     # [0, 1, 2, 3, 4]

    # # What does tuple() do in this situation?
    #     # Results in a tuple of the elements.
    # print(tuple(n for n in range(5)))   # (0, 1, 2, 3, 4)

    # Can we compare tuples?
    # It seems we may be able to compare tuples.
    # print(tuple(n for n in range(5)) == (0, 1, 2, 3, 4))    # True
    
    # print(list(n for n in range(5)) == [n for n in range(5)])   # True

    # If we were to use '+=' with a space adjacent to the string, the result can have a space at beginning or end of string.
    # the_string = ''
    # for n in range(5):
    #     the_string += ' ' + str(n)
    # print(the_string)

    # print(' '.join(str(n) for n in range(7) if n % 2 != 0))   # 1 3 5

    # print(' '.join(str(n) for n in range(7) if n % 2 == 0))   # 0 2 4 6

    # Print each character in the string.
    # print(character for character in "abc") # <generator object <genexpr> at 0x0000019266F60270>
    # print(character for character in ['a','b']) # <generator object <genexpr> at 0x0000023B58620270>

    # Start back where something prints an actual string or int.
    # print(' '.join(str(n) for n in range(5)))   # 0 1 2 3 4
    # print(str(n) for n in range(5))   # <generator object <genexpr> at 0x0000026D99D702E0>
    pass
########################################## BIG MOMENT ###########################################
# print([str(n) for n in range(5)])   # ['0', '1', '2', '3', '4']
########################################## BIG MOMENT ###########################################

# NOTE: [str(n) for n in range(5)] creates a LIST ['0', '1', '2', '3', '4']

# Print the alphabet position of each letter in the string 'test_string'.
# print([str(string.ascii_lowercase.index(n.lower()) + 1) for n in test_string if n.isalpha()])   # ['20', '8', '5', '20', '5', '19', '20', '19', '20', '18', '9', '14', '7']

# Print the alphabet positions of letters which are not 't' and not 'T'.
# print([str(string.ascii_lowercase.index(n.lower()) + 1) for n in test_string if n.lower() != 't' and n.isalpha()])   # ['8', '5', '5', '19', '19', '18', '9', '14', '7']

# Print the alphabet positions of letters which are 't' or 'T'.
# print([str(string.ascii_lowercase.index(n.lower()) + 1) for n in test_string if n.lower() == 't' and n.isalpha()])   # ['20', '20', '20', '20']


# print(' '.join([n for n in range(5)]))    # TypeError: sequence item 0: expected str instance, int found  #### .join() is a string method and so works only on strings.

# print(' '.join([str(n) for n in range(5)]))    # 0 1 2 3 4

# Print a couple numbers.
# print([n for n in range(5)])    # [0, 1, 2, 3, 4]

# .join() with and without []
# print(' '.join(str(n) for n in range(5)))    # 0 1 2 3 4
# print(' '.join([str(n) for n in range(5)]))    # 0 1 2 3 4

# ########################################################################
# ########################################################################
# # From: https://www.codewars.com/kata/reviews/55249a95de8b4b5ae2000464/groups/552540ce2142d7ba24000e65
# word = "Theg String"
# print(word)
# print("".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()]))
# ########################################################################

# # It seems the [] is not required in the solution. Will need to test this against the test battery.
# # It seems the version without the [] passes the full test battery. join() seems to work on generator object.
# print("".join("(" if word.lower().count(c) == 1 else ")" for c in word.lower()))

# ########################################################################
# ########################################################################

# Prints a string. 'n' is converted from int to str. Each element of generator object is concatenated with the other elements with a space ' '.
# print(' '.join(str(n) for n in range(6)))   # 0 1 2 3 4 5

# Remember, we can deconstruct a string by 'for character in word' and then reassemble using join(). Added a space ' ' for fun.
# print(' '.join(character for character in "A String"))  # A   S t r i n g

# 'character for character in "A String"' should return a generator object.
# Confirmed.
# print(character for character in "A String")    # <generator object <genexpr> at 0x000001ACE8221A80>

# I suspect this will not return something properly. I learned it's not subscriptable.
# print((character for character in "A String")[2])    # Results in TypeError.
    # File "g:\My Drive\Python\PythonLearning\learn_single_line_for.py", line 176, in <module>
    # print((character for character in "A String")[2])    #
    # TypeError: 'generator' object is not subscriptable

# # generator_object = character for character in "A String"    # Lots of squiggle lines. # SyntaxError: invalid syntax
# # Group the generator object together, since it's not read in above example as something useful.
# # Need to group the words together '(character for character in "A String")' to make it coherent.
# generator_object = (character for character in "A String")
# # Reminder: We can join() the elements of a generator object.
# print(' '.join(generator_object))   # A   S t r i n g
