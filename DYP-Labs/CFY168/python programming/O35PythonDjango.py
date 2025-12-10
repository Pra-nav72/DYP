from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["prnv_db"]
collection = db["EMP"]

for i in collection.find({'age': {"$lt" : 200}}):
    print(i)