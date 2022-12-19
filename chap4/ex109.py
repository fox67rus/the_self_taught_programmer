try:
    a = input("Input first number: ")
    b = input("Input second number: ")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Input error! Enter numbers greater than 0")
