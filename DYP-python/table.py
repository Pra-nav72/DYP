# print a table as well as.....
# print a series of table through CLA

import sys

n = len(sys.argv)

# to print table of a particular number
if n == 2:

    if sys.argv[1].isdigit():
        a = int(sys.argv[1])

        print("Table of", a)
        for i in range(1, 11):
            print(a, 'X', i, '=', a * i)

    else:
        print("Argument is not a number!")

# To print a series of table
if n == 3:

    if sys.argv[1].isdigit() and ((sys.argv[2]).isdigit()):
        # Typecasting to integer
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        if a > b:
            print("first number should must be smaller!")
        else:
            print("Table of ", a, "to", b, ":")
            for i in range(a, b + 1):
                print("\n--------------\nTable of", i, "\n--------------\n")
                for j in range(1, 11):
                    print(i, 'X', j, '=', i * j)

    else:
        print("Argument is not number!")


# if expected no. of inputs are not given
elif n < 2 or n > 3:
    print("Invalid number of arguments!")
