def valid_parentheses(input_string):
    '''Returns True for a valid order of parentheses and False for an invalid order of parentheses.'''
    number_open = 0
    is_valid = True
    
    for character in input_string:
        
        if character == ')':
            if number_open >= 1:
                number_open -= 1
                is_valid = True
                continue
            else:
                is_valid = False
                break
        
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

test = '(()())'



print(f'''
Summary:
Input string: '{test}'
String is valid: {valid_parentheses(test)}
''')

