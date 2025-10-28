#Q1. take input in upper case and return in lower case using decorators

def changecase(func):
    def inner():
        return func().lower()
    return inner

@changecase
def user():
    return input("Enter some words in UpperCase: ").upper()

print(user())


#Q2. 

def func1(func):
    def inner1():
        print("Welcome in decorators!")
        return func()
    return inner1

def func2(func):
    def inner2():
        print("bye bye decorator!")
        return func()
    return inner2


@func1
@func2
def funcDecorator():
   return

funcDecorator()