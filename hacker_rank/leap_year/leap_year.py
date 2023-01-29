def is_leap(year):
    leap = False
    
    # If year is evenly divisible by 4:
    if year % 4 == 0:
        # If year is evenly divisible by 100:
        if year % 100 == 0:
            # If year is evenly divisible by 400:
            if year % 400 == 0:
                leap = True
            # Don't need `else` here because `leap` is already `False`.
        else:
            leap = True
    
    return leap

if __name__ == '__main__':
    print("Welcome to Leap Year Checker!")
    year = int(input("Please enter a year: "))
    print(f'is_leap({year}): ', is_leap(year))