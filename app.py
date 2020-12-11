
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from flask import Flask, request, jsonify, Response, abort, make_response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os

# Local import
import string_util as su


app = Flask(__name__)
api = Api(app)


'''
    http://localhost:8071/
'''
@app.route("/")
def main():

    result_dict = {
        "result" : "welcome"
    }

    return make_response(jsonify(result_dict), 200)


'''
    http://localhost:8071/env
'''
@app.route("/env")
def show_env():

    env = int(os.environ.get('WORKER_SMTP_PORT', '28'))

    result = {
        'env' : env
    }

    return make_response(jsonify(result), 200)

'''
    http://localhost:8071/reverse

    http://localhost:8071/reverse?content=hello
'''
@app.route("/reverse")
def reverse_string_api():

    content = request.values.get('content')

    print('c : ', content)

    r_content = su.reverse_string(content)

    result = {
        'content' : r_content
    }

    return make_response(jsonify(result), 200)

if __name__ == '__main__':
    app.run( host = '0.0.0.0', port = 8071, debug = True)
