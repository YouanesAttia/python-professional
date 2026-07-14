import numpy as np
import time


arr1 = np.array([1, 2, 3, 4])
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)
arr1 = np.zeros((2, 3))
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)
arr1 = np.ones((2, 3), dtype=np.int64)
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)
arr1 = np.arange(-5, 5, 0.01)
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)
arr1 = np.random.randn(8)
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)
arr1 = np.linspace(5, -5, num=10)
print(
    f"Shape: {arr1.shape}, "
    f"Data type: {arr1.dtype}, "
    f"Dimensions: {arr1.ndim}, "
    f"Size: {arr1.size}"
)

# Broadcasting: add `(3,1)` to `(1,4)` — what shape results? Subtract row mean from every row (no loops).
A = np.array([[1], [2], [3]])
B = np.array([[10, 20, 30, 40]])
print(A + B)       # 3 x 4


X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
centered = X - X.mean(axis=1, keepdims=True)

# Vectorization benchmark: sum 10M numbers with Python loop vs `np.sum()`. Record speedup (~100x).
lst = list(range(10000000))
arr = np.arange(10000000)

start = time.perf_counter()
total = 0
for x in lst:
    total += x
python_time = time.perf_counter() - start

start = time.perf_counter()
sum = np.sum(arr)
numpy_time = time.perf_counter() - start

print(f"Python loop: {python_time:.4f} s")
print(f"NumPy sum : {numpy_time:.4f} s")
print(f"Speedup   : {python_time / numpy_time:.1f}x")
