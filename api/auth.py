import functools

from flask import (
    Blueprint, flash, g, redirect, jsonify, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from api.db.config_db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

def check_user(user_email):
    db = get_db()
    users = db.users
    for user in users:
        if user['email'] == user_email:
            return True
    return False

@bp.route('/register', methods=('GET', 'POST'))
def register():
    db = get_db()
    users = db.users
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
            users.insert_one(user_to_add)
            response_object['message'] = 'User added!'
    else:
        response_object['users'] = users
    return jsonify(response_object)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    db = get_db()
    users = db.users
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        email = post_data.get('email')
        password = request.form['password']
        error = None

        user = users.find_one({"email": email})

        if user is None:
            response_object['message'] = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            response_object['message'] = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['_id']
            response_object['message'] = 'User logged in!'

        flash(error)

    return jsonify(response_object)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = get_db()
        users = db.users
        g.user = users.find_one({"user_id": user_id})

@bp.route('/logout')
def logout():
    session.clear()
    response_object = {'status': 'success'}
    response_object['message'] = 'User logged out!'

    return jsonify(response_object)
