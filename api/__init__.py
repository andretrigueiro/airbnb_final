from flask import Flask, jsonify, session
from flask_cors import CORS
import boto3

from api.db.config_db import init_app

# configuration

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(__name__)
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY='dev',
        UPLOAD_FOLDER = "uploads",
        BUCKET = "airbnb-clone-project",
    )

    # enable CORS
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})

    s3 = boto3.resource('s3')

    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    # Register DB commands
    init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    CORS(auth.bp)

    from . import users
    app.register_blueprint(users.bp)
    CORS(users.bp)

    from . import files
    app.register_blueprint(files.bp)
    CORS(files.bp)

    return app