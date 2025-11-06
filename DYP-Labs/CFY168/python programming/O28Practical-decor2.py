def my_decorator(func):
    def wrapper():
        msg = func() 
        print(msg, "<-- This is decorated now")
    return wrapper

@my_decorator
def originalfunc():
    return "I am a function kindly decorate my content"

originalfunc()
