#!venv/bin/python3
from flask import Flask, jsonify, make_response, request, abort
from flask_httpauth import HTTPBasicAuth
from utils.utils import *


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users:
        if users[username] == password:
            return username


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/api/register', methods=['POST'])
def register():
    # If json is empty
    if not request.json:
        return make_response(jsonify({'error': 'Json is empty'}), 400)
    # Checking fields for emptiness 
    elif not check_register_json(request.json):
        return make_response(jsonify({'error': 'Some fields is empty'}), 400)
    
    register_user(request.json)
    return make_response(jsonify(request.json), 200)



if __name__ == '__main__':
    app.run(debug=True)

