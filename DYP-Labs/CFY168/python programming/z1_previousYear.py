def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def generate_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

# Example usage
n = int(input("Enter number of terms: "))
generate_fibonacci(n)
