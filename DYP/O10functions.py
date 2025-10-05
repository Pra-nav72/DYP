import time
#---------------1. Positional arguments------------------------



def add(x, y):
    z = x+y
    return z
print(f"calling add(40+39): {add(40, 39)}")



#------------------------2. Default arguments---------------------

def multiply(x=1, y=2):
    z = x*y
    return z

print(f"\ncalling multiply no argument: {multiply()}")
print(f"calling multiply with 1 arg(x): {multiply(2)}")
print(f"calling multiply with all arg: {multiply(3, 5)}")


# if any one or two of the many arguments is default then write it later
#       i.e non-default argument should be written first.
# def count(end, start=0):
#     for i in range(start, end+1):
#         print(i)
#         time.sleep(0.5)
#     print("Done!") 
# count(10)
# print()
# count(30, 15)


#-----------------------3. keyword Argument-----------------------------

# An argument preceded by an identifier helps in readibility
# order of arguments does'nt matter in this.

def hello(greetings, title, first, last):
    print(f"{greetings.title()} {title}{first.title()} {last.title()}")

hello("hellow!", last="kumar", title="mr.", first="praNaV")
 #positional arguments must be ahead of keyword argument.



 #--------------------4. Arbitrary Arguments---------------------------------

 #  *args  --->allow to pass multiple elements(in tuple)
 #  **kwargs --->allow to pass multiple keyword arguments(in dictionary)
 #              * --> unpacking operator


def add(*args): #args is just a variable name
    total=0
    print(f"args: {args} of type: {type(args)}")
    for argument in args:
        total += argument
    return total

x = add(1, 3, 45, 53, 6)
print(f"adding the every args: {x}")



def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10} : {value}")

address(street="B-16", area="Navshantiniketan", city="Akurdi", district="Pune", zip="412101")