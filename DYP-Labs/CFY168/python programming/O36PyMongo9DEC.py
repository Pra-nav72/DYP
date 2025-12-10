from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["prnv_db"]
collection = db["student_practical"]
collection2 = db["Library"]

while True:
    print("1. Enter Student details \n " \
    "2. Enter library books")
    inp = int(input("What you want to do?: "))

    if inp==1:
        details = [
            {'name' : input("Enter name: "),
            'course': input("Enter course: "),
            'Mobile': input("Enter Mobile: "),
            'address': {'area': input("Enter address area: "),
                        'city': input("Enter address city: "),
                        'country': input("Enter address country: "),
                        'pin': input("Enter PIN: ")}},
        ]
        collection.insert_many(details)
        print("\n\n")
        
        flag = input("do you want to add more?(y/n): ").lower()
        if flag=='n':
            break
    
    elif inp==2:
        books = [
            {
                'bookTitle': input("Enter book Title: "),
                'bookAuthor': input("Enter book author name: "),
                'bookPage': int(input("Enter total no. of pages: ")),
                'bookPrice': int(input("Enter price: "))
            },
        ]
        collection2.insert_many(books)
        print("\n\n")
        flag = input("do you want to add more?(y/n): ").lower()
        if flag=='n':
            break


for i in collection.find():
    print(i)

print("------------------------------------------------------------------------------------------------")

for i in collection2.find():
    print(i)