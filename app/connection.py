# import json
# from pymongo import MongoClient
# from os import getenv
#
# #
# # mongo_uri = getenv("MONGO_URI", "mongodb://mongodb-gerstnir-dev.apps.rm2.thpm.p1.openshiftapps.com:27017/")
# # mongo_db = getenv("MONGO_DB", "testdb")
# # mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
# # file_path = './employee_data_advanced.json'
# #
# # # Making Connection
# # myclient = MongoClient(mongo_uri)
# #
# # # database
# # db = myclient[mongo_db]
# #
# # # Created or Switched to collection
# # # names: GeeksForGeeks
# # Collection = db[mongo_collection]
#
# client = MongoClient("mongodb+srv://refael1:refael1370@cluster0.dzumeea.mongodb.net/")
# db = client["ecomerce_db"]
# collection = db["employee_data_advanced"]
#
# def conn_employee():
#     with open("employee_data_advanced.json", "r", encoding="utf-8") as f:
#         users = json.load(f)
#
#     result = collection.insert_many(users)
#     print(result)
#     return result

import json
from pymongo import MongoClient
from os import getenv

mongo_uri = getenv("MONGO_URI", "fastapi")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './employee.json'

def get_connection():
    myclient = MongoClient(mongo_uri)
    db = myclient["contacts_data"]
    Collection = db["employee_data_advanced"]
    return Collection
collection = get_connection()