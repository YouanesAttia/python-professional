import array
import os
from collections import namedtuple

# A listcomp is meant to do one thing only: to build a new list.
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

# Cartesian product
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for size in sizes for color in colors]

# Generator expressions
# If you only wanted to turn that list into a tuple, you are essentially building a giant list just to "feed" it to the tuple creator, then throwing the list away. It’s like buying a whole cake just to take one bite and throw the rest in the trash.
tuple1 = tuple(ord(symbol) for symbol in symbols)
array.array('I', (ord(symbol) for symbol in symbols)) # is a "C-style" array. It is much leaner and faster, but it has one strict rule: Every item in the array must be the exact same data type
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# Tuples used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport) 
for country, _ in traveler_ids:
    print(country)
t = (20, 8)
quotient, remainder = divmod(*t)
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# filename: 'idrsa.pub'

# Nested Tuple Unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # 1
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # 2
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))

# Named tuples
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo.population  # 36.933

# Slicing
l = [10, 20, 30, 40, 50, 60]
l[:2] # [10, 20]
l[2:] # [30, 40, 50, 60]

# sequence[start : stop : step]
s = 'bicycle'
s[::3] # 'bye'
s[::-1] # 'elcycib'
# These two are doing the exact same thing:
part = s[0:5:2]
part = s[slice(0, 5, 2)]

invoice = """
0.....6..................................40........52..55........
1909  Pimoroni PiBrella                    $17.50   3    $52.50
1489  6mm Tactile Switch x20                $4.95   2     $9.90
1510  Panavise Jr. - PV-201                $28.00   1    $28.00
1601  PiTFT Mini Kit 320x240               $34.95   1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


# Assigning to Slices
l = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]   # [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]          # [0, 1, 20, 30, 5, 8, 9]
l[2:5] = 100        # TypeError: can only assign an iterable

# Using + and * with Sequences
l = [1, 2, 3]
l * 5         # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
5 * 'abcd'    #'abcdabcdabcdabcdabcd'

# Building Lists of Lists
board = [['_'] * 3 for i in range(3)] # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'                     # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
