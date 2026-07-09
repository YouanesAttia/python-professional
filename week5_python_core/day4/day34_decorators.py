import time
import functools

def timer(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_ms = time.time() * 1000
        result = function(*args, **kwargs)
        end_ms = time.time() * 1000
        elapsed_ms = end_ms - start_ms 
        print(f"Function {function.__name__} took {elapsed_ms:.4f} ms")
        return result
    return wrapper



def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


def retry(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt}/{n} failed for {func.__name__}: {e}")
            
            print(f"Function {func.__name__!r} failed after {n} retries.")
            raise last_exception
        return wrapper
    return decorator