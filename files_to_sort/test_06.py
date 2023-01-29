# ************************* #
#      Pytest Learning      #
#   Trying out some stuff   #
#        Version: 1.0       #
#    Author: Bruce Stull    #
#         2022-01-06        #
# ************************* #

# GOAL
# Ones Digit
# Write a function that returns the ones digit of a number

# print(len(str(10)))

# print('56'[1])

print(f'''
True and True:  {True and True}
True and False: {True and False}
False and True: {False and True}
False and False:{False and False}
''')

# True and True:  True
# True and False: False
# False and True: False
# False and False:False

print(f'''
True or True:  {True or True}
True or False: {True or False}
False or True: {False or True}
False or False: {False or False}
''')

# True or True:  True
# True or False: True
# False or True: True
# False or False:False

# print(' '.upper())

# def loud_text(text):
#     return text.upper().replace('', '_')

# print(loud_text('hello'))

# the_list = ['f', 'b', 'h']
# the_list.sort()
# print(the_list)

text = 'hihi hh hillh'
result = 0
for i, character in enumerate(text):
    # Break out of loop at end so we don't have an index out of range.
    if i == len(text) - 1:
        break
    # Check if i follows an h.
    if character == 'h':
        if text[i + 1] == 'i':
            result += 1
print(result)
