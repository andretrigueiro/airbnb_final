from api.db.mongodb import DATABASE

def convert_id_to_string(convert_list):
    for user in range(len(convert_list)):
        #print("antes: ", type(convert_list[user]['_id']))
        convert_list[user]['_id'] = str(convert_list[user]['_id'])
        #print("depois: ", type(convert_list[user]['_id']))
    return convert_list

def find_all():
    result = list(DATABASE.users.find())
    result = convert_id_to_string(result)
    return result

def find_by_email(email):
    result = list(DATABASE.users.find({'email': email}))
    return result

def find_one(user_id):
    result = DATABASE.users.find_one({'_id': user_id})
    return result

def set_host(user_id):
    DATABASE.user.update_one({'_id': user_id}, {'$set': {'type': 'host'}})