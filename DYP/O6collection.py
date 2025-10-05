# #Collections--> single variable used to store multiple values.
# #   List=[] --> ordered & changeable, duplicates allowed
# #   set={} ---> unordered & Immutabel, add/remove allowed, duplicates not allowed
# #   Tuple=()--> ordered & unchangeable, duplicates allowed, faster

# #-----------------------LIST[]---------------------------------------------------

# fruits = ["banana", "guava", "melon", "kiwi"]
# print(fruits) 

# fruits.append("kiwi")
# fruits[0] = "coconut"
# print(f"appending kiwi & changing index 0: {fruits}") 

# fruits.insert(0, "lemon")
# print(f"after insert at 0: {fruits}")

# for fruit in fruits:
#     print(fruit)


# print(len(fruits))

# print(f"is apple in fruits: {('apple' in fruits)}")#can't use "" in {''}formatted type

# fruits.sort()
# fruits.reverse()
# print(f"after sorting & reversing: {fruits}")
# print(f"1st occurance of kiwi at index: {fruits.index('kiwi')}")

# print(f"count no. of occurance of kiwi: {fruits.count('kiwi')}")
# # fruits.clear()  #empty the list

# # print(dir(fruits)) #fruits(list) related attributes & functions
# # print(help(fruits)) # description of the above attributes & functions


# #---------------------Set{}-------------------------------------------------------------
#output changes in each run

menu = {"Pizza", "Pasta", "Maggie", "Omelate"}

# print(dir(menu)) #menu(set) related attributes & funcitons
# print(help(menu)) # description of the attributes & functions of set

print(f"length: {len(menu)}")

#instead of boolean--> returns 1st correct value[CONFUSION]
print(f"pizza is in menu?? {'pizza' and 'Pizza' and 'Maggie' in menu}")
print(f"pizza is in menu?? {'Pizza' and 'pizza' in menu}") # returns false

#Wrong word will give 'keyError'
menu.add('cola')
menu.remove('Omelate')
print(f"after adding the cola & removing omelate: {menu}")


#------------Tuple()------------------
