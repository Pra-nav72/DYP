import random

l=[]
for i in range(11):
    l.append(int(random.random() * 100))
print(f"before sort: {l}")
l.sort()
print(f"after sort:  {l}\n")
print(l[-2])