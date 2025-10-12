#Write a Python program to remove duplicates from a list using set and keep order.
lst = ["Mohan", "guava", "Mohan", "grapes", "grapes", "orange"]
lst1 = []

s = set(lst)
for i in lst:
    if i in s:
        lst1.append(i)
        s.discard(i)        
# s.remove(i) --> give error if <i> is not in <s>[discard won't give error]
        
print(lst1)