# swap every odd-even index character in the string
string_input = input("Enter a string: ")

for i in range(1, len(string_input)):
    new_string=" "  
    if i % 2 == 0:
        new_string += string_input[i-1]
    elif i % 2 ==1:
        new_string += string_input[i]
print(new_string)
