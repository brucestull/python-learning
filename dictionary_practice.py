#******************************#
# Project: Dictionary practice
#
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 6, 2021
#******************************#

import random

# Initialize dictionaries. This isn't neccesarily neccessary, the memory allotment for program space is reset each time script is run. 'car' 'rps' are non-existent.
car = {}
rps = {}

# Create a dictionary for a car.
car = {
  'brand': "Ford",
  'model': "Mustang",
  'year': 1964
}

# Alt way create dictionary. The above format can be a little easier to read.
# car = {'brand': "Ford",'model': "Mustang",'year': 1964}

# print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Add a 'color' entry to the 'car' dictionary.
car['color'] = ['red', 'white', 'blue']

# Print out the entire dictionary. The 'color' entry (list) now shows up in 'car'.
# print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': ['red', 'white', 'blue']}

# Print out the value of the 'brand' entry. Select the key 'brand' for the brand of 'car'.
# print(car['brand']) # Ford

# Create rock paper scissors dictionary.
rps = {
  'rock': ['paper', 'scissors'],
  'paper': ['scissors', 'rock'],
  'scissors': ['rock', 'paper']
}

# What is size of dictionary?
# print(len(car)) # 4
# print(len(rps)) # 3

# What is the type of class for a dictionary?
# print(type(car))  #<class 'dict'>

# Specify some variables.
model_of_car = car['model'] # or car.get('model')
color_of_car = car['color'] # or car.get('color')

# Print some variables.
# print(model_of_car) # Mustang
# print(color_of_car) # ['red', 'white', 'blue']

# What are the keys of the 'car' dictionary?
keys_of_car = car.keys()
# print(keys_of_car)  # dict_keys(['brand', 'model', 'year', 'color'])

# What are the values of the 'car' dictionary?
values_of_car = car.values()
# print(values_of_car)  # dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue']])

# Weirdness:
x = car.values()    # https://www.w3schools.com/python/python_dictionaries_access.asp indicates that the returned list (of car.values()) is a 'view'. So, maybe whenever 'x' is used, 'car.values()' is used in 'x's place?
# print(x)  # dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue']])
car['year'] = 2020
# print(x)  # dict_values(['Ford', 'Mustang', 2020, ['red', 'white', 'blue']])            # The value of 'x' changes, even though we didn't have to re-assign it to car.values().

# print(car.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', ['red', 'white', 'blue'])])  # Returns  each item in the dictionary as tuples in a list.

# Check if key 'model' exists for 'car'.
# if 'model' in car:
#   print("Yes, 'model' is a key for 'car'.")

# Change a value of the dictionary.
car['year'] = 1970
# print(car['year'])
car.update({'year': 2015})
# print(car['year'])

# Add an item to dictionary.
car['seats'] = 5
# print(car.items())
car.update({'wheels': 4})
# print(car.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2015), ('color', ['red', 'white', 'blue']), ('seats', 5), ('wheels', 4)])

# Remove an item from dictionary.
car.pop('wheels')
# print(car.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2015), ('color', ['red', 'white', 'blue']), ('seats', 5)])

# Add wheels again.
car.update({'wheels': 4})
# print(car.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2015), ('color', ['red', 'white', 'blue']), ('seats', 5), ('wheels', 4)])

# Remove last item interted.
car.popitem() # Removes the last item inserted.
# print(car.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2015), ('color', ['red', 'white', 'blue']), ('seats', 5)])
car.update({'wheels': 4})

# Remove item of key 'model'.
del car['model']
# print(car.items())
car.update({'model': 'Junker'})
# print(car.items())

# Delete whole dictionary.
# del car
# print(car) # Will result in error since dictionary doesn't exist anymore.

# Clear the dictionary.
# car.clear()
# print(car)

# # clear()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# thisdict.clear()
# print(thisdict)

# Print all key names in 'car'.
# for item in car:
#   print(item)

# Print all the values in 'car'.
# for item in car:
#   print(car[item])

# List all the values of the 'car'.
# for item in car.values():
#   print(item)

# List all the keys of 'car'.
# for item in car.keys():
#   print(item)

# Loop through both keys and values.
# for key, value in car.items():
#   print(key, value)

# Copy a dictionary.
copy_of_car = car.copy()  # Makes a copy of 'car' and names it 'copy_of_car'.
pointer_to_car = car  # Only creates a reference to 'car'.

# print(copy_of_car)
# print(pointer_to_car)
# print(car)

car.update({'seats': 4})  # Affects both 'car' and 'pointer_to_car'.

# print(copy_of_car)
# print(pointer_to_car)
# print(car)

# Copy a dictionary, using dict().
second_car_copy = dict(car)
# print(car)
# print(second_car_copy)

# Nested dictionaries.
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# OR

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# print(family) # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
# print(family['child1']) # {'name': 'Emil', 'year': 2004}
# print(family['child1']['name']) # Emil
# print(family[0])  # KeyError: 0

# print(car)  # {'brand': 'Ford', 'year': 2015, 'color': ['red', 'white', 'blue'], 'seats': 4, 'wheels': 4, 'model': 'Junker'}
# print(car['color'][0], car['model'])  # red  # This works since the key 'color' has a value which is a list so we can access the list elements with position numbers.

# List of some Python Dictionary Methods: https://www.w3schools.com/python/python_dictionaries_methods.asp
