from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet():
    return "Welcome"

@app.route("/welcome/home")
def welcome_home():
    return "Welcome home"

@app.route("/welcome/back")
def welcome_back():
    return "Welcome back"

