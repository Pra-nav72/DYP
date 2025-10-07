userString = input("Enter a Sentence:   ")
print(f"find my at: {userString.find("my")}")
# print(f"index my at: {userString.index("my")}")  #it will show error if not found
print(f"strip function: {userString.strip()}")
print(f"Lstrip: {userString.lstrip()}")
print(f"Rstrip: {userString.rstrip()}")  
print(f"count: {userString.count("a")}")  #counts number of occurance.
print(f"split: {userString.split()}")

#Seperator
# print(f"Seperator(,).join: {",".join(userString)}")

#character
print(f"if alpha-numeric: {userString.isalnum()}")  #There must be no space3(_) in beetween to be True.
print(f"if aplphabet: {userString.isalpha()}")  #english alphabets only.

#---------Difference b/w the bellow----------------
print(f"if decimal: {userString.isdecimal()}")
print(f"if digit: {userString.isdigit()}")
print(f"if numeric: {userString.isnumeric()}")
print(f"if title: {userString.istitle()}") #Only first letter of every words should be capital and else every letter shoulbe be small.




#changing case
print(f"to upper: {userString.upper()}") #all capital 
print(f"to capitalize: {userString.capitalize()}")  #first letter of sentence shoulbe capital
print(f"to small: {userString.casefold()}")
print(f"to title: {userString.title()}")
