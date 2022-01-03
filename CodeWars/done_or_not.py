# def done_or_not(board): #board[i][j]
#   # your solution here
#   # ..
#   # return 'Finished!'
#   # ..
#   # or return 'Try again!'

# 2-D list (list of lists) review:
# the_2D_list[<row>][<column>]

def done_or_not(board): #board[i][j]
    '''Returns "Finished!" for a completed Sudoku board and "Try again!" for an unfinished board.'''

    result = "Try again!"
    return result

# A row is "valid" if it contains exactly one of each of the numbers 1 through 9.
def row_valid(row_values):
    '''Returns "True" if row is valid, "False" if otherwise.'''
    # Build dictionary.
    row_dictionary = {}
    for element in row_values:
        row_dictionary[element] = row_values.count(element)
    print(row_dictionary)
    result = False
    return result

valid_region = [
    [1, 2, 3]
    ,[2, 3, 1]
    ,[3, 1, 2]
]

invalid_region = [
    [1, 2, 3]
    ,[1, 2, 3]
    ,[3, 1, 2]
]

# row_valid([1, 2, 3])

# The rows are "distinct" when the contents of every row only occurs once.
# No rows exist that are a copy of another row.
def rows_distinct():
    '''Returns True if rows are distinct, False is returned otherwise.'''
    # 
    result = False
    return result

# Learn/review list mappings.
three_by_three = [
    ['a', 'b', 'c']
    ,['d', 'e', 'f']
    ,['g', 'h', 'i']
]

# print(three_by_three)
# # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# for i in range(len(three_by_three)):
#     print(three_by_three[i])
# # ['a', 'b', 'c']
# # ['d', 'e', 'f']
# # ['g', 'h', 'i']

# for i in range(len(three_by_three[0])):
#     print(three_by_three[i])
# # ['a', 'b', 'c']
# # ['d', 'e', 'f']
# # ['g', 'h', 'i']

# for j in range(3):
#     print(three_by_three[0][j])
# # a
# # b
# # c

# for j in range(3):
#     print(three_by_three[j][0])
# # a
# # d
# # g

