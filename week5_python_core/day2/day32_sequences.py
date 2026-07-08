import sys

nums = [n for n in range(1000)]
words = ["apple", "banana", "cherry", "cat", "elephant", "dog", "giraffe", "lion"]
matrix = [[1, 2], [3, 4], [5, 6]]

even = [n for n in nums if n % 2 == 0]
table = [[n * m for n in nums] for m in nums]
upper = [word.upper() for word in words]
long = [word for word in words if len(word) > 5]
flattened = [num for row in matrix for num in row]


evengen = (n for n in nums if n % 2 == 0)
uppergen = (word.upper() for word in words)
flattenedgen = (num for row in matrix for num in row)

print(sys.getsizeof(even))
print(sys.getsizeof(evengen))