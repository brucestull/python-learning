# ************************ #
#   Create New Test File   #
#     Uses: os module      #
#       Version: 1.0       #
#   Author: Bruce Stull    #
#        2022-01-06        #
# ************************ #

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

## Make a list of things in a directory.
# Import needed module.
import os
# Use os.listdir() to get the list of files/directories in the current working directory.
# arr = os.listdir('<path\\to\\search\\>')
arr = os.listdir('.\\')

# Loop through list and display the files which start with 'test_'.
for item in arr:
    if item.startswith('test_'):
        print(item)

# Loop through list arr, if element starts with 'test_', remove 'test_' from the element and append the string to versions.
versions = []
for item in arr:
    if item.startswith('test_'):
        versions.append(int(item.replace('test_','').replace('.py', '')))

print(versions)

# working_file = open("test_05.py", mode='a', encoding = 'utf-8')
# working_file.write("# First line in\n")
# working_file.close()
