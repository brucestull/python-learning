# A Narcissistic Number is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcisstic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether
# the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid
# positive non-zero integers will be passed into the function.

def narcissistic(input_integer):
    '''Returns True for narcissistic numbers and False if not narcissistic.'''
    
    ###############################
    # Non-good method.
    ###############################
    input_integer_to_string = str(input_integer)
    # print(f"{input_integer_to_string} is type {type(input_integer_to_string)} of length {len(input_integer_to_string)}")
    number_digits = len(input_integer_to_string)
    input_as_list_of_strings = list(input_integer_to_string)
    # print(input_as_list_of_strings)
    sum_of_powers = 0
    for string in input_as_list_of_strings:
        sum_of_powers += int(string)**number_digits
    ###############################

    if input_integer == sum_of_powers:
        result = True
    else:
        result = False
    
    return result

test_value = 133
print(f'''
{test_value} has narcissistic status of {narcissistic(test_value)}
''')
