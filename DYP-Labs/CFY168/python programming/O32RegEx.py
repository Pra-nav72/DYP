#regular expression
import re
str1 = input("Enter a string: ")


p = re.compile("ram")
x = p.finditer(str1)

for i in x:
    print(f"{i.start()} ---> {i.end()} ---> {i.group()}")


print("----------------------------------------------")

# Second method to do the same Regular expression
R = re.finditer("ram", str1)

for r1 in R:
    print(f"{r1.start()} ---> {r1.end()} ---> {r1.group()}")