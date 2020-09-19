from pymongo import MongoClient
from pymongo.cursor import CursorType

host = "localhost"
port = "27017"
mongo = MongoClient(host, int(port))
#print(mongo)

def insert_item_one(mongo, data, db_name = None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result

insert_item_one(mongo, {"text":"hello python"}, "test", "test")
