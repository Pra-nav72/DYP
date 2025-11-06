from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(1, 21):
    if is_prime(i):
        print(f"{i} is prime")
    