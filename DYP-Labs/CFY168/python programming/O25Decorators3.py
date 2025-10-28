def fun1(fun):
    def inner(a):
        x = fun(a)
        print(f"printing X {x}")
        return x*x
    return inner

def fun2(fun):
    def inner(a):
        y = fun(a)
        print(f"printing Y: {y}")   
        return y+y
    return inner


@fun2
@fun1
def funX(a):
    return a

print(funX(10))