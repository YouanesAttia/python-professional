import time
from operator import mul
from functools import reduce

def timer(function):
    def wrapper(*args, **kwargs):
        start_ms = time.time() * 1000
        result = function(*args, **kwargs)
        end_ms = time.time() * 1000
        elapsed_ms = end_ms - start_ms 
        print(f"Function {function.__name__} took {elapsed_ms:.4f} ms")
        return result
    return wrapper
