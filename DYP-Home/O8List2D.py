food = ["pizza", "samosa", "salad", "hamburger"]
drinks = ["cola", "sprite", "limica", "sting"]
fruits = ["mango", "apple", "litchi", "kiwi"]

# this will act like 2D List
groceries = [food, drinks, fruits]

#index > available ----> Error: Index out of range
print(f"all the list in groceries: {groceries}")
print(f"\nat index 0, list=food: {groceries[0]}")
print(f"access 2nd food: {groceries[0][1]}")
print(f"access 3rd fruits: {groceries[2][2]}\n")

#to iterate all elements of list
for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()