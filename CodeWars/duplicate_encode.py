#******************************#
# Project: Codewars duplicate_encode()
#    Duplicate encode
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 16, 2021
#******************************#

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

def duplicate_encode(word):
    '''This function: The goal of this exercise is to convert a string to a new string
    where each character in the new string is "(" if that character appears only once
    in the original string, or ")" if that character appears more than once in the original
    string. Ignore capitalization when determining if a character is a duplicate.'''

    # Convert any upper case alpha characters to lower case since we are ignoring case of alpha characters.
    # Initialize working string.
    working_string = ''
    # Iterate over the 'word'.
    for character in word:
        # Lower each character of 'word' and add to 'working_string'.
        working_string += character.lower()
    
    # Initialize result string.
    result = ''
    # Iterate over 'working_string'.
    for character in working_string:
        # If 'character' occurs only once:
        if working_string.count(character) == 1:
            # Add the appropriate character '(' to result string.
            result += '('
        # Otherwise (character occurs more than once):
        else:
            # Add the appropriate character ')' to result string.
            result += ')'
    
    # Return the result string.
    return result


string_to_encode = "A Simple strIng"
expected_result =  "()))(((())(()(("

print(f'''
'{string_to_encode}'
'{duplicate_encode(string_to_encode)}'
'{expected_result}'
''')
