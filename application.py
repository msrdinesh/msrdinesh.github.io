from flask import Flask

app = Flask(__name__)


@app.route("/")

def index():
    return "hello world!"

@app.route("/<string:name>")

def name(name):
    name = name.capitalize()
    return "<h1>hello {}!</h1>".format(name)
    
