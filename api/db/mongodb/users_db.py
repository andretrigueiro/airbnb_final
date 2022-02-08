from api.db.mongodb import DATABASE

def convert_all_id_to_string(convert_list):
    for user in range(len(convert_list)):
        convert_list[user]['_id'] = str(convert_list[user]['_id'])
    return convert_list

def convert_one_id_to_string(convert_list):
    convert_list['_id'] = str(convert_list['_id'])
    return convert_list

def find_all():
    result = list(DATABASE.users.find())
    result = convert_all_id_to_string(result)
    return result

def find_by_email(email):
    result = DATABASE.users.find_one(email)
    result = convert_one_id_to_string(result)
    return result

def find_one(user_id):
    result = DATABASE.users.find_one({'_id': user_id})
    return result

def set_host(user_id):
    DATABASE.user.update_one({'_id': user_id}, {'$set': {'type': 'host'}})

def insert_one(user):
    DATABASE.users.insert_one(user)