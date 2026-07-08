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


a = 10
b = 20
a, b = b, a
print(a)  # 20
print(b)  # 10

data = ("Cairo", 2026, "Egypt", "Africa", 22_000_000)
city, year, *rest = data
print(city)
print(year)
print(rest)


def get_student():
    return "Alice", 20, "Physics"

name, age, major = get_student()
print(name)
print(age)
print(major)