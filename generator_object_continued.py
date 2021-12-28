#******************************#
# Project: Generator Object
#
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 19, 2021
#******************************#

# List comprehension is probably a better description. Even though the created object is a generator object, the thing created might be a list or similar.
# Link to list comprehension: https://www.programiz.com/python-programming/list-comprehension

# return f(g(h() + <value>) for <index of object> in <object> if <condition>)
# return ' '.join(str(string.ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
# return ' '.join(<next_line>)
#     str(<next_line>) for n in text if n.isalpha()
#     string.ascii_lowercase.index(<next_line>) + 1
#     n.lower()

#     y = n.lower()                               # Take 'n' and lower() it. This is 'y'
#     z = string.ascii_lowercase.index(y) + 1     # Find the the index of 'y' in string.ascii_lowercase. This is z.
#     M = str(z) for n in text if n.isalpha()     # Make a sequence of str(z) for each element n in text if n is alpha. The sequence of elements/items is compose M.
#     N = ' '.join(M)                             # Perform a .join() operation on all the elements of M. This is N.

# We do the operation <str(string.ascii_lowercase.index(n.lower()) + 1)> on each <n> in text whenever <n> .isalpha().

# <Some operation on 'n'> for 'n' in 'text' if 'n' .isalpha().

################### BIG THING #######################################
# Do f(n) for all the n in N according to condition(n).
# f(n) for <n> in <N> if <condition(n)>
################### BIG THING #######################################

N = [1, 2, 3, 4, 5]
print([n**2 for n in N if n % 2 == 1])  # [1, 9, 25]

print([[n] + [n] for n in N if n % 2 == 1]) # [[1, 1], [3, 3], [5, 5]]

print([(str(n), 2 * str(n)) for n in N if n % 2 == 1])  # [('1', '11'), ('3', '33'), ('5', '55')]







    # f(x) = join(x) ; g(x) = str(x) ; h(x) = string.ascii_lowercase.index(x.lower()) + 1 ; 
    # f(g(h(x)) for x in <object> if x.isalpha())
