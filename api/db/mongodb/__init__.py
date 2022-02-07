import pymongo
import os
CONNECTION_STRING = os.environ.get('AIRBNB_FINAL_DB_CONNECTION')
DATABASE = pymongo.MongoClient(CONNECTION_STRING).airbnb_final