# Put your app in here.
from operations import *
from flask import Flask, request
# from operations import add

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome home!"

# *****************
# THE WET WAY
# *****************


@app.route('/search')
def search():
    operation = request.args["operation"]
    a = request.args["a"]
    b = request.args["b"]
    operation, a, b = {operation, a, b}
    return operation(a, b)


@app.route('/add')
def do_math1():
    a = request.args["a"]
    b = request.args["b"]
    result = add(int(a), int(b))
    return f"{result}"


@app.route('/sub')
def do_math2():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return f"{result}"


@app.route('/mult')
def do_math3():
    a = request.args["a"]
    b = request.args["b"]
    result = mult(int(a), int(b))
    return f"{result}"


@app.route('/div')
def do_math4():
    a = request.args["a"]
    b = request.args["b"]
    result = div(int(a), int(b))
    return f"{result}"


# *****************
# A MORE DRY WAY
# *****************
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/math/<operator>')
def do_math(operator):
    a = int(request.args["a"])
    b = int(request.args["b"])
    oper = operators.get(operator, "Operator not found")
    result = oper(a, b)
    return str(result)
