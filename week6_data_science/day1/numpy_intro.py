import numpy as np
import math

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print (a.shape)
print (a[0, 2])

# Most NumPy arrays have some restrictions. For instance:
#### All elements of the array must be of the same type of data.
#### Once created, the total size of the array can’t change.
#### The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have the same number of columns.

# Array attributes
print(a.ndim)         # 2 (The number of dimentions)
print(a.size)         # The total number of elements in an array
a.size == math.prod(a.shape)
print (a.dtype)       # int

# How to create a basic array
a = np.zeros(2)
print(a)              # [0., 0.]
b = np.ones(3) 
print(b)              # [1., 1., 1.]
g = np.ones(2, dtype=np.int64)
print(g)              # [1, 1]
c = np.empty(2) 
print (c)             # [3.14, 42.  ] may vary
d = np.arange(4)
print(d)              # [0, 1, 2, 3]
e = np.arange(2, 9, 2)
print (e)             # [2, 4, 6, 8]
f = np.linspace(0, 10, num=5)
print (f)             # [ 0. ,  2.5,  5. ,  7.5, 10. ]

# Reshaping
a = np.arange(6)
b = a.reshape(3, 2)
print (b)            # [[0 1] [2 3] [4 5]]

# How to convert a 1D array into a 2D array
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)        # (6,)