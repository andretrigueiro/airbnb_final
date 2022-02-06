from flask import Flask, jsonify, request
from flask_cors import CORS

from api.db.config_db import get_db
# from api.views import add_views

# configuration
DEBUG = True

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(__name__)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
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



    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    # users route
    @app.route('/users', methods=['GET'])
    def all_users():
        db = get_db()
        users = db.users
        response_object = {'status': 'success'}
        response_object['users'] = users
        return jsonify(response_object)

    from api.db.config_db import init_app
    init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app