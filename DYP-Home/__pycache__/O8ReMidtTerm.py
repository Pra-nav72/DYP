# Creating the decorator
def notify(func):
    def wrapper():
        print("Function is being executed")
        return func()
    return wrapper

# Applying the decorator
@notify
def greet():
    return "Hello World"

# Calling the function
print(greet())

def my_range(start, end, step):
    for i in range(start, end, step):
        yield i
        print(i)
