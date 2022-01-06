my_dict = {'foo':'bar'}

while True:
    try:
        value = input("Please input dictionary key: ")  # This line is only requesting input
        print(my_dict[value])   # This line is where the exception is caught
        break
    except KeyError:
        print('Try again!')
