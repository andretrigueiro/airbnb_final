from flask import Flask, jsonify, request
from flask_cors import CORS
# from api.views import add_views

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

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(__name__)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # adding views
    # add_views(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    def check_user(user_email):
        for user in USERS:
            if user['email'] == user_email:
                return True
        return False

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
            email = post_data.get('email')
            if check_user(email):
                response_object['message'] = 'Email already in use! Try other'
            else:
                USERS.append({
                    'user': post_data.get('user'),
                    'password': post_data.get('password'),
                    'email': email,
                    'type': post_data.get('type')
                })
                response_object['message'] = 'User added!'
        else:
            response_object['users'] = USERS
        return jsonify(response_object)

    from api.db.config_db import init_app
    init_app(app)

    return app