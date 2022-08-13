# Import Flask Dependency
from flask import Flask

#Create new Flask app Instance
app = Flask(__name__)

# Define root (starting point)
@app.route('/')
def hello_world():
    return 'Hello world'