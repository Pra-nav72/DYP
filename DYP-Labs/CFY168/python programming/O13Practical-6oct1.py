inp = input("Enter a string: ")

for char in inp:
    print(char, end=' ')
print()
for char in reversed(inp):
    print(char, end=" ")

print()


#Q7. break loop if user integer -ve value
is_running = True
while is_running:
    inp = int(input("Enter an integer: "))
    if inp >= 0:
        print(f"you have entered {inp}.")
    else:
        print(f"you have entered negative value {inp}")
        is_running=False
