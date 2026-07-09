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
