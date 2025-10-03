# addition of given numbers through command line argument..........

import sys

n = len(sys.argv)
print("total number of argument passed: ", n)

print("first argument is: ", sys.argv[0])
print("argument passed for evaluation: ", end=" ")

for i in range(1, n):
    print(sys.argv[i], end=" ")

add = 0

for i in range(1, n):
    add += int(sys.argv[i])

print("\n\nresult: ", add)
