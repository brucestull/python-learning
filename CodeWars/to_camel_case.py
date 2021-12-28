# https://www.codewars.com/

# Solutions:
#   https://www.codewars.com/kata/reviews/550b3a030681518093000205/groups/550c98e3da6111855d000274

def to_camel_case(text):
    '''This function will convert dash/underscore delimited words into camel casing.'''
    
    list_of_words = None
    working_object = []
    
    # If input string is empty, return an empty string.
    if text == '':
        return ''
    # If input string has dashes, remove them and replace with '*'.
    if '-' in text:
        text = text.replace('-', '*')
    # If input string has underscores, remove them and replace with '*'.
    if '_' in text:
        text = text.replace('_', '*')
    
    # Create list of words.
    list_of_words = text.split('*')
    # Append the first word of the input to the working_object, since it's case wont be changed.
    working_object.append(list_of_words[0])
    
    # Capitalize the first letter of the remaining words of input string.
    for index in range(1, len(list_of_words)):
        working_word = list_of_words[index].capitalize()
        # Add the caplitalized word to the the working_object.
        working_object.append(working_word)
    
    # Join the working_object list into a single string.
    result_string = ''.join(working_object)

    # Return the result string.
    return result_string
