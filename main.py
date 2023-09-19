from flask import Flask

app = Flask(__name__)

# Addition function
def add(a, b):
    return a + b

# Subtraction function
def subtract(a, b):
    return a - b

# Multiplication function
def multiply(num1, num2):
    return num1 * num2

# Division function
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

# Modulus function
def mod(num1, num2):
    return num1 % num2

@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def addRoute(num1, num2):
    return str(add(num1, num2))

@app.route('/subtract/<int:num1>/<int:num2>')
def subtractRoute(num1, num2):
    return str(subtract(num1, num2))

@app.route('/multiply/<int:num1>/<int:num2>')
def multiplyRoute(num1, num2):
    return str(multiply(num1, num2))

@app.route('/divide/<int:num1>/<int:num2>')
def divideRoute(num1, num2):
    return str(divide(num1, num2))

@app.route('/mod/<int:num1>/<int:num2>')
def modRoute(num1, num2):
    return str(mod(num1, num2))

if __name__ == '__main__':
    app.run(debug=True)
