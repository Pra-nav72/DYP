
n = int(input("Enter number of elements: "))

elements_set = set()

for i in range(n):
    elem = input(f"Enter element {i+1}: ")
    if len(elem) > 0:
        elements_set.add(elem[0])

# Display the set
print("Set elements:", elements_set)

# length of set
print("Length of set:", len(elements_set))

# Initialize counters
digits = lowercase = uppercase = 0

# Count digits, lowercase, and uppercase letters
for ch in elements_set:
    if ch.isdigit():
        digits += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isupper():
        uppercase += 1

# Display counts
print("\nNumber of digits:", digits)
print("Number of lowercase letters:", lowercase)
print("Number of uppercase letters:", uppercase)
