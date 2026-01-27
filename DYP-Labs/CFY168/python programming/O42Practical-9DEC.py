from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["MYEMP"]
collection = db["Student_info"]


students = [
    {"Roll_No": 1, "Name": "Amit", "Course": "BCA", "Total_Marks": 450, "Percentage": 90},
    {"Roll_No": 2, "Name": "Rahul", "Course": "MCA", "Total_Marks": 380, "Percentage": 76},
    {"Roll_No": 3, "Name": "Neha", "Course": "BCA", "Total_Marks": 320, "Percentage": 64},
    {"Roll_No": 4, "Name": "Rahul", "Course": "MCA", "Total_Marks": 410, "Percentage": 82},
    {"Roll_No": 5, "Name": "Pranav", "Course": "MCA", "Total_Marks": 390, "Percentage": 78},
]

collection.insert_many(students)
print("Inserted 5 student documents.\n")



print("-----------------------------------------Students with percentage between 70 and 80:-------------------------------------")
for s in collection.find({"Percentage": {"$gte": 70, "$lte": 80}}):
    print(s)
print()



collection.update_many({"Name": "Rahul"},{"$set": {"Roll_No": 999}})
print("Updated Roll_No for students named Rahul.\n")


print("---------------------------------------------Top 5 students by percentage:-----------------------------------------------")
for s in collection.find().sort("Percentage", -1).limit(5):
    print(s)
print()



highest = collection.find_one(sort=[("Percentage", -1)])["Percentage"]

print("-----------------------Student(s) having highest percentage:-------------------------------------------------------")
for s in collection.find({"Percentage": highest}):
    print(s)
print()



print("---------------------------------------------All students from course MCA:-----------------------------------------------")
for s in collection.find({"Course": "MCA"}):
    print(s)
print()



print("-----------------------------------------------Students sorted by percentage (descending):------------------------------")
for s in collection.find().sort("Percentage", -1):
    print(s)
