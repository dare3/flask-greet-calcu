# Put your app in here.
from flask import Flask,request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = add(a,b)
    return str(result)


@app.route("/sub")
def do_sub():
    """subtract a and b parameters."""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = sub(a,b)

    return str(result)


@app.route("/mult")
def do_mult():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = mult(a,b)

    return str(result)


@app.route("/div")
def do_div():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    result = div(a,b)

    return str(result)
#further study 
operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<operate>")
def do_math(operate):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[operate](a, b)

    return str(result)

