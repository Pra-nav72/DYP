from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / select database
db = client["prnvDB"]

# Create / select collection
emp_col = db["EMP"]

# i) Insert 5 documents
employees = [
    {"Emp-name": "Riddhi", "Emp-mobile": "9876543210", "Emp-sal": 8000, "Age": 25},
    {"Emp-name": "Amit", "Emp-mobile": "9123456789", "Emp-sal": 12000, "Age": 30},
    {"Emp-name": "Sneha", "Emp-mobile": "9988776655", "Emp-sal": 6000, "Age": 22},
    {"Emp-name": "Rahul", "Emp-mobile": "9090909090", "Emp-sal": 5000, "Age": 28},
    {"Emp-name": "Neha", "Emp-mobile": "8888888888", "Emp-sal": 9500, "Age": 26}
]

emp_col.insert_many(employees)
print("5 employee records inserted")

# iii) Find employees with salary between 5000 and 10000
print("\nEmployees with salary between 5000 and 10000:")
for emp in emp_col.find({"Emp-sal": {"$gte": 5000, "$lte": 10000}}):
    print(emp)

# iv) Update mobile number of employee named Riddhi
emp_col.update_one(
    {"Emp-name": "Riddhi"},
    {"$set": {"Emp-mobile": "9999999999"}}
)
print("\nMobile number updated for Riddhi")

# v) Display employees ordered by Age
print("\nEmployees ordered by Age:")
for emp in emp_col.find().sort("Age", 1):
    print(emp)
