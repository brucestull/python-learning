welcome_string = "\nWelcome to Signature Generator!\n"
print(welcome_string)

# Prompt user for "Author" name.
author_name = input("Enter your name: ")

# Prompt user for 'Project Name'.
project_name = input("Please enter project name: ")

# Prompt user for version number.
version_number = input("Please enter version number: ")

# TODO: Add functionality where user decides whether to auto-populate current date or use manually entered date.
# TODO: Add functionality where date is auto populated by code.
from datetime import date
current_date = date.today()
# # Prompt user for date.
# current_date = input("Please enter the date: ")

# Combine variables into a list so we can determine how wide to make the asterisk lines.
field_list = [author_name, project_name, version_number, str(current_date)]
print(field_list)

field_sizes = []
for item in field_list:
    field_sizes.append(len(str(item)))
print(field_sizes)

# Create variable for how much padding to place on sides of longest character in signature_list.
padding = 4

#
pound_sign = '#'
asterisk = '*'

required_width = max(field_sizes) + padding
print(required_width)

print(pound_sign, asterisk * required_width, pound_sign)
for item in field_list:
    print('  ' + item.center(required_width))
print(pound_sign, asterisk * required_width, pound_sign)
