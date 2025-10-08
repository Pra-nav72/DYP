#perform operation on the following tuple given
t = (10, 20, 30, 40, 50)

input_num= int(input("Enter a number: "))
if input_num in t:
    print(f"Number {input_num} is in tuple")
else:
    print(f"Number {input_num} is not in tuple")

t_to_list = list(t)
print(f"converted tuple to list: {t_to_list}")

t_to_list[len(t)-1] = 100
print(f"replaced last value to {t_to_list}")


t = tuple(t_to_list)
inp = int(input("Enter a number to find it's index: "))
print(type(t))
for i in t:
    if i == inp:
        print(f"Number {inp} is at index {t.index(i)}")
        break
else:
    print(f"Number {inp} is not in tuple")