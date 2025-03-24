

def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as error:
        return f"U stupid asshole, dont divide by zero"

def clear(input_field):
    input_field = ""
    return input_field


print(divide(2,0))