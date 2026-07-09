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


import functools

def debug(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper
