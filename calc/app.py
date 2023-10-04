# Put your app in here.
from operations import add, sub, mult, div

from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_page():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{add(a,b)}"

@app.route('/sub')
def sub_page():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{sub(a,b)}"

@app.route('/mult')
def mult_page():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{mult(a,b)}"

@app.route('/div')
def div_page():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{div(a,b)}"

@app.route('/math/<calc>')
def all_in_one_page(calc):
    calcs = {
        'add': add,
        'sub':sub,
        'div':div,
        'mult':mult
    }
    a = int(request.args['a'])
    b = int(request.args['b'])
    operation = calcs[calc]
    return f"{operation(a,b)}"
    
