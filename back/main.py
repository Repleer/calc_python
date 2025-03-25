from flask import Flask, render_template, request,jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operation"]
            if operator == "+":
                result = add(num1,num2)
            elif operator == "-":
                result = minus(num1,num2)
            elif operator == "x":
                result = multiply(num1,num2)
            elif operator == "/":
                result = divide(num1,num2)
            else:
                result = "invalid ti invalid"

            return jsonify({"result": result})
    return render_template("calc.html")
def add(a, b):
    res = a + b
    append_to_file("add", res)
    return f"{a} + {b} = {res}"

def minus(a, b):
    res = a - b
    append_to_file("minus", res)
    return f"{a} - {b} = {res}"

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    res = a / b
    append_to_file("divide", res)
    return f"{a} / {b} = {res}"

def multiply(a, b):
    res = a * b
    append_to_file("multiply", res)
    return f"{a} * {b} = {res}"

def append_to_file(func_name, res):
    with open("history.txt", "a") as file:
        file.write(f"\n{func_name} used, result: {res}")

if __name__ == "__main__":
    app.run(debug=True)
