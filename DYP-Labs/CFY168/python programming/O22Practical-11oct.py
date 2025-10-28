d = {}
flag=True
    
while flag:
    d.update({input("Enter key: "): input("Enter value: ")})
    c = input("do you want to continue? (y/n): ").lower()
    if c=='n':
        flag=False
        break
    elif c != 'n'  or c!='y':
        print("Invalid input!")
print(d)