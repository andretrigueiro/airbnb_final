import functools

from flask import (
    Blueprint, g, jsonify, request, session
)
from werkzeug.security import check_password_hash, generate_password_hash

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
            response_object['user_email'] = ''
            error = 'Couldnt find email.'
        if not check_password_hash(user['password'], password):
            response_object['message'] = 'Incorrect password.'
            response_object['user_email'] = ''
            error = 'Incorrect password.'

        if error is None:
            print("- What is in session before clear?")
            print(session)
            session.clear()

            session['user_email'] = user['email']
            session.modified = True
            session.permanent = True

            print("- Session new email: ", session['user_email'])

            print("- What is in the final session login?")
            print(session)

            response_object['user_email'] = user['email']
            response_object['message'] = 'User logged in!'
            check_session()

    return jsonify(response_object)

def check_session():
    print("- Check function session")
    print(session)

@bp.before_app_request
def load_logged_in_user():
    print("- Initial before_app_request SESSION: ")
    print(session)
    user_email = session.get('user_email')

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