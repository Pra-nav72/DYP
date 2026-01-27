from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["MYEMP"]
coll = db["EMP"]

details = [
    {
        "Emp-name":"Pranav",
        "Emp-mobile":"783449237",
        "Emp-sal": 10000,
        "Emp-age": 23
    },

    {
        "Emp-name":"Riddhi",
        "Emp-mobile":"98736434",
        "Emp-sal": 6000,
        "Emp-age": 25
    },

    {
        "Emp-name":"Rohit",
        "Emp-mobile":"86776732",
        "Emp-sal": 5000,
        "Emp-age": 22
    },

    {
        "Emp-name":"sidhhant",
        "Emp-mobile":"96867423",
        "Emp-sal": 12000,
        "Emp-age": 24
    },

    {
        "Emp-name":"Nikhil",
        "Emp-mobile":"60484834",
        "Emp-sal": 8000,
        "Emp-age": 21
    },
]

coll.insert_many(details)

print("\n\n--------------------------------------------salary 5k-10k----------------------------------------")
for i in coll.find({"Emp-sal" : {"$gte": 5000, "$lte": 10000}}):
    print(i)

coll.update_many({"Emp-name":"Riddhi"}, {"$set":{"Emp-mobile": "9999999999"}})

print("\n\n--------------------------------------show according to age----------------------------------------")
for i in coll.find().sort("Emp-age", 1):
    print(i)