import numpy as np
my_arr = np.arange(1000000)
my_list = list(range(1000000))
# If we tried to multiply each element by any num, you will notice that numpy is much faster


# 4.1 The NumPy ndarray: A Multidimensional Array Object
data = np.random.randn(2, 3)
print (data)
print (data * 10)
print (data +data)
print (data.shape)             # (2,3)
print (data.dtype)             # float64

## Creating ndarrays
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print (arr1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print (arr2.shape)

arr3 = np.zeros(10)
arr4 = np.ones(10)
arr5 = np.empty(10)

## Data Types for ndarrays
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int64)
print (arr2.astype(np.bool))

## Arithmetic with NumPy Arrays
#### Arrays are important because they enable you to express batch operations on
#### data without writing any for loops. NumPy users call this vectorization. 
arr1 = np.arange(10, dtype=np.float64)
print(arr1 * arr1)
print(arr1 - arr1)
print(1/arr1)
arr2 = np.arange(5, 15)
print (arr2 > arr1)

## Basic Indexing and Slicing
arr1[5:8] = 12         # 
arr_slice = arr1[5:8]  # Only view of the data
arr_slice[1] = 12345   # arr1 = [ 0,  1,  2,  3,  4, 12, 12345, 12,  8,  9]
arr1[:] = 12           # arr1 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12]


## Boolean Indexing
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(data[names == 'Bob', 2:])       # It will print row 0 and row 3


## Fancy Indexing
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
arr[[4, 3, 0, 6]]
"""
array([[ 4.,  4.,  4.,  4.],
       [ 3.,  3.,  3.,  3.],
       [ 0.,  0.,  0.,  0.],
       [ 6.,  6.,  6.,  6.]])
"""
arr = np.arange(32).reshape((8, 4))
arr[[1, 5, 7, 2], [0, 3, 1, 2]]        # array([ 4, 23, 29, 10])


# Transposing Arrays and Swapping Axes
arr = np.arange(15).reshape((3, 5))
print (arr)
print (arr.T)
np.dot(arr.T, arr)
