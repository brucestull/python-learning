# def done_or_not(board): #board[i][j]
#   # your solution here
#   # ..
#   # return 'Finished!'
#   # ..
#   # or return 'Try again!'

def done_or_not(board): #board[i][j]
    '''Returns "Finished!" for a completed Sudoku board and "Try again!" for an unfinished board.'''

    result = "Try again!"
    return result

def row_valid(row_values):
    '''Returns "True" if row is valid, "False" if otherwise.'''
    # Build dictionary.
    row_dictionary = {}
    for element in row_values:
        row_dictionary[element] = row_values.count(element)
    print(row_dictionary)
    result = False
    return result

# # Learn/review list mappings.
# three_by_three = [['a', 'b', 'c']
# ,['d', 'e', 'f']
# ,['g', 'h', 'i']]

# print(three_by_three)
# # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# for i in range(len(three_by_three)):
#     print(three_by_three[i])
# # ['a', 'b', 'c']
# # ['d', 'e', 'f']
# # ['g', 'h', 'i']

row_valid([1, 2, 3])