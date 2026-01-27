password = input("Enter password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False

special_chars = "$#@*"

# Checking each character
for ch in password:
    if ch.islower():
        has_lower = True
    elif ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

# Checking all conditions
if (8 <= len(password) <= 20 and
    has_lower and
    has_upper and
    has_digit and
    has_special):
    print("Password is Valid")
else:
    print("Password is Invalid")
