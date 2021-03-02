from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def index():
    return '<h1>Hello Everyone!</h1> \
        <p>Welcome to this page</p>'