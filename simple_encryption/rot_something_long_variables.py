
dict = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
           "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
           }


def encrypt_or_decrypt(word_is_now_inside_the_function, encryption_dictionary_is_now_inside_the_function):
    '''We use capital letters in the next line to signify the specific values of the input parameters.'''
    '''WORD_IS_NOW_INSIDE_THE_FUNCTION is the word to be encrypted or decrypted. ENCRYPTION_DICTIONARY_IS_NOW_INSIDE_THE_FUNCTION is the ROT-13 dictionary used for encryption-decryption.'''
    working_list_is_inside_the_function = []
    for character_is_inside_the_function in word_is_now_inside_the_function:
        working_list_is_inside_the_function.append(encryption_dictionary_is_now_inside_the_function[character_is_inside_the_function])
    the_final_word_is_inside_the_function = ''.join(working_list_is_inside_the_function)
    return the_final_word_is_inside_the_function

word_to_encrypt = "bigcat"
print(word_to_encrypt)

# Encrypt the word using the function encrypt_or_decrypt:
the_encrypted_word_outside_the_function = encrypt_or_decrypt(word_to_encrypt, dict)
print(the_encrypted_word_outside_the_function)

# Decrypt the word using the function encrypt_or_decrypt:
the_new_encrypted_word_outside_the_function = encrypt_or_decrypt(the_encrypted_word_outside_the_function, dict)
print(the_new_encrypted_word_outside_the_function)

print('word_to_change'.upper())