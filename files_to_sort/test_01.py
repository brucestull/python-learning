def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for n in range(5):
    print(fibonacci(n))

print(fibonacci(int(input("PLease enter number to fibonacci: "))))