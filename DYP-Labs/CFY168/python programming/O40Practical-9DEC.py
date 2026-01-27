from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['MYEMP']
collection = db['employee']

details = [
    {
        'ID': 123,
        'name':"pranav", 
        'address':"Pune",
        'phone': 93847589,
        'email': 'kkkppp@gmail.com',
        'dept': 'IT'
     },
     {
        'ID': 210345,
        'name':"Srikant", 
        'address':"Noida",
        'phone': 888375083,
        'email': 'sri1901@gmail.com',
        'dept': 'Accounts'
     },
     {
        'ID': 2345,
        'name':"Karanjeet", 
        'address':"Rajgir",
        'phone': 974435083,
        'email': 'karanjeet@gmail.com',
        'dept': 'Accounts'
     },
     {
        'ID': 2105,
        'name':"Yash", 
        'address':"Nawada",
        'phone': 387832342,
        'email': 'Merayashuyashu@gmail.com',
        'dept': 'HR'
     },
     {
        'ID': 9345,
        'name':"Shanu", 
        'address':"Delhi",
        'phone': 8888996523,
        'email': 'Shanuuuu@gmail.com',
        'dept': 'Accounts'
     }
]

# collection.insert_many(details)

print("-------------------------------Accounts-----------------------------------------------")
for i in collection.find({"dept":"Accounts"}):
   print(i)

collection.delete_many({'ID':210345})
print("\n\n----------------------------after deletion-------------------------------------------")
for i in collection.find():
   print(i)


collection.update_many({'ID': 123}, {"$set":{'phone': 99999999}})
print("\n\n----------------------------after updating phone-------------------------------------------")
for i in collection.find():
   print(i)