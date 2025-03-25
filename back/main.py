
from flask import Flask,render_template

# from back import main
app = Flask(__name__)

@app.route('/calc',methods=['Post'])
def home():
    return render_template('calc.html')
if __name__ == '__main__':
    app.run(debug=True)

input_field = ""



def add(a,b):
    res = a + b
    append_to_file(add.__name__, res)
    return f"{a} + {b} = {res}"

def minus(a,b):
    res = a - b
    append_to_file(minus.__name__, res)
    return f"{a} - {b} = {res}"

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("U can't divide by zero")
        else :
            res = a / b
            append_to_file(divide.__name__, res)
            return f"{a} / {b} = {res}"
    except ZeroDivisionError as e:
        return e


def multiply(a,b):
    res = a * b
    append_to_file(multiply.__name__, res)
    return f"{a} * {b} = {res}"
#
# def clear(input_field):
#     input_field = ""


def append_to_file(func_name,res):
    with open("history.txt", "a") as file:
        file.write(f"\nWas used {func_name} and result is {res}" )



print(divide(4, 0))