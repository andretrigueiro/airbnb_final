from unittest.mock import patch
from flask import Flask, jsonify
from flask.globals import request
from api.db.userdata import USERS

def add_views(app: Flask):
    app.add_url_rule('api/users', view_func=get_users)
    app.add_url_rule('api/users/<user_id>', view_func=get_users, methods=['GET', 'POST'])


def get_users():
    response_object = {'status': 'success'}
    response_object['users'] = USERS
    response = jsonify(response_object)
    return response

def get_user(user_id):
    response_object = {'status': 'success'}
    if user_id is None:
        return {'status': 'failed'}
    user = search_on_list(USERS, 'email', user_id)
    if request.method == 'POST':
        patch_data = request.json
    response_object['user'] = user
    response = jsonify(response_object)
    return response

def search_on_list(list_of_dicts, key, value):
    return next(item for item in list_of_dicts if item.get(key) == value)