#******************************#
# Project: Codewars valid_braces()
#          Find It
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 28, 2021
#******************************#

# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Results:
    # False, if there are any *_open flags still False at the end of the list.
    # False, if any specific closing bracket occurs which hasn't been preceded by opening bracket.

# Examples - True:
# ()
# {}
# []
# {{}}
# {[]}
# ({[]})
# ({}[])
# ([{}])
# (({{[[]]}}))

# Examples - False:
# (}
# ({)
# (])
# ({}])
# ([{})
# ({[(])]})
# ({[(])]})

# Invalids:
    # If bracket is closing bracket:
        # If previous bracket is an opening bracket and previous bracket was of different type:
            # result = False
            # break
        # If bracket is a closing bracket and bracket_type_open == False:
            # result = False
            # break
    # If number open != number closed
        # result = False
    
def validBraces(string):
    '''The function returns False if sequence of brackets is invalid and True if sequence is valid.'''
    parentheses_open = 0
    square_open = 0
    squiggle_open = 0

    last_open = None

    for index in range(len(string)):

        if string[index] == '(':
            parentheses_open += 1
            result = True
            last_open = string[index]
            if index == len(string) - 1:
                break
            if string[index + 1] in [']', '}']:
                result = False
                break
            else:
                result = True
        elif string[index] == '[':
            square_open += 1
            result = True
            last_open = string[index]
            if index == len(string) - 1:
                break
            if string[index + 1] in [')', '}']:
                result = False
                break
            else:
                result = True
        elif string[index] == '{':
            squiggle_open += 1
            result = True
            last_open = string[index]
            if index == len(string) - 1:
                break
            if string[index + 1] in [')', ']']:
                result = False
                break
            else:
                result = True
        
        elif string[index] == ')':
            # if parentheses_open < 1 or last_open != '(':
            if parentheses_open < 1:
                result = False
                parentheses_open -= 1
                break
            else:
                parentheses_open -= 1
                result = True
        elif string[index] == ']':
            # if square_open < 1 or last_open != '[':
            if square_open < 1:
                result = False
                square_open -= 1
                break
            else:
                square_open -= 1
                result = True
        elif string[index] == '}':
            # if squiggle_open < 1 or last_open != '{':
            if squiggle_open < 1:
                result = False
                squiggle_open -= 1
                break
            else:
                squiggle_open -= 1
                result = True
    
    if parentheses_open != 0 or square_open != 0 or squiggle_open != 0:
        result = False
    else:
        result = True
    
    return result

# (((({{
# string_sequence = '([{}])'
string_sequence = '(((({{'
print(f'''
{string_sequence} is valid: {validBraces(string_sequence)}
''')








def validBraces_v1(string_sequence):
    # Use a loop and adjacent_valid to determine if sequence is valid.
    result = True
    for index in range(len(string_sequence) - 1):
        if string_sequence[index] not in ['(', '[', '{']:
            result = True
            continue
        else:
            # print(adjacent_valid(string_sequence[index], string_sequence[index + 1]))
            opening_bracket = string_sequence[index]
            closing_bracket = string_sequence[index + 1]
            
            if opening_bracket == '(':
                if closing_bracket == ']' or closing_bracket == '}':
                    result = False
                    break
                else:
                    result = True
            elif opening_bracket == '[':
                if closing_bracket == ')' or closing_bracket == '}':
                    result = False
                    break
                else:
                    result = True
            elif opening_bracket == '{':
                if closing_bracket == ')' or closing_bracket == ']':
                    result = False
                    break
            else:
                result = True
    return result
