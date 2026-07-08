import collections
import sys
import re
from types import MappingProxyType
from unicodedata import name

my_dict = {}
isinstance(my_dict, collections.abc.Mapping)

# Hashable
# All of Python’s immutable built-in objects are hashable
tt = (1, 2, (30, 40))
hash(tt)     # 8027212646858338501
tl = (1, 2, [30, 40])
# hash(tl)     # TypeError: unhashable type: 'list'
tf = (1, 2, frozenset([30, 40]))
hash(tf)     # -4118419923444501110

# Build dictionaries
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e    # True


# Dict comprehension
DIAL_CODES = [
    (86, 'China'),    
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),    
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')]

countary_code = {country: code for (code, country) in DIAL_CODES}
print(countary_code)


# Handling Missing Keys with setdefault
word = re.compile('\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word.finditer(line):
            wordn = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[wordn] = occurrences


with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word.finditer(line):
            wordn = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# Mappings with Flexible Key Lookup
### defaultdict: Another Take on Missing Keys
###### if dd is a defaultdict, and k is a missing key, dd[k] will call the default_factory to create a default value, but dd.get(k) still returns None.
WORD_RE = re.compile('\w+')
index = collections.defaultdict(list)   # Create a defaultdict with the list constructor as default_factory.
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

### The __missing__ Method
###### The __missing__ method is just called by __getitem__ (i.e., for the d[k] operator). 
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def get(self, key, default=None):
        try:
            return self[key]   
        except KeyError:
            return default 
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys() 


# Variations of dict
### OrderedDict
my_odict = collections.OrderedDict()    # Maintains keys in insertion order
my_odict['setup'] = "Done"
my_odict['coding'] = "In Progress"
my_odict['testing'] = "Pending"
my_odict.popitem(last = True)                      # ops the first item by default
my_odict.move_to_end('coding')
d1 = collections.OrderedDict([('a', 1), ('b', 2)])
d2 = collections.OrderedDict([('b', 2), ('a', 1)])
print("Is d1 == d2?", d1 == d2)    # False

### ChainMap
defaults = {'theme': 'Light', 'font': 'Arial', 'show_line_numbers': True}
user_settings = {'theme': 'Dark'}
command_line_args = {'show_line_numbers': False}
config = collections.ChainMap(command_line_args, user_settings, defaults)  # We chain them. The FIRST one in the list has the HIGHEST priority
print(f"Theme: {config['theme']}")               # Found in user_settings -> 'Dark'
print(f"Show Lines: {config['show_line_numbers']}") # Found in command_line_args -> False
print(f"Font: {config['font']}")                 # Found in defaults -> 'Arial'
config['font'] = 'Consolas'                      # it ONLY goes into the first dictionary
print(f"Command line dict: {command_line_args}") # Has 'font': 'Consolas'
print(f"Defaults dict: {defaults['font']}")      # STILL 'Arial' (Untouched!)

### Counter
ct = collections.Counter('abracadabra')          # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')                            # Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.most_common(2)                                # [('a', 10), ('z', 3)]


# Subclassing UserDict
class StrKeyDict(collections.UserDict):          # MutableMapping
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item 


# Immutable Mappings
d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy[2] = 'x'     # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'           # This is okay
d_proxy              # mappingproxy({1: 'A', 2: 'B'})  [Dynamic view]

# Set Theory
l = ['spam', 'spam', 'eggs', 'spam']
set(l)               # {'eggs', 'spam'}
list(set(l))         # ['eggs', 'spam']
###  so, given two sets a and b, a | b returns their union, a & b computes the intersection, and a - b the difference.
###  to create an empty set, you should use the constructor without an argument: set()
s = {1, 2, 3}        # Faster way to create a set
print(type(s))       # <class 'set'>
frozenset(range(10)) # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})


# Set Comprehensions
s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}