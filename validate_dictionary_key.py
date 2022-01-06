my_dict = {'foo':'bar'}

while True:
    try:
        value = input("Please input dictionary key: ")
        print(my_dict[value])
        break
    except KeyError:
        print('Try again!')
