#******************************#
# Project: Codewars valid_parentheses()
#          Find It
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 28, 2021
#******************************#

# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Define the function.
def valid_parentheses(input_string):
    '''Returns True for a valid order of parentheses and False for an invalid order of parentheses.'''
    number_open = 0
    is_valid = True
    
    # Evaluate each character.
    for character in input_string:
        
        # If character is ')':
        if character == ')':
            # If there is already one or more opening parentheses:
            if number_open >= 1:
                # Reduce number of unclosed parentheses by one.
                number_open -= 1
                # Sequence is currently valid.
                is_valid = True
                # Go to beginning of loop and check next character.
                continue
            # If there are no opening parentheses before this closing one:
            else:
                # Sequence is invalid.
                is_valid = False
                # Break out of loop.
                break
        
        # Check if character is '(':
        elif character == '(':
            # Add one to the number of open parentheses.
            number_open += 1
            # Sequence is valid.
            is_valid = True
            # Continue to next character.
            continue
        # Otherwise, character is not either parentheses.
        else:
            # Sequence is valid. Letters and numbers are okay.
            is_valid = True
            # Continue to next character.
            continue
    
    # If there are any open parentheses or sequence has already determined to be invalid:
    if number_open != 0 or not is_valid:
        # Set flag as False.
        is_valid = False
    
    # If all open parentheses have been closed.
    elif number_open == 0:
        # Sequence is valid.
        is_valid = True
    
    # Return the validity status.
    return is_valid

test = ''
# print(valid_parentheses(test))



# Summary:
print(f'''
Summary:
Input string: '{test}'
String is valid: {valid_parentheses(test)}
''')

# for character in test:
#     print(character)