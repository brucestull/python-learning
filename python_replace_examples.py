# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3/library/stdtypes.html#str.replace
# str.replace(old, new[, count])
    # Return a copy of the string with all occurrences of substring old replaced by new. 
    # If the optional argument count is given, only the first count occurrences are replaced.

text01 = "abcdef"
text02 = "ab-cd_ef"

# ---------------------------------------------------------------------- #
# str.replace() will return a new string. The method does not modify the original str object.

# This will print out the modified input string but the resultant string will not be saved.
print(text02.replace('-', '*')) # ab*cd_ef # Print out the modified string but it's not being saved.
print(text02)                   # ab-cd_ef # Original string not changed.

# ---------------------------------------------------------------------- #
# Save the returned string to new variable and print result.
# We now have one named storage space of 'text02' containing orginal string and a new named storage space 'result' which contains the new string.
result = text02.replace('-', '*')
print(result) # ab*cd_ef

# ---------------------------------------------------------------------- #
# It seems that if 'old' is not present in 'str', then original 'str' is returned. The method doesn't error if 'old' isn't present in 'str'.
result = text01.replace('-', '*')
print(result) # abcdef

# ---------------------------------------------------------------------- #
# We can chain the replace() method since each returned value of the method is a string.
result = text02.replace('-', '*').replace('_', '*')
print(result)   # ab*cd*ef

# ---------------------------------------------------------------------- #
# TODO: Need to work some examples using 'count'.

# Lessons learned:
    # Some methods take an object, perform operations on it, and return a new object with new value, but the original object is unchanged.
    # Some methods take an object and modify the original object and return a None.