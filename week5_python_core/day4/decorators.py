import time
import functools

def decorate(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorate
def target():
    print("Running")

target()


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()        # running inner()


# When Python Executes Decorators
registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()

# running register(<function f1 at 0x000001CA26EECF40>)
# running register(<function f2 at 0x000001CA26EED260>)
# running main()
# registry -> [<function f1 at 0x000001CA26EECF40>, <function f2 at 0x000001CA26EED260>]
# running f1()
# running f2()
# running f3()

# Decorator-Enhanced Strategy Pattern
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discout for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):   
    """Select best discount available"""
    return max(promo(order) for promo in promos)


# Variable Scope Rules
b = 6
def f1(a):
    print(a)        # a
    print(b)        # 6

def f2(a):
    print(a)
    print(b)
    b = 9            # UnboundLocalError: local variable 'b' referenced before assignment

def f3(a):           # This will run
    global b
    print(a)
    print(b)
    b = 9


# Closures
#### a closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there.
class Averager():
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

class Averager1():
    def __init__(self):
        self.total = 0.0
        self.count = 0
    
    def __call__(self, new_value):
        self.count += 1
        self.total += new_value
        return self.total / self.count

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

avg = make_averager()
avg[10]
avg[11]
avg[12]

avg.__code__.co_varnames          # ('new_value', 'total')
avg.__code__.co_freevars          # ('series',)
avg.__closure__[0].cell_contents  # [10, 11, 12]

def make_averager():
    count = 0
    total = 0
    def averager(new_val):
        # count += 1    # UnboundLocalError: local variable 'count' referenced before assignment
        # total += new_val
        nonlocal count, total
        count += 1
        total += new_val
        return total/count
    return averager

# Implementing a Simple Decorator
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
            
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)        
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked