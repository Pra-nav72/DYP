from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / select database
db = client["prnvDB"]

# Create / select collection
employee_col = db["employee"]

# Sample employee documents
employees = [
    {
        "ID": 123,
        "name": "Rahul Sharma",
        "address": "Delhi",
        "phone": "9876543210",
        "email": "rahul@gmail.com",
        "dept": "Accounts"
    },
    {
        "ID": 210345,
        "name": "Anita Verma",
        "address": "Mumbai",
        "phone": "9123456789",
        "email": "anita@gmail.com",
        "dept": "HR"
    },
    {
        "ID": 456,
        "name": "Karan Singh",
        "address": "Pune",
        "phone": "9988776655",
        "email": "karan@gmail.com",
        "dept": "Accounts"
    }
]

# Insert documents
employee_col.insert_many(employees)

# a) Display all employees in Accounts department
print("Employees in Accounts Department:")
for emp in employee_col.find({"dept": "Accounts"}):
    print(emp)

# b) Delete employee with ID 210345
employee_col.delete_one({"ID": 210345})
print("\nEmployee with ID 210345 deleted")

# c) Update phone for employee ID 123
employee_col.update_one(
    {"ID": 123},
    {"$set": {"phone": "9999999999"}}
)
print("Phone number updated for employee ID 123")
