# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *

app = Flask(__name__)
api = Api(app)



@app.route('/', methods=['GET'])
def pessoas(id):
    if request.method == 'GET' :
        return "Hello"

    
if __name__ == '__main__':
    app.run()

    
#debug=true
