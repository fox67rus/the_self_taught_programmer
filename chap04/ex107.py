a = input("Input first number: ")
b = input("Input second number: ")

a = int(a)
b = int(b)

try:
    print(a/b)
except ZeroDivisionError:
    print("The second number must be greater than 0")