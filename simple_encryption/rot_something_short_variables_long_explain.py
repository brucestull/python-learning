
dictionary_outside = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
           "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
           }

# NOTE: ALL THESE WORDS WITH '_inside' ARE ONLY USED INSIDE THE FUNCTION.
# WE ARE SPECIFYING THE NAMES HERE WHEN WE 'def'INE THE FUNCTION.
# THERE IS NO NEED TO EVER CHANGE THESE NAMES WHEN WE USE THE FUNCTION. NEVER NEVER NEVER!!! ALMOST? LOL! LOL!
def encrypt_or_decrypt(word_inside, dictionary_inside):
    '''We use capital letters in the next line to signify the specific values of the input parameters, WHEN WE 'CALL' THE FUNCTION.'''
    '''The lower-case variables are the ones inside the function.'''
    '''WORD_INSIDE is the word to be encrypted or decrypted. DICTIONARY_INSIDE is the ROT-13 dictionary used for encryption-decryption.'''
    list_inside = []
    for character_inside in word_inside:
        list_inside.append(dictionary_inside[character_inside])
    encrypted_word_inside = ''.join(list_inside)
    return encrypted_word_inside


################################
# Here, we are specifying
# a test word to encrypt.
word_to_encrypt = "bigcat"
# NOTE: WE ARE ONLY PRINTING THE THING HERE 
# TO SHOW THE VALUE OF THE VARIABLE. THIS
# PRINT STATEMENT PERFORMS NO LOGIC USEFUL
# TO OUR GOAL. IT IS ONLY PRINTING OUT THE
# VALUE SO WE CAN SEE IT WHILE TESTING.
print(word_to_encrypt)
################################


################################
# When we say 'pass the variable to the function':
# NOTE: 'word_to_encrypt' becomes 'word_inside'
# NOTE: 'dictionary_outside' becomes 'dictionary_inside'
# NOTE: WE DO NOT EDIT THE STUFF INSIDE THE
# FUNCTION INTO THE WORDS USED OUTSIDE THE FUNCTION.
# THE FUNCTION DOES ALL THAT WORK FOR US.
################################



# 'word_to_encrypt' and 'dictionary_outside' are passed into 'encrypt_or_decrypt',
# the return value of 'encrypt_or_decrypt' is set to 'encrypted_word_outside'.
encrypted_word_outside = encrypt_or_decrypt(word_to_encrypt, dictionary_outside)
# NOTE: WE ARE ONLY PRINTING THE THING HERE 
# TO SHOW THE VALUE OF THE VARIABLE. THIS
# PRINT STATEMENT PERFORMS NO LOGIC USEFUL
# TO OUR GOAL. IT IS ONLY PRINTING OUT THE
# VALUE SO WE CAN SEE IT WHILE TESTING.
print(encrypted_word_outside)

decrypted_word_outside = encrypt_or_decrypt(encrypted_word_outside, dictionary_outside)
# NOTE: WE ARE ONLY PRINTING THE THING HERE 
# TO SHOW THE VALUE OF THE VARIABLE. THIS
# PRINT STATEMENT PERFORMS NO LOGIC USEFUL
# TO OUR GOAL. IT IS ONLY PRINTING OUT THE
# VALUE SO WE CAN SEE IT WHILE TESTING.
print(decrypted_word_outside)

print('dictionary_inside'.upper())