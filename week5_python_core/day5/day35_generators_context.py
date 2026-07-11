import itertools


#  `fibonacci()` generator — yields infinitely. Use `itertools.islice` to take first 20.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

first_20 = list(itertools.islice(fibonacci(), 20))

# `read_large_file(path)` — yields one line at a time, never loads whole file
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line

for line in read_large_file("large.txt"):
    print(line, end="")

# `integer_range(start, stop, step)` — your own `range()`, no lists
def integer_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step