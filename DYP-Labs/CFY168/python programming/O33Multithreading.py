# multiThreading means creating & running multiple threads.
# Synchronisation means controlling those multiThread.

# multiThreading in python can be acheived by 3 ways
# 1. without creating class
# 2. with extending class Thread
# 3. without extending Thread class

from threading import *
import time

#multithreading without extending any class
def execute1():
    print(f"executing wihtout class! {current_thread().name} ")
    for i in range(10):
        time.sleep(0.2)
        print(f"print {i}")

# thread should be used after the targeted method
# t.join() is used to execute the other thread first then after mainThread will execute

t = Thread(target=execute1)
t.name = "prnv"
t.start()
# t.join()

current_thread().name="Head/Main Thread"
print("this is main thread!")
for i in range(11):
    time.sleep(.3)
    print(current_thread().name)





# Using class without extending Thread class 
class Child_thread:
    def display(self):
        for i in range(11):
            time.sleep(.5)
            print(f"child class Thread: {current_thread().name}")

obj = Child_thread()
th = Thread(target= obj.display)
th.start()
th.name = "2nd Thread without inheritance"

print("\n\n-----------------------------------\n\n")

for i in range(11):
    time.sleep(.5)
    print("Main Thread ", current_thread().name)
    print("Class without inheritance: ", i)




# Using class with extending Thread class 
class Child2(Thread):
    def run(self):   # This method run() is important
        for i in range(11):
            time.sleep(1.5)
            print("child Thread: ", current_thread().name)
        obj.display()

th2 = Child2()
th2.start()
th2.name="3rd Thread with inheritance"

print("\n\n-----------------------------------\n\n")
for i in range(11):
    time.sleep(0.5)
    print(current_thread().name)