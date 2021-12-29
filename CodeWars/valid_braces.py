#******************************#
# Project: Codewars valid_braces()
#          Find It
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 28, 2021
#******************************#

# Results:
    # False, if there are any *_open flags still False at the end of the list.
    # False, if any specific closing bracket occurs which hasn't been preceded by opening bracket.

# Define the function.
def valid_braces(string):
    if string == '(':
        is_valid = False
    return is_valid

test = '('
print(valid_braces(test))