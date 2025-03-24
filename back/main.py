
input_field = ""

def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("U can't divide by zero")
        return a / b
    except ZeroDivisionError as e:
        return e


def multiply(a,b):
    return a * b

def clear(input_field):
    input_field = ""

clear(input_field)

print(divide(2,0))

