from api.db.mongodb.users_db import find_all, find_by_email, find_one, set_host

from flask import (
    Blueprint, flash, g, redirect, jsonify, request, session, url_for
)

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/all_users', methods=["GET"])
def all_users():
    users = find_all()
    response_object = {'status': 'success'}
    response_object['users'] = users
    return jsonify(response_object)