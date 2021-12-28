#******************************#
# Project: Programming_102_Unit_02_Practice_Misc
#
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 7, 2021
#******************************#

# Import random module so we can use random.randint().
import random

# Import string module so we can use string methods.
import string

# Define a function which accepts a list and returns a list of the squared value of the elements of the first list.
def get_squares(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

print(get_squares([3, 4, 5]))   # [9, 16, 25]
print(get_squares([7, 8, 9]))   # [49, 64, 81]

# Create a function which takes in a string and returns a string in which each character of the first string is doubled.
def double_string(input_string):
    result = ''
    for character in input_string:
        result += 2 * character
    return result

print(double_string("hello"))   # hheelllloo

# Create a function that uses a loop to build a list of n random single letters from A-Z, where n is a positive integer.
def random_letters(n=8):
    result = []
    index = 0
    while index < n:
        result.append(random.choice(string.ascii_uppercase))
        index += 1
    return result

print(random_letters()) # ['Y', 'T', 'U', 'C', 'O', 'T', 'X', 'K']
print(random_letters(10))   # ['L', 'W', 'A', 'L', 'T', 'I', 'B', 'Q', 'K', 'N']

# Create a function that returns an integer representing the number of vowels in a list or string.
def count_vowels(parameter_01):
    vowels = ['a', 'e', 'i', 'o', 'u']
    the_count = 0
    for item in parameter_01:
        if item.lower() in vowels:
            the_count += 1
    return the_count

print(count_vowels('potato'))   # 3
print(count_vowels('orange'))   # 3
print(count_vowels('mississippi'))   # 4
print(count_vowels('crepuscular'))   # 4

# Create a function that returns a list of n random integers between 1 and 100, where n is a positive integer.
def random_numbers(n = 8, low_number = 1, high_number = 100):
    count = 0
    result = []
    while count < n:
        result.append(random.randint(low_number, high_number))
        count += 1
    return result

print(random_numbers()) # [92, 49, 82, 61, 53, 15, 55, 13]
print(random_numbers(10)) # [20, 26, 9, 21, 9, 32, 27, 89, 57, 11]
print(random_numbers(10, -50, 50)) # [-21, -11, 34, 1, -23, -30, 3, -49, 22, 41]

# Create a function that returns an integer representing the number of positive numbers in a list of numbers.
def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

print(count_positive([7, -5, 1, -5, -9, -10, -7, 9, -2, 2]))        # 4
print(count_positive([-21, -11, 34, 1, -23, -30, 3, -49, 22, 41]))  # 5

