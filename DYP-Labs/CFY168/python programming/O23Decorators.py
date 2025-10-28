# Decorators let you add extra behavior to a function,
# without changing the function's code.

# A decorator is a funciton that takes another function as input and returns a new funtion..

# This is decorator function
def changeletter(func):
    def innerfunc():
        return func().upper()
    return innerfunc


# funcX is function that gets decorated by using '@changeletter'
@changeletter
def funcX():
    return "hello world!"


print(funcX())

