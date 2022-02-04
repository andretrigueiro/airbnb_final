import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

USERS = [
    {
        'user': 'ronaldinho',
        'password': '123',
        'email': 'ronaldinho@gmail.com',
        'type': 'host'
    },
    {
        'user': 'ronaldo',
        'password': '1234',
        'email': 'ronaldo@gmail.com',
        'type': 'guest'
    },
    {
        'user': 'rivaldo',
        'password': '12345',
        'email': 'rivaldo@gmail.com',
        'type': 'guest'
    },
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# users route
@app.route('/users', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        USERS.append({
            'user': post_data.get('user'),
            'password': post_data.get('password'),
            'email': post_data.get('email'),
            'type': post_data.get('type')
        })
        response_object['message'] = 'User added!'
    else:
        response_object['users'] = USERS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
