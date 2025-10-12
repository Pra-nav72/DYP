lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2=["Pune", "Mumbai", "Goa", "Delhi", "Tokyo", "Hawaii", "Athens", "Korea", "Paris", "Greece"]

dict={}
for i in range(len(lst1)):
    dict.update({lst1[i]:lst2[i]})

for key, value in dict.items():
    print(f"{key} ---> {value}")