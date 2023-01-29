# Second edit.
# Added feature_01.
# Create two nested 'for' loops.
for x in range(1,5):
    print(f"Start of x:{x} loop.")
    for y in range(1,5):
        print(f"Start of y:{y} loop.")
        if y == 3:
            print(x, y, 'breaking')
            # print("Only 'break' out of inner 'y' loop.")
            break
        else:
            print(x, y, f"continuing. AKA end of y:{y} loop." )
            # print("Will this start at beginning of 'y' loop?")
            continue
        # Code here not reacheable since following 'if' -> 'else'.
        print("Code here not reacheable since following 'if' -> 'else'.")
    print("Just finished all the 'y' loops.")
    print(f"Also, just finished x:{x} loop.")
print("Just finished all the 'x' loops.")
