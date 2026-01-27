import threading
import time
import math

# Function to calculate square
def print_square(num):
    print("Square of", num, "is:", num * num)
    time.sleep(1)

# Function to calculate factorial
def print_factorial(num):
    print("\nFactorial of ", num, "is:", math.factorial(num))
    time.sleep(1)

# Starting time
start_time = time.time()

# Creating threads
t1 = threading.Thread(target=print_square, args=(5,))
t2 = threading.Thread(target=print_factorial, args=(5,))

# Starting threads
t1.start()
t2.start()

# Waiting for threads to complete
t1.join()
t2.join()

# Ending time
end_time = time.time()

# Display total execution time
print("Total Execution Time:", end_time - start_time, "seconds")
