
keys = ['name', 'age', 'city', 'is_student']
person = {}

# get values for each key
for key in keys:
    value = input(f"Enter value for '{key}': ")
    person[key] = value

# Display the final dictionary
print("Final Dictionary: ")
print(person)
