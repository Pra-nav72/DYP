# import array as arr

#Q1

arr = []
for i in range(7):
    inp = float(input("Enter temperature: "))
    arr.append(inp)

print(arr)
add_temp = 0
i=0
for temp in arr:
    add_temp += temp
avg_temp = add_temp/len(arr)
print(f"average temperature: {avg_temp:.2f}")
print(f"hottest days: {max(arr)}")
print(f"coldest days: {min(arr)}")

for temp in arr:
    i+=1
    if temp>=avg_temp:
        print(f"day: {i}")



# Q2

