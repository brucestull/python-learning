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
    # Split the string into elements.
    working_list = string
    # NOTE: A clue, we can't 'close' a set of brackets until they are open.
    # In other words, we need a '(' before ')', '[' before ']', '{' before '}'.
    # Initialize some variables.
    parentheses_open = False
    square_open = False
    squiggle_open = False
    is_valid = True
    last_open = None
    # Loop through working_list.
    # Check for closing brackets which are not paired with opening ones, set is_valid to False.
    for bracket in working_list:
        if bracket == ")" and not parentheses_open:
            is_valid = False
            break
        elif bracket == ']' and not square_open:
            is_valid = False
            break
        elif bracket == '}' and not squiggle_open:
            is_valid = False
            break

        elif bracket == ')' and last_open != '(':
            is_valid = False
            break
        elif bracket == ']' and last_open != '[':
            is_valid = False
            break
        elif bracket == '}' and last_open != '{':
            is_valid = False
            break
        
        elif bracket == ')' and last_open == '(':
            parentheses_open = False
            is_valid = True
        elif bracket == ']' and last_open == '[':
            square_open = False
            is_valid = True
        elif bracket == '}' and last_open == '{':
            squiggle_open = False
            is_valid = True
        
        elif bracket == '(':
            parentheses_open = True
            last_open = '('
            is_valid = True
        elif bracket == '[':
            square_open = True
            last_open = '['
            is_valid = True
        elif bracket == '{':
            squiggle_open = True
            last_open = '{'
            is_valid = True

    return is_valid

# First attempt.
test = '('
# Print return value of the function.
print(valid_braces(test))

# '([(]{})'
'''
bracket = (
    still valid
bracket = [
    still valid
bracket = (
    still valid
bracket = ]
    no longer valid

'''