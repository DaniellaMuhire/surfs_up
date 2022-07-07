# import flask dependency
from flask import Flask
# flask instance
app = Flask(__name__)
#first route
#starting point known as root
@app.route('/')
def hello_world():
    return 'Hello world'
