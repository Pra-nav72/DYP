import random

lst = []
for i in range(11):
    lst.append(int(random.random() * 100))
print(f"original list: {lst}")

lst2 = []
for i in lst:
    if i%2==0:
        lst2.append(i)
print(f"only even: {lst2}")
#Converted them in set to use the difference property of set. Then again typeCasted to list
lst = list(set(lst).difference(set(lst2)))
print(f"only odd: {lst}")