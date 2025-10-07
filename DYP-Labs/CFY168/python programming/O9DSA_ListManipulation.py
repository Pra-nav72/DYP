list = [1, 4, 65, 8786, "hello"]
#add 2 at last position

# print(help(list.append(list)))
# print(help(list))

#count
def count(list):
    counts = 0
    for i in list:
        if i in list:
            counts +=1
    return counts

print(f"total element is list is: {count(list)}")

#pop
def pop(list):
    
    del list[len(list)-1]
    return list

print(pop(list))

#pop(index, list)
def pop(index, list):
    del list[index]
    return list
print(pop(0, list))