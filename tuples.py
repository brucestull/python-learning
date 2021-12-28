#******************************#
#   Project: Tuples practice
#
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 22, 2021
#******************************#

# Do we need parentheses to wrap around the tuple? No error when compiled.
cat = 'fuzzy', 'furry', 'purry'

# Define tuple over multiple lines. '\' is used to spread command over multiple lines.
# There may be cases where one form is preferred over the other.
dog =\
    'bad',\
    'barky',\
    'bitey'

print(dog)  # ('bad', 'barky', 'bitey')

# Can we print the tuple? Yes. NOTE: tuple is wrapped in ().
# print(cat)  # ('fuzzy', 'furry')

# Can we index elements of a tuple? Yes, the returned string doesn't have '' wrapping it.
# The '', which usually wraps each element, only shows up when we return the list or tuple of strings.
# print(cat[0])   # fuzzy
# print(cat)      # ('fuzzy', 'furry', 'purry')

# Can we iterate over a tuple?
# for element in cat:
#     print(element)
#     # fuzzy
#     # furry
#     # purry

# Can we apply generator object here? The tuple has been converted to a list.
# print([element for element in cat]) # ['fuzzy', 'furry', 'purry']

