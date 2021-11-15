# Import module
from flask import Flask, request
import intra


app = Flask(__name__)

@app.route('/', methods=['GET'])
def query():
    intra.intra_function()