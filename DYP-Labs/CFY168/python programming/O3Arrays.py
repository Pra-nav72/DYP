# import array as arr


# list1=["hello", "world", "ankit", "stop"]
# list2=[1, 324, 22, 34, 34, 33]
# arr_my = arr.array([list1, list2])
# print(arr_my.dtype)

import numpy as np

# Create an array where elements are lists
my_array = np.array([[1, 2], [3, 4, 5], [6]])

print(my_array)
print(my_array.dtype)