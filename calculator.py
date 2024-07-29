def add(x, y):
    if type(x) and type (y) == int:
        return x + y
    else:
        return "Please enter a numerical value only."


def subtract(x, y):
    if type(x) and type (y) == int:
        return x - y
    else:
        return "Please enter a numerical value only."


def divide(x, y):
    if type(x) and type (y) == int and y != 0:
        return x / y
    else:
        return "Please enter a numerical value only. Ensure the denominator is a non-zero integer, as division by zero is not allowed."
    


def multiply(x, y):
    if type(x) and type (y) == int:
        return x * y
    else:
        return "Please enter a numerical value only."


def square(x):
    if type(x) == int:
        return x * x
    else:
        return "Please enter integer values only"
    


def power(x, y):
    if type(x) and type (y) == int:
        return x ** y
    else:
        return "Please enter a numerical value only."


def sqrt(x):
    if type(x)  == int:
        return x ** 0.5
    else:
        return "Please enter a numerical value only."
