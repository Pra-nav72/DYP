# Write a Python program to group words by their first letter in dictionary format.
# Input: l = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']
# Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

l = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']

d = {}
for i in l:
    fLetter = i[0].lower()
    d.setdefault(fLetter, []).append(i)
print(d)