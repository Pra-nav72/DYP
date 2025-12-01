def changecase(func):
    def inner():
        return func().lower()
    return inner

@changecase
def user():
    return input("Enter some words in UpperCase: ").upper()

print(user())
