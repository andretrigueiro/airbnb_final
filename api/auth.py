import functools

from flask import (
    Blueprint, flash, g, jsonify, request, session
)
from werkzeug.security import check_password_hash, generate_password_hash

from api.db.config_db import get_db

from api.db.mongodb.users_db import find_all, find_by_email, find_one, set_host, insert_one

bp = Blueprint('auth', __name__, url_prefix='/auth')

def check_user(user_email):
    if find_by_email(user_email):
            return True
    return False

@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')

        if check_user(email):
            response_object['message'] = 'Email already in use! Try other'
        else:
            username = post_data.get('user')
            password = post_data.get('password')
            type = post_data.get('type')

            user_to_add = {
                'user': username,
                'password': generate_password_hash(password),
                'email': email,
                'type': type
            }
            insert_one(user_to_add)
            response_object['message'] = 'User added!'
    else:
        response_object['users'] = find_all()
    return jsonify(response_object)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        email = post_data.get('email')
        password = post_data.get('password')
        error = None

        user = find_by_email({"email": email})

        if user is None:
            response_object['message'] = 'Couldnt find email.'
            error = 'Couldnt find email.'
        if not check_password_hash(user['password'], password):
            response_object['message'] = 'Incorrect password.'
            error = 'Incorrect password.'

        if error is None:
            session.clear()

            print("1 - login email: ", user['email'])

            session['user_email'] = user['email']

            print("2 - session email: ", session['user_email'])

            response_object['message'] = 'User logged in!'

    return jsonify(response_object)

@bp.before_app_request
def load_logged_in_user():
    user_email = session.get('user_email')

    print("load_logged")
    print("3 - session logged email: ", user_email)

    if user_email is None:
        g.user = None
    else:
        g.user = find_by_email(user_email)

@bp.route('/logout')
def logout():
    session.clear()
    response_object = {'status': 'success'}
    response_object['message'] = 'User logged out!'

    return jsonify(response_object)

def login_required(view):
    response_object = {'status': 'success'}
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            response_object['message'] = 'No user logged in!'
            return jsonify(response_object)

        return view(**kwargs)

    return wrapped_view