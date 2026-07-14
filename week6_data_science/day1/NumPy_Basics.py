import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)

arr1 = np.zeros((2, 3))
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)

arr1 = np.ones((2, 3), dtype=np.int64)
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)

arr1 = np.arange(-5, 5, 0.01)
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)

arr1 = np.random.randn((8,8))
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)

arr1 = np.linspace(5, -5, num=10)
print("Shape: " + arr1.shape + " data-type: " + arr1.dtype + " dimentions: " + arr1.ndim + " size: " + arr1.size)


# Broadcasting: add `(3,1)` to `(1,4)` — what shape results? Subtract row mean from every row (no loops).
import numpy as np

A = np.array([[1], [2], [3]])
B = np.array([[10, 20, 30, 40]])
print(A + B)       # 3 x 4


X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
centered = X - X.mean(axis=1, keepdims=True)