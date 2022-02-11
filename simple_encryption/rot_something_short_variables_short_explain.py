
dictionary_outside = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
           "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
           }


# NOTE: Your 'index' function in app.py does not need any 'parameter's to be passed into it's function signature.
# We can just use any 'outside' variables and such on the 'inside' of the 'index' function.
# It's one of the few exceptions where we don't put the outside variables into the parentheses.
# NOTE: We do not need to change any of the words inside THIS function to 'match' any words outside.
def encrypt_or_decrypt(word_inside, dictionary_inside):
    '''WORD_INSIDE is the word to be encrypted or decrypted. DICTIONARY_INSIDE is the ROT-13 dictionary used for encryption-decryption.'''
    list_inside = []
    for character_inside in word_inside:
        list_inside.append(dictionary_inside[character_inside])
    encrypted_word_inside = ''.join(list_inside)
    return encrypted_word_inside


word_to_encrypt = "bigcat"
# PRINT IS USED HERE ONLY FOR TESTING!
print(word_to_encrypt)


# 'word_to_encrypt' becomes 'word_inside'
# 'dictionary_outside' becomes 'dictionary_inside'
# 'encrypt_or_decrypt' does it's logic work.
# 'encrypted_word_inside', on line 16, becomes 'encrypted_word_outside'
encrypted_word_outside = encrypt_or_decrypt(word_to_encrypt, dictionary_outside)


# PRINT IS USED HERE ONLY FOR TESTING!
print(encrypted_word_outside)


# 'encrypted_word_outside' becomes 'word_inside'
# 'dictionary_outside' , again, becomes 'dictionary_inside'
# 'encrypt_or_decrypt' does it's logic work.
# 'encrypted_word_inside', on line 16, becomes 'decrypted_word_outside'
decrypted_word_outside = encrypt_or_decrypt(encrypted_word_outside, dictionary_outside)


# PRINT IS USED HERE ONLY FOR TESTING!
print(decrypted_word_outside)
