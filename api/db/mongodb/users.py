from api.db.mongodb import DATABASE

def find_all():
    result = list(DATABASE.users.find({}, {'_id': False}))
    return result

def find_by_email(email):
    result = list(DATABASE.users.find({'email': email}, {'_id': False}))
    return result

def find_one(user_id):
    result = DATABASE.users.find_one({'id': user_id})
    return result

def set_host(user_id):
    DATABASE.user.update_one({'id': user_id}, {'$set': {'type': 'host'}})