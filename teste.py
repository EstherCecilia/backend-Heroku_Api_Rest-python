# -*- coding: cp1252 -*-
from flask import Flask, request

app = Flask(__name__)
api = Api(app)



@app.route('/')
def pessoas():
        return "Hello"

    
if __name__ == '__main__':
    app.run()

    
#debug=true
