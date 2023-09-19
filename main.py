import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def addRoute():
    return add(num1, num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtractRoute():
    return subtract(num1, num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiplyRoute():
    return multiply(num1, num2)

@app.route('/divide/<int:num1>/<int:num2>')
def divideRoute():
    return divide(num1, num2)

@app.route('/mod/<int:num1>/<int:num2>')
def mod():
    return mod(num1,num2)
  
#addition function

def add(a,b):
	return a+b
	
#subtraction function

def subtract(a,b):
	return a-b
