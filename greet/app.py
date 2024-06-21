from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet():
    return "<h1>WELCOME</h1>"

@app.route("/welcome/home")
def welcome():
    return "<h1> Welcome, home!</h1>"

@app.route("/welcome/back")
def welcome_back():
    return "<h1> Welcome, back~~~</h1>"