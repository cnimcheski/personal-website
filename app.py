from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # should return the index route...
    return "hello, world"