#******************************#
# Project: Codewars find_it()
#          Find It
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 18, 2021
#******************************#

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
    # [7] should return 7, because it occurs 1 time (which is odd).
    # [0] should return 0, because it occurs 1 time (which is odd).
    # [1,1,2] should return 2, because it occurs 1 time (which is odd).
    # [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
    # [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# This is initial attempt.
# This solution is more complicated than it needs to be.
# Seek out new solutions.

def find_it(seq):
    result = None
    
    # Iterate over seq and count how many times the value of each element occurs in the sequence.
    list_of_count = []
    for index in range(len(seq)):
        list_of_count.append(seq.count(seq[index]))

    # Create a list to hold if each element occurs odd number of times.
    list_of_odd = []
    for index in range(len(list_of_count)):
        list_of_odd.append(list_of_count[index] % 2 == 1)
    
    # Iterate over list_of_odd and return the value of the element of seq which occurs at same position as 'True'.
    for index in range(len(list_of_odd)):
        if list_of_odd[index] == True:
            result = seq[index]
            break

    return result

print(f'''
{find_it([1, 1, 2, 2, 5])}
''')
