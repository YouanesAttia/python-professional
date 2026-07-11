import itertools

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

first_20 = list(itertools.islice(fibonacci(), 20))