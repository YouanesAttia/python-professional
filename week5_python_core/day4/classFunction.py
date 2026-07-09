# Functions in Python are first-class objects:
### Created at runtime
### Assigned to a variable or element in a data structure
### Passed as an argument to a function
### Returned as the result of a function

from functools import reduce
from operator import add
import random
from inspect import signature
from typing import Annotated
from operator import mul
from operator import itemgetter
from collections import namedtuple
from operator import attrgetter

# Treating a Function Like an Object
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)
print(factorial(42))
type(factorial)           # <class 'function'>
factorial.__doc__         # 'return n!'

fact = factorial
fact(5)                   # 120
l = list(map(factorial, range(11)))


# Higher-Order Functions
#### A function that takes a function as argument or returns a function as the result is a higher-order function. 
#### Examples: map, filter, reduce, and apply
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)    # Higher-Order

def reverse(word):
    return word[::-1]
sorted(fruits, key=reverse)


# Modern Replacements for map, filter, and reduce
l1 = list(map(fact, range(6)))
l1 = [fact(n) for n in range(6)]
l2 = list(map(factorial, filter(lambda n: n % 2, range(6)))) 
l2 = [factorial(n) for n in range(6) if n % 2]
reduce(add, range(100))
sum(range(100))           # Faster
all(iter)                 # True if all is true
any(iter)                 # True if one is true


# Anonymous Functions
sorted(fruits, key=lambda word: word[::-1])


# User-Defined Callable Types
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
bingo.pick()         # pop a num
bingo()              # pop a num
callable(bingo)      # True


# Function Introspection
dir(factorial)
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()
upper_case_name.short_description = 'Customer name'

class C: pass  
obj = C()  
def func(): pass
sorted(set(dir(func)) - set(dir(obj))) # ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__',
# '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']


# From Positional to Keyword-Only Parameters
#### The ** prefix tells Python: "Take any remaining keyword arguments and put them into a dictionary named attrs."
#### The * prefix tells Python: "Take all the positional arguments that follow and put them into a tuple named content."
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br')) 
# Result: '<br />'

print(tag('p', 'hello')) 
# Result: '<p>hello</p>'

print(tag('p', 'hello', 'world'))
# Result: 
# <p>hello</p>
# <p>world</p>

print(tag('p', 'hello', id=33))
# Result: '<p id="33">hello</p>'

print(tag('p', 'hello', 'world', cls='sidebar'))
# Result: 
# <p class="sidebar">hello</p>
# <p class="sidebar">world</p>

print(tag(content='testing', name="img"))
# Result: '<img content="testing" />'

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 
          'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))
# Result: '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'



# Retrieving Information About Parameters
def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

clip.__defaults__          # (80, )
clip.__code__.co_varnames  # ('text', 'max_len', 'end', 'space_before', 'space_after')
clip.__code__.co_argcount  # 2

sig = signature(clip)
str(sig)                   # '(text, max_len=80)'
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)      # POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
                                                          # POSITIONAL_OR_KEYWORD : max_len = 80

# The kind attribute holds one of five possible values from the _ParameterKind class:
###  POSITIONAL_OR_KEYWORD
###  VAR_POSITIONAL: A tuple of positional parameters.
###  VAR_KEYWORD: A dict of keyword parameters
###  KEYWORD_ONLY: A keyword-only parameter (new in Python 3).
###  POSITIONAL_ONLY



# Function Annotations
def clip(text: str, max_len: Annotated[int, "must be > 0"] = 80) -> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

clip.__annotations__        # {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}



# Packages for Functional Programming
def fact1(n: int) -> int:
    return reduce(lambda a,b: a*b, range(1, n+1))

def fact2(n: int) -> int:
    return reduce(mul, range(1, n+1))

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

latLong = namedtuple('latLong', 'lat long')
metropolis = namedtuple('metropolis', 'name cc pop coord')
metro_areas = [metropolis(name, cc, pop, latLong(lat, long))
                    for name, cc, pop, (lat, long) in metro_data]
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))