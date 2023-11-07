

#Create a NumPy array with 5 elements of your choice.
#Display the 5th element of the array

import pandas as pd
import numpy as np
'''
my_list =  [2,5,7,3,9]

array_1 = np.array(my_list)

print(array_1)
print("The 5th element of the array is:", array_1[4])

my_array = np.array([10, 20, 30, 40, 50])

# Display the 5th element (index 4, as indexing starts from 0)
print("The 5th element of the array is:", my_array[4])

# Use the np.random.randint function to create a 2D array of size (3,4) with random integers between 0 and 10.

array_2 = np.random.randint(0,10, size= (3,4))
print(array_2)

arr1 = np.full((3, 3), fill_value = 5)
identity_1 = np.eye(arr1.shape[0], dtype='int64') 
print(arr1)
print('    +    ')
print(identity_1)
print('    =    ')
print(arr1 + identity_1)

matrix = np.arange(20).reshape(5, 4)

print(matrix[0, 0], matrix[1, 0], matrix[0, 1], matrix[2][0])

temp = matrix.reshape(2, 2, -1)
temp.shape

print(temp)
'''

# Create a NumPy array of random numbers with dimensions 6 x 10. Call it my_array

my_array = np.random.random((6,10))
print(my_array)

# Slice out the 1st, 3rd and 5th column of the array into as new array. Call it new_array

new_array = my_array[:, [0,2,4]]
print(new_array)

# Print the shape of each array you have created.

print("Shape of my_array:", my_array.shape)
print("Shape of new_array:", new_array.shape)

# Try to multiply new_array x my_array. Does it work? If not, do you know why?

#multiple_array = new_array * my_array
#result = np.dot(new_array, my_array)
#this thorwn an error due to not in same shape,,,ValueError: operands could not be broadcast together with shapes (6,3) (6,10)

# Transpose new_array and try again. Does it work now?


# Transpose new_array
new_array_transposed = new_array.T

# Try to multiply new_array_transposed x my_array
# This should work since the dimensions are compatible
result_transposed = np.dot(new_array_transposed, my_array)

# Print the shape of the result after transposing and multiplication
print("Shape of result after transposing and multiplying:", result_transposed.shape)




#Create a NumPy array of dimensions 5 x 5 where each element is a zero.

zero_array = np.zeros((5, 5))
print(zero_array)

#Replace the left diagonal of the array with 1s.

np.fill_diagonal(zero_array, 1)
print(zero_array)


# Create a 3D array of size (3,4,5) and use slicing to select the first two elements of the last dimension.

matrix = np.arange(60).reshape(3,4,5)
print(matrix)

last_two_elemnt = matrix[:, : , :2]
print(last_two_elemnt)


# Select the first two elements of the last dimension using slicing
first_two_elements_last_dim = matrix[..., :2]

# Print the resulting sliced array
print(first_two_elements_last_dim)


# Create a NumPy 1D-array with 10 elements, then reshape the array into a 2x5 matrix.

array_3 = np.arange(10)

matrix_1 = array_3.reshape(2,5)

print(array_3)
print(matrix_1)


# Create a second NumPy array with 5 elements, and join it to the first array using the concatenate function.

array_4 = np.arange(5)

matrix_2 = np.concatenate((array_3, array_4))
print(matrix_2)

# Create two arrays of size (2,3) and broadcast them together to create an array of size (2,3,3).

array_5 = np.random.random((2,3))
array_6 = np.random.random((2,3))

result = array_5.reshape(-1, 1, 3) * array_6.reshape(2, -1, 1)
result.shape

print(result)