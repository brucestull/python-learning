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
        
        # ')'
        if character == ')':
            if number_open >= 1:
                number_open -= 1
                is_valid = True
                continue
            else:
                is_valid = False
                break
        # '('
        elif character == '(':
            number_open += 1
            is_valid = True
            continue
        else:
            is_valid = True
            continue

    if number_open != 0 or not is_valid:
        is_valid = False
    
    elif number_open == 0:
        is_valid = True
    
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