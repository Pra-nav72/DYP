# vowels in th word "Learning Python"
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Learning python"

new_vowels = [i for i in word if i in vowels]
print(new_vowels)

#extend program by adding a list l2 after 'g'
list1 = ['a', 'b', ['c',['d', 'e',['f', 'g'], 'k'], 'l'], 'm', 'n']
l2 = ['h', 'i', 'j']

print("-----------------------------------\n")

#------using loop--------------------------
# for i in list1[2][1][2]:
#     if i=='g':
#         list1[2][1][2].insert(2, l2)
#     print(i)


#-----------using comprehension-------------------------
[list1[2][1][2].insert(2, l2) for i in list1[2][1][2] if i=='g']
print(list1)