import re

# # mobile no. should start from 6-9 & total 10 digits
# p = r"^[6-9][0-9]{9}$"
# u = input("Enter a mobile no.(start with [6-9]): ")

# x = re.search(p, u)

# if x != None:
#     print("Valid Mobile number!")
# else:
#     print("Not a valid number!") 


# # check PANCARD FORMAT

# pancard = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
# pc = input("Enter your PANCARD: ")

# ps = re.search(pancard, pc)
# if ps != None:
#     print("Valid PANCARD number!")
# else:
#     print("Not a valid PANCARD!") 


# Indian Phone Number(+91/91/91 /0/ )
phone = r"^(?:\+91|91|0)?\s?[6-9]+\d{9}$"
user = input("Enter your Mobile NO.: ")

m = re.fullmatch(phone, user)

if m != None:
    print("Valid Phone number!")
else:
    print("Not a valid Phone number!") 