# taking an input and showing its factorial through CLA

import sys

n = len(sys.argv)

if n != 2:
    print("Invalid number of argument!")


elif sys.argv[1].isdigit():
    f = int(sys.argv[1])

    fact = 1
    for i in range(1, f + 1):
        fact = fact * i

    print("factorial of ", f, " is ", fact)

else:
    print("Argument is string!")
