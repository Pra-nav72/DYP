# A dictionary is a collectionn of {key : value} pairs
#       ordered & changeable, NO Duplicates allowed

stateCapital = {"Bihar" : "Patna", "Goa":"Panji", "Maharashtra":"Mumbai"}

# print(dir(stateCapital))
# print(help(stateCapital))

print(f"capital of Goa: {stateCapital.get('Goa')}")
print(f"Uttar Pradesh-->Not in dict.: {stateCapital.get('Uttar Pradesh')}") #Return -->None

#for adding or MODIFYING TOO
stateCapital.update({"Uttarakhand":"Dehradun"})
stateCapital.update({"Goa":"Rajgir"})
print(f"after updating-->add & modify : {stateCapital}")

#remove item
# stateCapital.pop("Uttarakhand")

#remove last add item
# stateCapital.popitem()
# print(stateCapital)

#to remove all elements ----> stateCapital.clear()

# Returns all the keys of dictionary
keys = stateCapital.keys()
print(f"all the keys: {keys}")

# Returns all values
values = stateCapital.values()
print(f"all the values: {values}")

items = stateCapital.items()
print(f"\nall [(\'key\', \'value\')] pairs--> {items}\n")
#to understand easily print this:
for key, value in stateCapital.items():
    print(f"{key}:{value}")